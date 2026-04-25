# MANIFEST — состав студенческого AI-пакета 504

Канон путей относительно корня vault **Master-Strategy2**. При сборке ZIP или Git копируйте в корень релиза указанные деревья.

## Навыки (`.cursor/skills/<id>/`)

Копировать **целиком** каждую папку (все `.md` + `SKILL.md`).

| ID | Источник в vault | Назначение |
|----|------------------|------------|
| `course-goals-intake` | `.cursor/skills/course-goals-intake/` | Опрос целей на курс по шаблону |
| `participant-profile-load` | `.cursor/skills/participant-profile-load/` | Загрузка и нормализация профиля из `.md` |
| `504-hw-submit-prep` | `.cursor/skills/504-hw-submit-prep/` | Подготовка черновика сдачи ДЗ |
| `eq-self-diagnosis` | `.cursor/skills/eq-self-diagnosis/` | Самодиагностика EQ (Гоулман), мини-кейсы |
| `stai-problem-solving` | `.cursor/skills/stai-problem-solving/` | Системное решение проблемы (STAI 514): формулирование → диагностика → решение → реализация |
| `ms-participant-profile` | `.cursor/skills/ms-participant-profile/` | Сквозной профиль участника MS через программы: Intake / Quick Refresh / Mid-Course Diagnostic (обязательный) / Full Synthesis |
| `burnout-self-diagnosis` | `.cursor/skills/burnout-self-diagnosis/` | Самодиагностика выгорания (Maslach + JD-R + физиология): Quick / Full / Re-check, 4 зоны с рекомендациями. Авто-триггер в daily-notes и профиле при маркерах истощения |
| `mentor-handoff` | `.cursor/skills/mentor-handoff/` | Обезличивание материалов участника для передачи ментору / супервизору / терапевту / peer / публикации: auto-mask имён, проверка коммерческой тайны, упаковка в HTML/PDF |
| `render-notes-html` | `.cursor/skills/render-notes-html/` | Dashboard прогресса участника в HTML: timeline сессий, EQ, burnout-зона, активные эксперименты, бейджи приватности. Только для самого участника (Desktop) |

## Служебные файлы пакета (этот каталог)

| Файл | Путь в каноне |
|------|----------------|
| README | `MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Student-AI-Pack/README.md` |
| INSTALL | `…/Student-AI-Pack/INSTALL.md` |
| MANIFEST | `…/Student-AI-Pack/MANIFEST.md` |
| Шаблоны | `…/Student-AI-Pack/templates/*.md` |

## Политика хранения и шаблоны конспектов/логов

| Файл | Путь в каноне |
|------|----------------|
| Privacy & Storage Policy | `MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Storage-Policy/Privacy-and-Storage-Policy.md` |
| Шаблон тех. лога сессии | `…/Storage-Policy/templates/template-session-log.md` |
| Шаблон конспекта сессии | `…/Storage-Policy/templates/template-session-conspect.md` |

## Материалы по модулям

Копировать содержимое **`Module-N/Participant/`**. Для модулей с готовым NLM-пакетом также копировать **`Module-N/NotebookLM/`**.

| Модуль | Participant | NotebookLM |
|--------|-------------|------------|
| M1 | `MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Module-1/Participant/` | `.../Module-1/NotebookLM/` |
| M2 | `.../Module-2/Participant/` | `.../Module-2/NotebookLM/` |
| M3 | `.../Module-3/Participant/` | `.../Module-3/NotebookLM/` |
| M4 | `.../Module-4/Participant/` | `.../Module-4/NotebookLM/` + корневые `Module-4/Source-Manifest-M4.md`, `Module-4/Upload-Checklist-M4.md` |

## Навыки курса по модулям

Навыки находятся в `Module-N/Participant/` и копируются вместе с материалами участника.

