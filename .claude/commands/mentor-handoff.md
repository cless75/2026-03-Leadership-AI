# Команда: mentor-handoff

Подготовь **обезличенный пакет** материалов участника для передачи ментору / супервизору / терапевту / профессиональному peer / публикации по навыку **mentor-handoff**.

## Входные данные

Контекст (список файлов, цель, особенности): $ARGUMENTS

Если не указано — начни с вопроса: «Какие файлы / папки обрабатываем? Кому отправляем (5 опций)?».

## Методология

**Канон навыка:** [.cursor/skills/mentor-handoff/SKILL.md](../../.cursor/skills/mentor-handoff/SKILL.md)
**Справочник:** [.cursor/skills/mentor-handoff/reference.md](../../.cursor/skills/mentor-handoff/reference.md)
**Шаблоны:** `.cursor/skills/mentor-handoff/templates/*.md`
**Политика курса:** [Storage-Policy/Privacy-and-Storage-Policy.md](../../Storage-Policy/Privacy-and-Storage-Policy.md)

## Порядок выполнения

1. **Вход и фильтрация.** Получить файлы; **исключить** всё из `My-Notes/Private/` или с `privacy: private` — сообщить участнику.
2. **Цель и уровень обезличивания** (1 из 5: ментор / супервизор / терапевт / peer / публикация).
3. **Auto-сканирование** на 12 категорий чувствительных данных (см. reference).
4. **Mapping и контр-вопросы** — по именам, компаниям, финансам, цитатам, коммерческой тайне. Двойное подтверждение при confirmed-секретах.
5. **Создание пакета** в `My-Notes/handoff-YYYY-MM-DD-{цель}/` + mapping в той же папке (.gitignore).
6. **Упаковка в HTML/PDF** на Desktop (`Desktop/<participant>/handoff-...`) через headless Edge.

## Жёсткие правила

- T4 (Private) — никогда в handoff, даже после mask.
- PII — удаление, не маскирование.
- mapping — не в git.
- Финальный diff-обзор обязателен.
- Никаких «я уверен, всё ок» — каждое решение явно за участника.

## Важно

Этот навык **не передаёт пакет наружу сам** — только готовит его. Финальную отправку (email, чат, Drive) участник делает руками.
