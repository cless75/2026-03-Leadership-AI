# Команда: profile-intake

Запусти **Initial Intake** сквозного профиля участника Мастерской (`ms-profile.md`) по навыку **ms-participant-profile** — режим 1 (старт программы).

## Входные данные

Контекст / пожелания: $ARGUMENTS

Если не указано — начни с проверки существующего профиля (grep по `MS_PROFILE_PATH`, legacy `my-profile.md`) и предложи дальнейший путь: миграция, Quick Refresh или новый Initial Intake.

## Методология

**Канон навыка:** [.cursor/skills/ms-participant-profile/SKILL.md](../../.cursor/skills/ms-participant-profile/SKILL.md), режим 1.
**Схема файла:** [.cursor/skills/ms-participant-profile/schema.md](../../.cursor/skills/ms-participant-profile/schema.md)
**Шаблон:** [.cursor/skills/ms-participant-profile/templates/ms-profile.template.md](../../.cursor/skills/ms-participant-profile/templates/ms-profile.template.md)

## Порядок выполнения

1. Прочитай SKILL.md (режим 1) и schema.md.
2. Проверь существующий профиль. Если есть — не перезаписывай, предложи refresh.
3. Запроси у участника место хранения (локальный vault / gd-sync / другое) и сохрани путь в `.claude/settings.local.json` → `MS_PROFILE_PATH`.
4. Опроси 10 измерений по одному блоку за шаг (см. reference.md).
5. Создай `ms-profile.md v1` по шаблону.
6. Добавь ссылку в daily-note текущего дня.

## Итог

Файл `ms-profile.md v1` создан, путь сохранён, в daily — cross-link. Подтверждение участнику — одной фразой.
