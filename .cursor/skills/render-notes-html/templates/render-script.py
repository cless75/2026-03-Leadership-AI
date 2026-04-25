"""Dashboard прогресса участника 504.

Запуск:
  python render-script.py \
    --period day|week|module|range \
    --arg <YYYY-MM-DD | M2 | YYYY-MM-DD..YYYY-MM-DD> \
    --participant "Псевдоним" \
    --vault-root "C:/path/to/repo-or-clone" \
    [--include-private]

Выход: HTML на Desktop/<participant>/dashboard-YYYY-MM-DD.html
"""
import argparse
import re
from datetime import date, datetime, timedelta
from pathlib import Path

import markdown


# --- args ---

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--period", choices=["day", "week", "module", "range"], required=True)
    p.add_argument("--arg", default="")
    p.add_argument("--participant", default="participant")
    p.add_argument("--vault-root", required=True)
    p.add_argument("--include-private", action="store_true")
    p.add_argument("--css-file", default=None, help="Path to dashboard-css.css")
    return p.parse_args()


# --- date range ---

def resolve_range(period, arg):
    today = date.today()
    if period == "day":
        d = datetime.strptime(arg, "%Y-%m-%d").date() if arg else today
        return d, d
    if period == "week":
        end = today
        start = end - timedelta(days=6)
        return start, end
    if period == "range":
        a, b = arg.split("..")
        return datetime.strptime(a, "%Y-%m-%d").date(), datetime.strptime(b, "%Y-%m-%d").date()
    if period == "module":
        # Module — без даты-фильтра, фильтр по тегу/имени модуля.
        return None, None
    raise ValueError(f"Unknown period {period}")


# --- frontmatter ---

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_fm(text):
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, text[m.end():]


def file_date(path, fm):
    cdate = fm.get("CDate") or fm.get("date")
    if cdate:
        try:
            return datetime.strptime(cdate[:10], "%Y-%m-%d").date()
        except ValueError:
            pass
    return date.fromtimestamp(path.stat().st_mtime)


# --- collect files ---

NOTES_FOLDERS = {
    "Public": "public",
    "Sessions": "personal",
    "Logs": "personal",
    "Diagnostics": "personal",
    "HW": "personal",
    "Ideas": "personal",
}


def collect_entries(vault_root, start, end, period, arg, include_private):
    root = Path(vault_root) / "My-Notes"
    if not root.exists():
        return []
    entries = []
    for folder, default_privacy in NOTES_FOLDERS.items():
        folder_path = root / folder
        if not folder_path.exists():
            continue
        for f in folder_path.glob("*.md"):
            text = f.read_text(encoding="utf-8", errors="replace")
            fm, body = parse_fm(text)
            privacy = fm.get("privacy", default_privacy)
            kind = fm.get("kind", "other")
            d = file_date(f, fm)
            # period filter
            if period in ("day", "week", "range"):
                if not (start <= d <= end):
                    continue
            elif period == "module":
                # Module-N: ищем в имени файла или тегах
                module_tag = arg  # например "M2"
                fname = f.name
                if module_tag.upper() not in fname.upper() and module_tag.upper() not in fm.get("tags", "").upper():
                    continue
            entries.append({
                "path": f,
                "fm": fm,
                "body": body,
                "privacy": privacy,
                "kind": kind,
                "date": d,
                "folder": folder,
                "title": fm.get("title", f.stem),
            })
    if include_private:
        priv_path = root / "Private"
        if priv_path.exists():
            for f in priv_path.glob("*.md"):
                text = f.read_text(encoding="utf-8", errors="replace")
                fm, body = parse_fm(text)
                d = file_date(f, fm)
                if period in ("day", "week", "range"):
                    if not (start <= d <= end):
                        continue
                entries.append({
                    "path": f,
                    "fm": fm,
                    "body": body,
                    "privacy": "private",
                    "kind": fm.get("kind", "other"),
                    "date": d,
                    "folder": "Private",
                    "title": fm.get("title", f.stem),
                })
    entries.sort(key=lambda e: (e["date"], e["folder"]))
    return entries


# --- status / EQ / experiments ---

def read_optional(path):
    p = Path(path)
    if not p.exists():
        return None, None, None
    text = p.read_text(encoding="utf-8", errors="replace")
    fm, body = parse_fm(text)
    return p, fm, body


def get_burnout_status(vault_root):
    """Latest Diagnostics/burnout-*.md."""
    root = Path(vault_root) / "My-Notes" / "Diagnostics"
    if not root.exists():
        return None
    files = sorted(root.glob("burnout-*.md"), reverse=True)
    if not files:
        return None
    text = files[0].read_text(encoding="utf-8", errors="replace")
    fm, body = parse_fm(text)
    zone = fm.get("zone", "unknown")
    return {"zone": zone, "date": file_date(files[0], fm), "file": files[0]}


def get_profile_status(vault_root):
    """ms-profile.md if available."""
    candidates = [
        Path(vault_root) / "ms-profile.md",
        Path(vault_root) / "My-Notes" / "Diagnostics" / "ms-profile.md",
        Path(vault_root) / "my-profile.md",  # legacy
    ]
    for c in candidates:
        if c.exists():
            text = c.read_text(encoding="utf-8", errors="replace")
            fm, body = parse_fm(text)
            return {"version": fm.get("ProfileVersion", "—"), "active_program": fm.get("StartProgram", "—"), "file": c}
    return None


