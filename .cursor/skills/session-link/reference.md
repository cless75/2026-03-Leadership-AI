# Справочник: session-link

**Навык:** [SKILL.md](SKILL.md)
**Команды:** [session-start](.claude/commands/session-start.md), [session-close](.claude/commands/session-close.md), [session-result](.claude/commands/session-result.md)

---

## Канон путей

| Сущность | Путь |
|---|---|
| Ежедневная заметка | `YYYY/01-Daily/YYYY-MM-DD.md` (год в пути = год даты; пример: `2026/01-Daily/2026-04-03.md`) |
| Чат-мост | `.claude/session-handoff.md` |
| Wiki-ссылка на день | `[[YYYY-MM-DD]]` |
| Vault | `504-demo` (`C:\Obs-Vaults\504-demo`) |

---

## Карта статусов

| Эмодзи | Статус |
|---|---|
| 🔵 | Старт |
| 🟡 | Продолжение |
| 🟢 | Выполнено |
| 🟣 | DoD на сегодня завершён |
| ⚪ | Отложена |
| 🔴 | Не сработало |

---

## Примеры блоков

### Старт

```markdown
### 09:15 [[Подготовка HW M3]] (🔵 Старт)
- [ ] Начало работы · Claude Code
```

### Продолжение (тот же день, новый заход)

```markdown
### 14:30 [[Подготовка HW M3]] (🟡 Продолжение)
- [ ] Начало работы · Claude Code
```

### Промежуточный итог

Дописывается **под открытым** заголовком 🔵 / 🟡, статус в скобках не меняется:

```markdown
- [x] Собрал карту стейкхолдеров по S3.01
- [ ] Следующий шаг: пройти контр-тест перед финализацией диагноза Влада
```

### Финал (смена статуса)

Заменить скобки в том же заголовке:

```markdown
### 09:15 [[Подготовка HW M3]] (🟢 Выполнено)
- [x] Собрал карту стейкхолдеров по S3.01
- [x] Итог: карта готова, союзники и оппоненты размечены, ОНМС по тактике переговоров зафиксирован

**Следующие шаги (2026-04-25):**
- Разобрать конфликт-протокол S3.04 с кейсом PO
- Перед M3 end — пройти /mid-course-diagnostic
```

---

## Чат-мост `session-handoff.md`

Назначение: компактное резюме для **следующего** AI-чата, без необходимости читать весь daily. Дописывается после **CLOSE** по умолчанию (opt-out по просьбе).

Блок в `.claude/session-handoff.md`:

```markdown
## Session handoff 2026-04-25 14:30

- Тема: Подготовка HW M3
- Сделано:
  - Собрал карту стейкхолдеров по S3.01
  - Прошёл контр-тест по Владу, диагноз «нарцисс» снижен до «нарциссические черты в стрессе»
- Следующие шаги:
  - Разобрать конфликт-протокол S3.04 с кейсом PO
  - /mid-course-diagnostic перед началом M3 end
- Связанные файлы: [[My-Notes/M3-S3.01-stakeholder-map]], [[My-Notes/M3-S3.05-shadow-profiling]]
```

Правила:
- 2–3 пункта «сделано», 1–3 «следующих шага».
- Имена стейкхолдеров обезличить, если handoff может покинуть vault.
- Не дублировать полные выводы — только указатели на файлы через wikilinks.

---

## Формат ссылок

Все ссылки на файлы vault — **wikilinks** `[[path]]` или `[[path|alias]]`. Не использовать: `[текст](url)`, backticks `` `path` ``.

---

## CLI

| Действие | Команда |
|---|---|
| Открыть файл в Cursor | `cursor "C:\Obs-Vaults\504-demo\path\to\file.md"` |
| Открыть в Obsidian по URI | `obsidian://open?vault=504-demo&file=<путь-от-корня-vault>` (URL-encode параметров) |
| Открыть сегодняшний daily (если Obsidian Daily notes настроены) | `obsidian daily` |

---

## Mid-Course Diagnostic Gate

Gate активируется при `/session-start` на M3+ без актуального `mid-course-diagnostic-*.md` в `MS_PROFILE_PATH`. Подробнее — раздел «Mid-Course Diagnostic Gate» в [SKILL.md](SKILL.md). Связанный навык: [ms-participant-profile](../ms-participant-profile/SKILL.md).

---

## Границы с навыками пакета

| Запрос | Куда |
|---|---|
| START / MID / CLOSE в дне + опц. handoff | session-link |
| Идея на ходу, 1–2 строки | idea-capture |
| Принятие решения по ОНМС | micro-decision-514 |
| Pipeline «проблема → диагностика → решение» | stai-problem-solving |
| Initial Intake / Refresh / Mid-Course / Synthesis профиля | ms-participant-profile |
| Черновик сдачи HW | 504-hw-submit-prep |
