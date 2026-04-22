# 2026-03-Leadership-AI — мастерская 504 (AI Empowered Team)

Автономный Obsidian-vault и студенческий AI-пакет для курса **504**. Репозиторий выровнен по всем четырём модулям и разделён на три слоя:

- служебные AI-инструменты в `.cursor/skills/` и `.claude/commands/`;
- учебные материалы по модулям `Module-1/` ... `Module-4/`;
- пакет установки и шаблонов в `Student-AI-Pack/`.

## Структура репозитория

```text
.
├─ .cursor/skills/          # служебные навыки пакета
├─ .claude/commands/        # команды Claude Code
├─ BoK/                     # общая база знаний курса
├─ Module-1/                # участник + NotebookLM
├─ Module-2/                # участник + NotebookLM
├─ Module-3/                # участник + NotebookLM
├─ Module-4/                # участник + NotebookLM
└─ Student-AI-Pack/         # install, manifest, templates
```

## Модули курса

| Модуль | Область | Что лежит в репозитории |
|--------|---------|--------------------------|
| **M1** | Коммуникация | `Participant/`, `NotebookLM/`, `Module-1-Overview.md` |
| **M2** | Процессы и сотрудничество | `Participant/`, `NotebookLM/`, `Module-2-Overview.md` |
| **M3** | Стейкхолдеры | `Participant/`, `NotebookLM/` |
| **M4** | Динамика, миссия, стратегия развития | `Participant/`, `NotebookLM/`, `README.md`, корневые NLM manifest/checklist |

> Канон participant-слоя: в Git лежат публичные материалы участника и NotebookLM-пакеты. Внутренний операционный контур курса и private-файлы сюда не входят.

## Быстрый старт

```bash
git clone https://github.com/cless75/2026-03-Leadership-AI.git
cd 2026-03-Leadership-AI
```

Откройте папку репозитория в **Cursor** или **Claude Code** как корень проекта.

Далее: [[Student-AI-Pack/INSTALL|INSTALL]], [[Student-AI-Pack/MANIFEST|MANIFEST]], [[504-LEARNING-JOURNEY|учебный процесс]], [[504-HOMEWORK-GUIDE|домашние задания]].

## Документация для AI

См. `CLAUDE.md` в корне — режимы работы, ПЗ, таблица «сценарий → команда → навык».

## Личные файлы

Не коммитьте:

- `my-profile.md`
- `goals-504.md`
- содержимое `My-Notes/`
- локальные настройки `.obsidian/`
- служебные локальные файлы `.claude/settings.local.json`
- рабочие артефакты из `2026/`

См. `.gitignore`.
