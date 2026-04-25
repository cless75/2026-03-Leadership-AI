# Команда: render-notes

Сгенерируй **Dashboard прогресса** в HTML за период по навыку **render-notes-html**.

## Входные данные

Аргумент: $ARGUMENTS

Варианты:
- `day` или `day YYYY-MM-DD` — за день (по умолчанию — сегодня)
- `week` — последние 7 дней (по умолчанию при пустом аргументе)
- `module M2` — по модулю
- `range YYYY-MM-DD..YYYY-MM-DD` — произвольный диапазон
- `include-private` — добавить файлы из `My-Notes/Private/` (по умолчанию исключены)

## Методология

**Канон навыка:** [.cursor/skills/render-notes-html/SKILL.md](../../.cursor/skills/render-notes-html/SKILL.md)
**Скрипт:** [.cursor/skills/render-notes-html/templates/render-script.py](../../.cursor/skills/render-notes-html/templates/render-script.py)
**CSS:** [.cursor/skills/render-notes-html/templates/dashboard-css.css](../../.cursor/skills/render-notes-html/templates/dashboard-css.css)

## Порядок выполнения

1. Распарсить аргументы (период + опции).
2. Прочитать псевдоним участника (из `ms-profile.md` / `my-profile.md`); при отсутствии спросить и сохранить в `.claude/settings.local.json` ключ `PARTICIPANT_DESKTOP_FOLDER`.
3. Запустить Python:
   ```bash
   python ".cursor/skills/render-notes-html/templates/render-script.py" \
     --period <period> \
     --arg <arg> \
     --participant "<псевдоним>" \
     --vault-root "<root репо>" \
     [--include-private]
   ```
4. Скрипт собирает Dashboard, кладёт HTML в `Desktop/<участник>/dashboard-YYYY-MM-DD.html`.
5. Открыть в браузере (`Invoke-Item` или `start`).
6. Сообщить участнику путь, бейджи, наличие Private-баннера.

## Важно

- **Не для передачи.** Если нужно ментору — `/mentor-handoff`.
- **Только локально.** Размещение на Desktop, не в репо.
- **При наличии Private-файлов** — баннер сверху HTML; участник видит и не передаёт никому.
- **Зависимости:** Python 3 + библиотека `markdown` (если не установлена — `pip install markdown`).
