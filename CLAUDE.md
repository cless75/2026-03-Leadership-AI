# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

## Overview

Obsidian vault **504-demo** / репозиторий **2026-03-Leadership-AI**: материалы мастерской **504 AI Empowered Team**, русский язык по умолчанию.

- Ежедневные заметки: **`YYYY/01-Daily/YYYY-MM-DD.md`**
- Session-handoff: **`.claude/session-handoff.md`**
- Ссылки на файлы vault — **Obsidian wikilinks** `[[path]]` или `[[path|alias]]`

## Навигация для участника

- [[504-LEARNING-JOURNEY|Учебный процесс и недели]]
- [[504-HOMEWORK-GUIDE|Домашние задания]]
- [[Student-AI-Pack/README|Student-AI-Pack]] · [[Student-AI-Pack/MANIFEST|MANIFEST]]

## Режимы работы (Cursor / Claude Code)

- **Plan / планирование:** не вносить правки в vault без явного согласования черновика; можно предлагать структуру ПЗ и шаги.
- **Agent / исполнение:** правки в файлах после подтверждения пользователя или по явной команде.

Подробнее: `.cursor/rules/ai-behavior.md` (time-boxing, один шаг за ответ где уместно).

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
| подготовь ДЗ 504 | `/504-hw-submit-prep` | 504-hw-submit-prep | чеклист + инструкция `Week-N/…/504-WN-HW-Instructions` |

**Опционально (не в минимальном MANIFEST):** навык **participant-learning-profile** — «учебный профиль», «learner profile»; отдельной команды нет, читать `.cursor/skills/participant-learning-profile/SKILL.md`.

Полный состав навыков для копирования в другие среды: [[Student-AI-Pack/MANIFEST|MANIFEST]].

## Команды Claude Code (кратко)

`/session-close` · `/session-start` · `/session-result` · `/idea-capture` · `/eq-self-diagnosis` · `/micro-decision-514` · `/solve-problem` · `/course-goals-intake` · `/participant-profile-load` · `/504-hw-submit-prep`

## Правила

- `.cursor/rules/ai-behavior.md`
- `.cursor/rules/no-pseudographics.md`
- `.cursor/rules/russian-input-output.mdc`