# --- render HTML ---

def badge_class(privacy):
    return {"public": "badge-public", "personal": "badge-personal", "private": "badge-private"}.get(privacy, "badge-personal")


def zone_css(zone):
    return {"green": "zone-green", "yellow": "zone-yellow", "orange": "zone-orange", "red": "zone-red"}.get(zone, "")


def render_html(args, entries, has_private, status, profile, css):
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])
    title = f"Dashboard — {args.participant}"
    # banner
    banner = ""
    if has_private:
        banner = '<div class="banner-private">⚠️ Этот рендер содержит Private-файлы. Не передавать никому. Перечитывать только локально.</div>'

    # status row
    status_cards = []
    if status:
        zone = status["zone"]
        z_css = zone_css(zone)
        status_cards.append(f'<div class="status-card {z_css}"><div class="label">Burnout</div><div class="value">{zone}</div></div>')
    if profile:
        status_cards.append(f'<div class="status-card"><div class="label">Profile</div><div class="value">{profile["version"]}</div></div>')
        status_cards.append(f'<div class="status-card"><div class="label">Программа</div><div class="value">{profile["active_program"]}</div></div>')
    status_html = '<div class="status-row">' + "".join(status_cards) + '</div>' if status_cards else '<p>Нет данных о статусе. Запусти <code>/burnout-check</code> и <code>/profile-intake</code>.</p>'

    # timeline by day
    days = {}
    for e in entries:
        days.setdefault(e["date"], []).append(e)
    timeline_html = ""
    for d in sorted(days.keys()):
        timeline_html += f'<div class="day-block"><h3>{d.isoformat()} ({d.strftime("%a")})</h3>'
        for e in days[d]:
            badge = badge_class(e["privacy"])
            body_html = md.convert(e["body"])
            md.reset()
            timeline_html += (
                f'<details class="entry"><summary>'
                f'<span class="badge {badge}">{e["privacy"]}</span> '
                f'<span class="badge badge-kind">{e["kind"]}</span> '
                f'<span class="badge badge-kind">{e["folder"]}</span> '
                f'{e["title"]}'
                f'</summary><div class="body">{body_html}</div></details>'
            )
        timeline_html += '</div>'
    if not timeline_html:
        timeline_html = '<p>Нет записей за выбранный период.</p>'

    # stats
    n_logs = sum(1 for e in entries if e["kind"] == "log")
    n_conspects = sum(1 for e in entries if e["kind"] == "conspect")
    n_diag = sum(1 for e in entries if e["kind"] == "diagnostic")
    n_hw = sum(1 for e in entries if e["kind"] == "hw")
    n_ideas = sum(1 for e in entries if e["kind"] == "idea")
    stats_html = (
        '<div class="stats-row">'
        f'<div class="stat-card"><div class="num">{n_logs}</div><div class="label">Logs</div></div>'
        f'<div class="stat-card"><div class="num">{n_conspects}</div><div class="label">Conspects</div></div>'
        f'<div class="stat-card"><div class="num">{n_diag}</div><div class="label">Diagnostics</div></div>'
        f'<div class="stat-card"><div class="num">{n_hw}</div><div class="label">HW</div></div>'
        f'<div class="stat-card"><div class="num">{n_ideas}</div><div class="label">Ideas</div></div>'
        '</div>'
    )

    period_str = f"{args.period} {args.arg}" if args.arg else args.period
    today_str = date.today().isoformat()

    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — {today_str}</title>
<style>{css}</style>
</head>
<body>
<div class="wrap">
<header class="dash">
  <div class="eyebrow">Мастерская 504 · Dashboard прогресса</div>
  <h1>{title}</h1>
  <div class="meta">Период: <strong>{period_str}</strong> · Сгенерировано: {today_str}</div>
</header>

{banner}

<section>
  <h2>Текущий статус</h2>
  {status_html}
</section>

<section>
  <h2>Хронология</h2>
  {timeline_html}
</section>

<section>
  <h2>Статистика</h2>
  {stats_html}
</section>

<footer class="dash">
  Стратегическая мастерская · master-strategy.ru · Dashboard участника
</footer>
</div>
</body>
</html>
"""
    return html


# --- main ---

def main():
    args = parse_args()
    start, end = resolve_range(args.period, args.arg)
    entries = collect_entries(args.vault_root, start, end, args.period, args.arg, args.include_private)
    has_private = any(e["privacy"] == "private" for e in entries)
    status = get_burnout_status(args.vault_root)
    profile = get_profile_status(args.vault_root)

    css_path = args.css_file or str(Path(__file__).parent / "dashboard-css.css")
    css = Path(css_path).read_text(encoding="utf-8") if Path(css_path).exists() else ""

    html = render_html(args, entries, has_private, status, profile, css)

    desktop = Path.home() / "Desktop" / args.participant
    desktop.mkdir(parents=True, exist_ok=True)
    out = desktop / f"dashboard-{date.today().isoformat()}.html"
    out.write_text(html, encoding="utf-8")
    print(f"Written: {out}")
    print(f"Size: {out.stat().st_size} bytes")
    print(f"Has private files: {has_private}")
    print(f"Entries: {len(entries)}")


if __name__ == "__main__":
    main()
