---
ProjectId: 504
Type: notebooklm-checklist
Module: 4
CDate: 2026-04-17
MDate: 2026-04-18
---

# Upload Checklist — 504 M4

## Перед загрузкой

- [ ] Открыть `Source-Manifest-M4.md`
- [ ] Подготовлены 8 основных source-файлов
- [ ] Проверено отсутствие материалов M1-M2 (M3 концепции включены в Source-Concepts-M4)

## Источники для загрузки в NLM

> **Правило:** файлы нумеруются `[N]` для однозначного порядка загрузки. Сначала источники (S), потом промпты (P). Нумерация фиксируется в манифесте.

| # | Файл | Статус | Назначение |
|---|------|--------|------------|
| S1 | `Source-Concepts-M4.md` (21 карточка) | ☐ | Концепции M3+M4+Менторинг |
| S2 | `Skills-of-Module-M4.md` | ☐ | Навыки S4.00-S4.04 (обзор + промпты) |
| S3 | `Lesson-Core-M4.md` | ☐ | План сессий, блоки, карточки |
| S4 | `504-M4-Prep-Flipped-PreClass-Participants.md` | ☐ | PreClass v1 (6 тем + тёмная триада) |
| S5 | `504-M4-Review-Session-RunOfShow.md` | ☐ | RoS Review пн 21.04 |
| S6 | `504-M4-Workshop-RunOfShow.md` | ☐ | RoS Workshop вт 22.04 |
| P1 | `Prompt-Pack-Audio-Overview-M4.md` | ☐ | Промпты Audio Overview |
| P2 | `Prompt-Pack-M4.md` | ☐ | Все промпты (Concept Cards, Quiz, Flashcards, Slide Deck) |

### Навыки (загружать для полного контекста)

| # | Файл | SkillId | Статус |
|---|------|---------|--------|
| S7 | `504-M4-AI-Skill-Team-Development-Strategy-Orchestrator.md` | S4.00 | ☐ |
| S8 | `504-M4-AI-Skill-Retrospective-Reflection.md` | S4.01 | ☐ |
| S9 | `504-M4-AI-Skill-Practice-Based-Learning.md` | S4.02 | ☐ |
| S10 | `504-M4-AI-Skill-Team-Adaptability.md` | S4.03 | ☐ |
| S11 | `504-M4-AI-Skill-Feedback-Culture.md` | S4.04 | ☐ |

## Порядок генерации

| # | Материал | Промпт-источник | Статус |
|---|----------|------------------|--------|
| G1 | **Concept Cards** (25 карточек) | P2 § Карточки концепций | ☐ |
| G2 | **Slide Deck 1: Review** (8 слайдов) | `NLM-Ready-Prompts-M4.md` § Slide Deck 1 | ☐ |
| G3 | **Slide Deck 2: Workshop** (14 слайдов) | `NLM-Ready-Prompts-M4.md` § Slide Deck 2 | ☐ |
| G4 | **Audio Overview** (обзор теории, 10-12 мин) | P1 Промпт 1 | ☐ |
| G5 | **Audio Overview** (подготовка к защите, 5-7 мин) | P1 Промпт 2 | ☐ |
| G6 | **Study Guide** (до Review) | P2 § Учебное руководство | ☐ |
| G7 | **Квиз** (входной, 5 вопросов) | P2 § Квиз | ☐ |
| G8 | **Флеш-карточки** (15 шт) | P2 § Флеш-карточки | ☐ |

## NLM Slide Review (10 проверок)

- [ ] Покрытие моделей (все 21 концепция в слайдах?)
- [ ] Глубина ключевого концепта (Экологичное мышление — 2+ слайда?)
- [ ] Сквозные метафоры (экзоскелет, два волка, диод)
- [ ] Баланс моделей (ни одна не перетягивает)
- [ ] Антипаттерны названы корректно
- [ ] Практический промпт есть (S4.00 оркестратор)
- [ ] Callback W3 (6 моделей в Review)
- [ ] Cliffhanger (528 Vibe Leadership preview)
- [ ] Формат воркшопа (breakout инструкции на слайдах)
- [ ] Терминологическая точность

## После Workshop (вт 22.04)

- [ ] Post-Workshop Study Guide
- [ ] Post-session Quiz (Google Form)
- [ ] Проверка фактов всех материалов M4

## Перед защитой

- [ ] Pre-Defense Guide (учебное руководство к защите)
- [ ] Шаблон презентации защиты (5-7 слайдов)
- [ ] Обновлён `504-Delivery-Log`

## Публикация

- [ ] Экспорт в GDrive: PreClass, HW, навыки, конспект W3
- [ ] Финальные NLM материалы в Deliverables
- [ ] Git push репозитория участников
