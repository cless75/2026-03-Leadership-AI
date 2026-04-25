# Справочник: render-notes-html

**Навык:** [SKILL.md](SKILL.md)

## Источники данных по секциям Dashboard

### Шапка

- **Псевдоним:** frontmatter `ms-profile.md` поле `name`, либо `my-profile.md` поле `Псевдоним`. Если оба отсутствуют — спросить участника один раз и сохранить в `.claude/settings.local.json`.
- **Период:** аргумент команды.
- **Дата генерации:** текущая дата.

### Текущий статус

- **Burnout-зона:** из последнего файла `My-Notes/Diagnostics/burnout-*.md`. Frontmatter поле `zone` (`green` / `yellow` / `orange` / `red`) или из заголовка секции «Сводная зона».
- **Версия профиля:** frontmatter `ms-profile.md` поле `ProfileVersion`.
- **Активная программа:** frontmatter `ms-profile.md` поле `MS_Programs_Timeline`, статус `active`.
- **Health flags:** frontmatter `ms-profile.md` секция «Прогресс по программам» — поля `health_signal` для активной программы.

Fallback при отсутствии данных: «нет данных» в соответствующей ячейке.

### Прогресс EQ

- **Источники:** все файлы `My-Notes/Diagnostics/*EQ*.md` или с `kind: diagnostic` + tag `eq`. Также секция 5 текущего и предыдущих `ms-profile.md` версий (если хранится `ms-profile.history/`).
- **Парсинг:** искать таблицу с 5 компонентами Гоулмана и оценками 1–5; брать пары (date, score) для каждого компонента.
- **Визуализация:** inline SVG. Простой line-график 5 цветами (по компоненту), ось X — даты, ось Y — оценка.
- **Если <2 точек:** не показывать график, только текущая таблица с одной точкой.

### Timeline

- **Glob входов:** `My-Notes/Public/*.md`, `My-Notes/Sessions/*.md`, `My-Notes/Logs/*.md`, `My-Notes/Diagnostics/*.md`, `My-Notes/HW/*.md`, `My-Notes/Ideas/*.md`. По умолчанию **исключить** `My-Notes/Private/*.md`; включить только при явном `include-private` в аргументе.
- **Также входы из daily:** `2026/01-Daily/YYYY-MM-DD.md` за период (как индекс — короткие ссылки).
- **Сортировка:** по `CDate` frontmatter, при отсутствии — по mtime файла.
- **Группировка:** по дням (заголовок `### YYYY-MM-DD (день недели)` для каждого дня).
- **Внутри дня:** список файлов с бейджем privacy + kind, заголовком, и расхлопывающейся секцией `<details>` с содержимым.

### Активные эксперименты

- **Источники:** секция «Эксперименты» в `M3-S0.03-my-shadow.md`, `ms-profile.md` секция 5. Также любой файл с frontmatter `kind: experiment` (если используется в будущем).
- **Парсинг:** искать списки с маркерами «**Эксперимент N**» или нумерацию + дата начала + due-дата.
- **Статус:** активный (default) / завершён (если есть пометка ✅ или дата завершения) / просрочен (due прошла, не завершён).

### Открытые вопросы

- **Источник:** `My-Notes/open-questions.md` или любой файл с tag `open-questions` / `unresolved`.
- **Парсинг:** список вопросов с маркерами статуса (открыт / в работе / закрыт).

### Decisions log

- **Источник:** `My-Notes/Diagnostics/decisions-log.md` или `My-Notes/Logs/decisions-log.md`.
- **Парсинг:** последние 5–10 датированных секций с формулой «A, а не B, потому что C, чтобы D».

### Footer / статистика

- Считать по timeline за период:
  - сколько Logs
  - сколько Sessions (conspect)
  - сколько Diagnostics
  - сколько HW
  - сколько Ideas
  - средний интервал между Logs (для оценки регулярности)

## Frontmatter, который читает скрипт

```yaml
privacy: public | personal | private
kind: log | conspect | hw | diagnostic | idea | reflection | other
CDate: YYYY-MM-DD
```

Остальные поля frontmatter — игнорируются для render.

## Палитра CSS (см. dashboard-css.css)

- `--ink: #0C2340` — темно-синий (тексты, заголовки)
- `--accent: #3DCBC0` — бирюзовый (акценты, бейджи)
- `--bg: #F8FFF2` — светлый фон
- `--panel: #FFFFFF` — карточки
- Бейджи privacy:
  - public — `#3DCBC0` (бирюзовый)
  - personal — `#F7AF22` (оранжевый, заливка)
  - private — `#D32F2F` (красный)

## Fallback и пограничные случаи

| Случай | Действие |
|---|---|
| Папки `My-Notes/Sessions/` или `Logs/` не существует | Создать пустую секцию с пометкой «нет файлов в этой папке за период» |
| `ms-profile.md` отсутствует | Шапка без псевдонима, статус и EQ — «нет данных» |
| `burnout-*` отсутствует | Секция Status — «диагностика выгорания не пройдена; рекомендация — `/burnout-check`» |
| Все файлы за период из Private | Показать баннер вверху, не показывать содержимое (только метаданные) |
| Markdown файл без frontmatter | Считать `privacy: personal`, `kind: other` |
| Период range пересекает текущую дату | Включить файлы до **сегодня включительно** |

## Запуск Python-скрипта

Wrapper-команда `/render-notes` (в `.claude/commands/render-notes.md`) формирует запрос к скрипту:

```bash
python templates/render-script.py \
  --period <day|week|module|range> \
  --arg <YYYY-MM-DD | M2 | YYYY-MM-DD..YYYY-MM-DD> \
  --participant "<псевдоним>" \
  --include-private  # опционально
```

Скрипт читает файлы по политике, генерирует HTML на Desktop, открывает в браузере.

## Связи

- `Storage-Policy/Privacy-and-Storage-Policy.md`
- `templates/render-script.py` — генератор
- `templates/dashboard-css.css` — стили
