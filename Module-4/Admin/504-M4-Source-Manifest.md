---
ProjectId: 504
Type: notebooklm-source-manifest
Module: 4
CDate: 2026-04-17
MDate: 2026-04-18
---

# Source Manifest — 504 M4

## Основные источники (загружать обязательно)

> Нумерация: `S` = source (загрузить в NLM), `P` = prompt (использовать для генерации).

| # | Файл | Назначение |
|---|------|------------|
| **S1** | **`Source-Concepts-M4.md`** (СВОДНЫЙ) | **Все концепции M3+M4+Менторинг:** 21 карточка |
| **S2** | `Skills-of-Module-M4.md` | Навыки S4.00-S4.04 (обзор + промпты) |
| **S3** | `Lesson-Core-M4.md` | План сессий, блоки, карточки |
| **S4** | `504-M4-Prep-Flipped-PreClass-Participants.md` | PreClass v1 (6 тем + тёмная триада) |
| **S5** | `504-M4-Review-Session-RunOfShow.md` | RoS Review пн 21.04 |
| **S6** | `504-M4-Workshop-RunOfShow.md` | RoS Workshop вт 22.04 |
| **P1** | `Prompt-Pack-Audio-Overview-M4.md` | Промпты Audio Overview |
| **P2** | `Prompt-Pack-M4.md` | Concept Cards + Quiz + Flashcards + Slide Deck |
| **P3** | `NLM-Ready-Prompts-M4.md` | Slide Deck промпты (Review + Workshop) |
| — | `Upload-Checklist-M4.md` | Операционный контроль (не загружать) |

> **v2 (2026-04-18):** добавлены Concept Cards промпт (генерация карточек всех концепций для теории), Slide Deck промпты Review/Workshop (привязаны к актуальному RoS v1). Обновлён протокол 504-g-Workshop-Prep-Process: правило генерации карточек концепций.
>
> **v1 (2026-04-17):** создание пакета M4. Source-Concepts-M4 включает концепции M3 + M4 + Mentoring (21 карточка).

## Дополнительные источники (для Slide Deck)

| # | Файл | Когда подключать |
|---|------|------------------|
| 8 | `504-M4-Prep-Flipped-PreClass-Participants.md` | Slide Deck 1 (Review) + Slide Deck 2 (Workshop) |
| 9 | `504-M4-Review-Session-RunOfShow.md` | Slide Deck 1 (Review) |
| 10 | `504-M4-Workshop-RunOfShow.md` | Slide Deck 2 (Workshop) |
| 11 | `Source-Defense-Concepts-Pack.md` (ранее `504-NLM-Full-Concepts-Pack`, `Defense/NotebookLM/`) | Полный контекст (48 концепций курса) |

## Навыки M4 (загружать для Concept Cards и Slide Deck)

| # | Файл | SkillId | Статус |
|---|------|---------|--------|
| 12 | `504-M4-AI-Skill-Team-Development-Strategy-Orchestrator.md` | S4.00 | v1 |
| 13 | `504-M4-AI-Skill-Retrospective-Reflection.md` | S4.01 | v1 |
| 14 | `504-M4-AI-Skill-Practice-Based-Learning.md` | S4.02 | v1 |
| 15 | `504-M4-AI-Skill-Team-Adaptability.md` | S4.03 | v1 |
| 16 | `504-M4-AI-Skill-Feedback-Culture.md` | S4.04 | v1 |

## Ограничения

- Не подключать в этот же ноутбук длинные staging-файлы.
- Не смешивать материалы других модулей (M1-M2) с M4.
- Концепции M3 включены в M4, так как менторинг M4-W3 содержит дополнительные концепции.
- При конфликтах источников приоритет:
  1) `Source-Concepts-M4.md`,
  2) `Lesson-Core-M4.md`,
  3) `Source-Defense-Concepts-Pack.md` (ранее `504-NLM-Full-Concepts-Pack`).

## Порядок генерации

1. **Concept Cards** → проверить 21+ карточку (формат + связи)
2. **Slide Deck 1 (Review)** → NLM Slide Review (10 проверок)
3. **Slide Deck 2 (Workshop)** → NLM Slide Review (10 проверок)
4. **Audio Overview** (2 промпта: теория + подготовка к защите)
5. **Study Guide / Quiz / Flashcards**
6. **Fact-check** всех материалов