| Модуль | SkillId | Файл | Назначение |
|--------|---------|------|------------|
| M1 | S1.01 | `504-M1-AI-Mentor-Communication.md` | Обратная связь и коммуникация |
| M1 | S1.05 | `504-M1-AI-Skill-Situational-Leadership.md` | Ситуационное лидерство |
| **M1** | **S1.06** | **`504-M1-AI-Skill-Boundary-Diagnostic.md`** | **Диагностика внутренних и внешних границ (Terry Cole)** |
| **M1** | **S1.07** | **`504-M1-AI-Skill-Boundary-Communication.md`** | **Коммуникация границ — скрипты под стейкхолдеров** |
| **M1** | **S1.08** | **`504-M1-AI-Skill-HFC-Release.md`** | **Работа с High-Functioning Codependency — 4 практики** |
| M2 | S2.00 | `504-M2-AI-Skill-Value-Chain-Diagnostics.md` | Value Chain (оркестратор) |
| M2 | S2.01 | `504-M2-AI-Skill-Team-Interaction-Design.md` | Дизайн взаимодействия |
| M2 | S2.02 | `504-M2-AI-Skill-Roles-Responsibilities.md` | Роли и ответственность |
| M2 | S2.03 | `504-M2-AI-Skill-Team-Rhythms.md` | Ритмы команды |
| M2 | S2.04 | `504-M2-AI-Skill-Delegation-Coordination.md` | Делегирование |
| **M3** | **S3.00** | **`504-M3-AI-Skill-Stakeholder-Orchestrator.md`** | **Оркестратор стейкхолдеров** |
| **M3** | **S3.01** | **`504-M3-AI-Skill-Stakeholder-Mapping.md`** | **Карта стейкхолдеров** |
| **M3** | **S3.02** | **`504-M3-AI-Skill-Manage-Up.md`** | **Manage Up** |
| **M3** | **S3.03** | **`504-M3-AI-Skill-Negotiation-Alignment.md`** | **Переговоры** |
| **M3** | **S3.04** | **`504-M3-AI-Skill-Conflict-Escalation.md`** | **Конфликт и эскалация** |
| **M3** | **S3.05** | **`504-M3-AI-Skill-Stakeholder-Shadow-Profiling.md`** | **Профилирование тени стейкхолдера** |
| **M3** | **S3.06** | **`504-M3-AI-Skill-Shadow-Communication-Planning.md`** | **Коммуникация с учётом тени** |
| **M3** | **S3.07** | **`504-M3-AI-Skill-Dark-Triad-Communication.md`** | **Работа с тёмной триадой** |
| **M4** | **S4.00** | **`504-M4-AI-Skill-Team-Development-Strategy-Orchestrator.md`** | **Стратегия развития команды** |
| **M4** | **S4.01** | **`504-M4-AI-Skill-Retrospective-Reflection.md`** | **Рефлексия и ретроспектива** |
| **M4** | **S4.02** | **`504-M4-AI-Skill-Practice-Based-Learning.md`** | **Обучение через практику** |
| **M4** | **S4.03** | **`504-M4-AI-Skill-Team-Adaptability.md`** | **Миссия и адаптивность** |
| **M4** | **S4.04** | **`504-M4-AI-Skill-Feedback-Culture.md`** | **Культура обратной связи** |
| **M4** | **M4+** | **`504-M4-AI-Skill-EQ-Diagnosis-Mentor.md`, `504-M4-AI-Skill-Primal-Leadership-Mentor.md`** | **Дополнительные менторы модуля** |

## Вход EQ для участника (страница-объяснение)

| Файл | Путь |
|------|------|
| EQ — вход | `MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Module-1/Participant/EQ-504-Entry.md` |

## Не включать в студенческий дистрибутив

- `Module-N/Facilitator/Private/`
- `Module-N/Facilitator/` (кроме специально вынесенных публичных NLM-артефактов)
- `2026/504/*` (операционный контур)
- `.env`, `.mcp.json`, секреты

## Связанные документы

- [[MS-Courses/Course-Design/Course-Student-AI-Pack-Guide|Course-Student-AI-Pack-Guide]]
- [[MS-Courses/Course-Design/Course-Package-Policy|Course-Package-Policy]]
