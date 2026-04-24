# Команда: profile-synthesis

Проведи **Full Synthesis** профиля участника в конце программы по навыку **ms-participant-profile** — режим 4. Занимает 1.5–2 часа с AI + сутки паузы + 30 мин финализации.

## Входные данные

Контекст (какую программу закрываем, нужны ли рекомендации): $ARGUMENTS

## Методология

**Канон:** [.cursor/skills/ms-participant-profile/SKILL.md](../../.cursor/skills/ms-participant-profile/SKILL.md), режим 4.
**Шаблон отчёта-синтеза:** [.cursor/skills/ms-participant-profile/templates/profile-synthesis-report.template.md](../../.cursor/skills/ms-participant-profile/templates/profile-synthesis-report.template.md)
**Шаблон рекомендаций:** [.cursor/skills/ms-participant-profile/templates/personal-recommendations.template.md](../../.cursor/skills/ms-participant-profile/templates/personal-recommendations.template.md)

## Порядок выполнения

1. **Сбор всех входов:** glob по `MS_PROFILE_PATH` и рабочей директории — `ms-profile.md`, `ms-profile.history/*`, `goals-*.md`, `*-HW-Protocol.md`, `*-EQ-diagnosis.md`, daily-notes за период программы, `open-questions.md`, `mid-course-diagnostic-*.md`.
2. **Проверка полноты.** Чеклист входов; предупреждение если >30% отсутствует.
3. **Реверс-инжиниринг по 10 измерениям** — для каждого цитата из файла + имя файла + строка.
4. **Дельты от v1 / от последнего mid-course.** Три категории: Подтверждение / Смещение / Новый слой.
5. **Контр-диагностика (обязательно)** — для каждого вывода-диагноза.
6. **Слепые зоны** — три точки по сигналам избегания.
7. **Рекомендации** (опционально, по запросу участника) — по шаблону.
8. **Запись:** `ms-profile.md vN+1`, `profile-synthesis-YYYY-MM-DD.md`, опц. `personal-recommendations-YYYY-MM-DD.md`.
9. **Сутки паузы** — не редактировать профиль в тот же день.

## Итог

Полный синтез программы; участник на следующий день перечитывает, финализирует v{N+1}.

## Важно

- **Цитаты обязательны** — без источников это фантазия AI.
- **Privacy guard** — имена третьих лиц в отчётах заменены ролями.
- **Не ставить диагнозов** — только операционные паттерны.
