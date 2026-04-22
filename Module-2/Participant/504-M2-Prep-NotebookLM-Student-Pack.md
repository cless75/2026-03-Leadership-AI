---
ProjectId: 504
Type: prep
Module: 2
tags:
  - 'notebooklm'
  - 'student-pack'
  - 'module-2'
CDate: 2026-04-09T00:00:00.000Z
gd_sync: true
---

# Student Pack — NotebookLM модуль 2: Процессы и сотрудничество

**Мастерская:** AI Empowered Team (504)
**Неделя:** 2 — Процессы и сотрудничество (Хоукинз #3)
**Lesson-Core:** [[MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Module-2/NotebookLM/Lesson-Core-M2|Lesson-Core M2]]

---

## 1. Источники для загрузки в NotebookLM

> **Правило:** не больше **8–9** источников в одном ноутбуке; нарративные файлы загружать **первыми** (Best Practices §2, манифест v3).
> **Полный локальный пакет M2:** [[MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Module-2/NotebookLM/README|Module-2/NotebookLM/README]]
> **Порядок и приоритеты:** [[MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Module-2/NotebookLM/Source-Manifest-M2|Source-Manifest-M2]]

| # | Источник | Тип | Назначение | Как загрузить |
|---|----------|-----|------------|---------------|
| 1 | **PreClass M2** (`504-M2-Prep-Flipped-PreClass-Participants`) | Нарратив | Преридинг, модели, 4 вопроса, самодиагностика 0–4 | Уже в Google Doc: `1d8oYeCqME6dK--eVKdlqXnxEIvnM4Xq4IM5rGbaedZ0` → импорт URL в NLM |
| 2 | **Script Three Layers AI** (`Source-Script-Three-Layers-AI-M2` в `Module-2/NotebookLM/`) | Нарратив | D/U/N, экзоскелет, демо AI-Диагноста, промпт | Загрузить `.md` или экспорт в GDoc (`gd:export`) |
| 3 | **S09 Value Chain** (`Source-S09-Value-Chain-M2`) | Нарратив | Цепочка ценности, 6 шагов, связь с ДЗ v2 | Загрузить `.md` из `Module-2/NotebookLM/`; альтернатива — GDoc скилла S09: `1xNhSfZBgX-ThuLskqF0_gCENDenxGqqhspEacd7DlBE` (не дублировать оба) |
| 4 | **Tuckman-Model** (канон) | Справочный | Фазы, переходы, признаки | Экспорт канона в GDoc → NLM |
| 5 | **Ideal-Team-Player** (канон) | Справочный | Скромность (Humble) / Мотивация (Hungry) / Эмоц. интеллект (Smart), антипаттерны | Экспорт в GDoc |
| 6 | **Organizational-Rhythm** (канон) | Справочный | Ритм как функция лидера, Run/Growth | Экспорт в GDoc |
| 7 | **Hawkins-Team-Competencies** (канон) | Справочный | Компетенция #3, маппинг недель | Экспорт в GDoc |

**Опционально (1 слот, если укладываетесь в лимит):**

| # | Источник | Когда |
|---|----------|--------|
| 8 | **Smart-Communication-Lencioni** (канон) | Связка M1→W3, акцент на Эмоц. интеллект (Smart) |
| 9 | **Lesson-Core-M2** | Тайминг блоков и карточки для Slide Deck / сверки |
| 10 | **Skills-of-Week-M2** | Промпты и структура S05–S08 + S09 |

**Не включать (шум):**

- полный канон **Situational-Leadership-Blanchard** (D1–D4 уже в PreClass / S09; полная карточка перетягивает NLM);
- **Run-of-Show**, **Mentor Brief** — операционка ведущего / приватное;
- длинные презентации и дубликаты одной темы в двух GDoc.

---

## 2. Prompt Pack для NotebookLM

Ниже — запросы для копирования в NotebookLM Studio. **Полные** промпты Slide Deck (части 1–2), пост-аудио, пост-квиз, NLM Slide Review и практический чеклист дублируются в [[MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Module-2/NotebookLM/Prompt-Pack-M2|Prompt-Pack-M2]] (v3).

Порядок: Study Guide → (опционально входной Quiz) → после воркшопа Post Guide / Post Quiz → Audio / Slides / Fact-check.

### 2.1 Study Guide (до воркшопа)

```text
Создай Study Guide для подготовки к воркшопу "504 M2: Процессы и сотрудничество".

Контекст:
- аудитория: руководители, продакты, тимлиды;
- формат: 120 минут, 2 breakout по 25 минут, парная работа с AI;
- цель: диагностика фазы команды по Такману + один эксперимент с процессами.

Структура:
1) 4 ключевые идеи: Такман (Storming необходим), Ideal Team Player (Skillful Politician), три роли AI (Диагност / Усилитель / Наставник), ритм как функция лидера;
2) как PreClass (4 вопроса) переходит в breakout;
3) чеклист "что взять с собой";
4) 5 вопросов самопроверки перед сессией.

Максимум 2 страницы. Практичный стиль, буллеты.
```

### 2.2 Study Guide (после воркшопа)

```text
Создай Post-Workshop Study Guide для "504 M2: Процессы и сотрудничество".

Участники уже прошли два breakout, работали с AI-аналитиком, определили фазу и точку эксперимента.

Сделай:
1) 5 вопросов рефлексии;
2) чеклист "что сделать на этой неделе" (связка с ДЗ v2: сначала карта цепочки S09, затем один точечный рычаг S05–S08);
3) три маркера "экзоскелет, не коляска";
4) превью W3: донесение до руководства.

Формат: 1 страница, можно распечатать.
```

### 2.3 Quiz (входной, 5 вопросов)

```text
Сгенерируй входной Quiz из 5 вопросов (multiple choice, 4 варианта) по теме "504 M2: Процессы и сотрудничество".

Каждый вопрос проверяет применение:
1) фаза Такмана по короткому описанию команды;
2) Ideal Team Player и связь со Storming (Humble / Hungry / Smart);
3) выбор роли AI (Диагност / Усилитель / Наставник) на кейсе процесса;
4) ритм как функция лидера vs отдельная "роль хранителя процессов";
5) экзоскелет vs коляска для AI-диагностики процессов.

Для каждого вопроса: правильный ответ; 1–2 предложения объяснения; типичная ошибка мышления.
```

### 2.4 Quiz (пост-сессия, 5 вопросов)

> **Канон для когорты:** публикация через **Google Form** (скрипт `Quiz-Scripts/504-M2-Post-Quiz-CreateForm.gs`). Промпт ниже — для черновика в NLM или сверки формулировок. Полный текст: [[MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Module-2/NotebookLM/Prompt-Pack-M2|Prompt-Pack-M2]] § 7.

```text
Сгенерируй post-session Quiz из 5 вопросов (multiple choice, 4 варианта) по теме "504 M2: Процессы и сотрудничество + value chain".

Темы (по одному вопросу): Такман / Storming; три слоя AI; экзоскелет vs коляска; ДЗ v2 (S09 + точечный S05–S08); когда уместен S09 vs ситуация без процесса.

Язык: русский. В конце — таблица правильных ответов.
```

### 2.5 Flashcards (15 карточек)

```text
Создай 15 flashcards (вопрос-ответ) по теме "504 M2: Процессы и сотрудничество".

Покрой:
- 5 фаз Такмана и тезис "Storming необходим";
- Ideal Team Player и три антипаттерна (фокус на Skillful Politician);
- организационный ритм и антипаттерн "SM как должность";
- три роли AI (D/U/N) и экзоскелет vs коляска;
- Бланшар D1–D4 в контексте делегирования;
- Smart Communication (Smart = EQ);
- S09 / value chain: зачем карта перед точечным экспериментом;
- компетенция Хоукинза #3 и парадокс AI в Run.

Формат: вопрос конкретный; ответ 1–3 предложения; одна строка "как заметить в работе".
```

### 2.6 Audio Overview (пре / пост)

Полные сценарии (7 мин пре, 10 мин пост): [[MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Module-2/NotebookLM/Prompt-Pack-M2|Prompt-Pack-M2]] § 3–4.

### 2.7 Slide Deck (две части)

Полные промпты (часть 1 — 12 слайдов, часть 2 — 10 слайдов): [[MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Module-2/NotebookLM/Prompt-Pack-M2|Prompt-Pack-M2]] § 1–2. После генерации — **NLM Slide Review** (11 проверок в том же файле).

### 2.8 FAQ для участников (10 вопросов)

```text
Сгенерируй FAQ (10 вопросов и ответов) для участников модуля 2 (504).

Покрой:
- не успел PreClass / нет своей команды (кейс TechVision);
- боюсь, что AI "подменит" моё judgment в диагностике;
- команда в "идеальном Norming" — как проверить на ложный Norming;
- одна встреча точно ритуал — как поднять тему;
- делегирование и сопротивление;
- чем S09 отличается от "просто спросить AI про команду";
- конфликт с коллегой vs процессная диагностика.

Формат: вопрос; ответ 3–5 строк; "что сделать сейчас" (1 действие).
```

### 2.9 Fact-check (контроль качества)

```text
Проведи факт-проверку материалов по M2 (Study Guide, Quiz, Flashcards, FAQ, Slides, Audio).

Проверь:
1) нет противоречий между выходами;
2) Такман — 5 фаз; Ленсиони — Humble/Hungry/Smart; Бланшар — D×S; Хоукинз #3 = процессы;
3) D/U/N — параллельные функции, не этапы;
4) "Экзоскелет" — метафора MS, корректно объяснена;
5) нет утверждений вне загруженных источников.

Вывод: таблица исправлений с приоритетом critical / medium / low.
```

---

## Связанные документы

- [[MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Module-2/NotebookLM/Lesson-Core-M2|Lesson-Core M2]]
- [[MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Module-2/Participant/504-M2-Prep-Flipped-PreClass-Participants|PreClass для участников]]
- [[MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Module-2/NotebookLM/Prompt-Pack-M2|Prompt-Pack M2]]
- [[MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Module-2/NotebookLM/Upload-Checklist-M2|Upload Checklist M2]]
- [[MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Operations/504-g-Workshop-Prep-Process|Процесс подготовки воркшопа (§5 NotebookLM)]]
- [[MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Quiz-Scripts/README-504-Quiz-Scripts|README Quiz-Scripts 504]]

---

**Версия пакета участника:** v1 (2026-04-09). Согласовано с NotebookLM package **v3** (`Module-2/NotebookLM/README`).
