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

## Служебные файлы пакета (этот каталог)

| Файл | Путь в каноне |
|------|----------------|
| README | `MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Student-AI-Pack/README.md` |
| INSTALL | `…/Student-AI-Pack/INSTALL.md` |
| MANIFEST | `…/Student-AI-Pack/MANIFEST.md` |
| Шаблоны | `…/Student-AI-Pack/templates/*.md` |

## Материалы участника по модулям

Копировать содержимое **`Module-N/Participant/`** (публичное). На релизе v1 минимум **M1**; по мере готовности — M2–M4.

| Модуль | Путь в каноне |
|--------|----------------|
| M1 | `MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Module-1/Participant/` |
| M2 | `…/Module-2/Participant/` |
| M3 | `…/Module-3/Participant/` |
| M4 | `…/Module-4/Participant/` |

Опционально для NotebookLM: `Module-N/NotebookLM/*.md` (без приватных заметок).

## Навыки курса по модулям

Навыки находятся в `Module-N/Participant/` и копируются вместе с материалами участника.

| Модуль | SkillId | Файл | Назначение |
|--------|---------|------|------------|
| M1 | S1.01 | `504-M1-AI-Mentor-Communication.md` | Обратная связь и коммуникация |
| M1 | S1.05 | `504-M1-AI-Skill-Situational-Leadership.md` | Ситуационное лидерство |
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
| M4 | S4.00-S4.04 | `504-M4-AI-Skill-*.md` | В работе |

## Вход EQ для участника (страница-объяснение)

| Файл | Путь |
|------|------|
| EQ — вход | `MS-Courses/25-CM-MDPG/504-CM-AI-Empowered-Team/Module-1/Participant/EQ-504-Entry.md` |

## Не включать в студенческий дистрибутив

- `Module-N/Facilitator/Private/`
- `Module-N/Facilitator/` (кроме явного решения курса о публичном фасилитации — по умолчанию **не включать**)
- `2026/504/*` (операционный контур)
- `.env`, `.mcp.json`, секреты

## Связанные документы

- [[MS-Courses/Course-Design/Course-Student-AI-Pack-Guide|Course-Student-AI-Pack-Guide]]
- [[MS-Courses/Course-Design/Course-Package-Policy|Course-Package-Policy]]
