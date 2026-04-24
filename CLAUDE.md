# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

## Overview

Obsidian vault **504-demo** / репозиторий **2026-03-Leadership-AI**: материалы мастерской **504 AI Empowered Team**, русский язык по умолчанию.

- Ежедневные заметки: **`YYYY/01-Daily/YYYY-MM-DD.md`**
- Session-handoff: **`.claude/session-handoff.md`**
- Ссылки на файлы vault — **Obsidian wikilinks** `[[path]]` или `[[path|alias]]`

## Язык по умолчанию

Все ответы и документация — **по-русски**. Переключаться на другой язык только по явной просьбе участника. (источник: `.cursor/rules/russian-input-output.mdc`, `alwaysApply: true`)

## Структура репозитория

- `Module-1/` … `Module-4/` — учебные модули. Каждый содержит `Participant/` и `NotebookLM/`; у M4 также `Facilitator/`, `Admin/`.
- `BoK/` — общая база знаний курса (`Concepts/`, `Principles/`, `Skills/`).
- `Student-AI-Pack/` — установщик и шаблоны: `README`, `INSTALL`, `MANIFEST`, `templates/`.
- `My-Notes/` — личные конспекты участника (в git только `README.md` и `TEMPLATE-WN-summary.md`).
- `.cursor/skills/` и `.claude/commands/` — служебные навыки пакета.
- Приватные материалы фасилитаторов и папка `2026/` — **вне git** (см. «Что не коммитить»).

## Навигация для участника

- [[504-LEARNING-JOURNEY|Учебный процесс и недели]]
- [[504-HOMEWORK-GUIDE|Домашние задания]]
- [[Student-AI-Pack/README|Student-AI-Pack]] · [[Student-AI-Pack/MANIFEST|MANIFEST]]

## Пре-сессия и ПЗ

Перед содержательной работой:

1. При необходимости уточнить **Objective** и путь к **ПЗ** (`ПЗ-*.md`, `*-п-*.md`) — см. `.cursor/skills/session-link/reference.md`.
2. Прочитать последние строки `## Ход работы` и при необходимости `## Открытые вопросы` в ПЗ.
3. Если ПЗ нет — по договорённости создать `ПЗ-<тема>.md` с секциями: Контекст, Ключевые решения, Ход работы, Открытые вопросы, Артефакты.

**session-link** дополняет ПЗ и журнал дня; не заменяет ведение ПЗ.

## Сценарий → команда → навык → артефакт

| Триггер (пример) | Команда | Навык | Артефакт / выход |
|------------------|---------|-------|------------------|
| зафиксируй сессию, checkpoint, session close | `/session-close` | session-link | ПЗ, Notes, `## Заметки в течение дня`, handoff |
| старт сессии | `/session-start` | session-link | штамп в Objective, журнал |
| итог сессии | `/session-result` | session-link | CLOSE |
| Идея:, зафиксируй идею | `/idea-capture` | idea-capture | `YYYY/01-Daily/…` → `## Входящие дня` |
| самодиагностика EQ, мини-кейс EQ | `/eq-self-diagnosis` | eq-self-diagnosis | протокол EQ |
| принять решение, ОНМС | `/micro-decision-514` | micro-decision-514 | формула A/B/C/D, дерево |
| решить проблему, системный анализ | `/solve-problem` | stai-problem-solving | pipeline STAI |
| опрос целей на курс | `/course-goals-intake` | course-goals-intake | `goals-504.md` |
| загрузи профиль | `/participant-profile-load` | participant-profile-load | резюме профиля |
| подготовь ДЗ 504 | `/504-hw-submit-prep` | 504-hw-submit-prep | чеклист + инструкция `Module-N/Participant/504-MN-HW-Instructions.md` |
| создай профиль участника MS, profile intake | `/profile-intake` | ms-participant-profile | `ms-profile.md v1` (сквозной профиль) |
| обнови профиль (после модуля), profile refresh | `/profile-refresh` | ms-participant-profile | `ms-profile.md vN+1` + запись в daily |
| mid-course diagnostic, checkpoint середины | `/mid-course-diagnostic` | ms-participant-profile | отчёт + решение Continue/Adjust/Pivot |
| синтез профиля после курса, profile synthesis | `/profile-synthesis` | ms-participant-profile | отчёт-синтез + финальный `ms-profile` + опц. рекомендации |

**Опционально (не в минимальном MANIFEST):** навык **participant-learning-profile** — «учебный профиль», «learner profile»; отдельной команды нет, читать `.cursor/skills/participant-learning-profile/SKILL.md`.

Полный состав навыков для копирования в другие среды: [[Student-AI-Pack/MANIFEST|MANIFEST]].

## Что не коммитить

- `my-profile.md`, `goals-504.md`, `*.local.md` — личные данные и цели участника.
- `My-Notes/*.md` — личные конспекты (исключения: `README.md` и `TEMPLATE-WN-summary.md`).
- `2026/` — включая daily-notes (`YYYY/01-Daily/YYYY-MM-DD.md`), ПЗ, операционные артефакты.
- `.claude/session-handoff.md`, `.claude/settings.local.json` — локальные служебные файлы.
- `.env`, `.mcp.env`, `.obsidian/` — секреты и локальные настройки Obsidian.

Полный список — в `.gitignore`. Не предлагать студенту коммитить эти файлы.

## Правила

- **Режимы Plan / Agent.** Plan: предлагать структуру и шаги без правок; Agent: править файлы после подтверждения или по явной команде. (`.cursor/rules/ai-behavior.md` — time-boxing, один шаг за ответ где уместно)
- **Без псевдографики.** Никаких box-drawing символов (`┌─┐│└┘`), ASCII-деревьев, текстовых «схем». Структура — через markdown-таблицы и списки. Блоки кода и Excalidraw — исключения. (`.cursor/rules/no-pseudographics.md`)
- **Новые схемы — Excalidraw** (`.excalidraw.md`), не Mermaid. Существующие Mermaid-блоки не трогать, новых не добавлять.
- **Statusline активного навыка.** При активном Skill **каждый ответ** начинается со строки `🔧 Активный навык: <SkillId> <Название> · Шаг N/M`. При завершении: `✅ Навык <SkillId> завершён`. (`.cursor/rules/ai-behavior.md`)
