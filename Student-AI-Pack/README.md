---
ProjectId: 504
Type: student-ai-pack
tags: [504, student-pack, claude, cursor]
CDate: 2026-04-03
---

# Пакет участника + AI — мастерская 504

Этот каталог описывает **студенческий дистрибутив** для работы с **Claude Code**, **Cursor** и загрузки **Skills в Claude.ai**. Этот vault — автономная копия для участников; канонический курс ведётся командой MDPG отдельно.

## Что внутри

| Элемент | Описание |
|---------|----------|
| [[MANIFEST|MANIFEST.md]] | Полный список папок и навыков для копирования в релиз |
| [[INSTALL|INSTALL.md]] | Быстрый старт после распаковки или `git clone` |
| [[templates/goals-intake|templates/goals-intake.md]] | Опрос целей на курс |
| [[templates/participant-profile.template|Шаблон профиля]] | Основа для `my-profile.md` |
| [[templates/hw-submission-checklist|Чеклист сдачи ДЗ]] | Перед отправкой домашки |

## Навигация по курсу

- [[504-LEARNING-JOURNEY|Учебный процесс и ключевые концепты по неделям]]
- [[504-HOMEWORK-GUIDE|Работа с домашними заданиями]]
- [[Week-1/Week-1-Overview|Week 1 — обзор]] · материалы: `Week-1/Participant/`
- [[Week-2/Week-2-Overview|Week 2 — обзор]] · материалы: `Week-2/Participant/`

Недели 3–4 — по материалам, которые выдаст команда курса.

## Служебные навыки (в репозитории vault)

После клонирования или распаковки они лежат в `.cursor/skills/`:

- **course-goals-intake** — провести опрос по шаблону целей, сохранить итог в `goals-504.md`.
- **participant-profile-load** — прочитать ваш заполненный профиль `.md` и выдать структурированное резюме для контекста.
- **504-hw-submit-prep** — собрать черновик сдачи ДЗ недели N по чеклисту.
- **stai-problem-solving** — полный pipeline системного решения проблемы по методологии курса **STAI** (514). Команда: `/solve-problem`.

## EQ (эмоциональный интеллект)

Полноценный публичный навык: **eq-self-diagnosis** (модель Гоулмана, мини-кейсы, сценарии). Краткий вход и связь с неделей 1:

- [[Week-1/Participant/EQ-504-Entry|EQ-504-Entry]]

## Три способа получить пакет

1. **Архив (Google Drive и др.):** по запросу команды курса — дерево по [[MANIFEST|MANIFEST]] → ZIP.
2. **Claude.ai:** загрузите папки навыков из MANIFEST как отдельные Skills (каждая с `SKILL.md` в корне).
3. **GitHub:** [cless75/2026-03-Leadership-AI](https://github.com/cless75/2026-03-Leadership-AI) — `git clone`, затем открыть корень в Claude Code / Cursor. Шаги: [[INSTALL|INSTALL]].

## Материалы недель (участник)

В дистрибутив входят файлы из `Week-1/Participant/`, `Week-2/Participant/` и обзоры [[Week-1/Week-1-Overview|Week 1]], [[Week-2/Week-2-Overview|Week 2]].
