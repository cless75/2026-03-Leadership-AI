---
ProjectId: 504
Type: participant-guide
Week: 1
tags: [504, week-1, participant, onboarding, export]
CDate: 2026-04-03
version: v1
---

# Неделя 1 — инструкция для участника (старт и экспорт пакета)

Этот файл — **единая точка входа** в первую неделю после того, как вы получили материалы **архивом**, **клоном GitHub** или копией папки. Дальше открывайте заметки по ссылкам ниже в Obsidian или в Cursor / Claude Code как vault-проект.

## 1. Как получить пакет

| Способ | Действие |
|--------|----------|
| **GitHub** | Репозиторий [cless75/2026-03-Leadership-AI](https://github.com/cless75/2026-03-Leadership-AI): `git clone`, затем откройте **корень клона** в Cursor или Claude Code. Подробно: [[Student-AI-Pack/INSTALL|INSTALL]]. |
| **ZIP** | Распакуйте в папку **без кириллицы** в пути, откройте эту папку как проект (внутри должны быть `.cursor/skills/` и `Student-AI-Pack/`). |

Личные файлы (`my-profile.md`, `goals-504.md`, черновики в `My-Notes/`) **не коммитьте** в публичный Git — см. `.gitignore`.

## 2. Что сделать до воркшопа W1 (порядок)

1. **Установка AI-среды** — [[Student-AI-Pack/INSTALL|INSTALL]] (уже сделано, если проект открыт).
2. **Цели и профиль** (по желанию до или в первую неделю): шаблоны [[Student-AI-Pack/templates/goals-intake|целей]] и [[Student-AI-Pack/templates/participant-profile.template|профиля]]; в чате можно вызвать команды `/course-goals-intake` и `/participant-profile-load`.
3. **PreClass** — [[Week-1/Participant/504-W1-Prep-Flipped-PreClass-Participants|Неделя 1: подготовка к воркшопу]] (15–20 минут до живого занятия).
4. **Карта PreClass → InClass** (по желанию) — [[Week-1/Participant/504-W1-Prep-Flipped-PreToInClass-Map|PreToInClass Map]].
5. **EQ** — [[Week-1/Participant/EQ-504-Entry|Вход в трек EQ]] и навык `eq-self-diagnosis` в `.cursor/skills/` (триггеры: «самодиагностика EQ», «мини-кейс EQ»).
6. **Материалы недели в этом репозитории** (читать по ходу недели):
   - [[Week-1/Participant/504-W1-AI-Mentor-Communication|AI-наставник: коммуникация (локальная заметка)]]
   - [[Week-1/Participant/504-W1-AI-Skill-Situational-Leadership|Ситуационное лидерство (локальная заметка)]]
   - [[Week-1/Participant/504-W1-Mentoring-Goal-Card|Карточка цели недели]]
   - [[Week-1/Participant/504-W1-Prep-NotebookLM-Student-Pack|NotebookLM Student Pack]] (если используете NotebookLM)
7. **Схемы** в той же папке: `504-s-*.excalidraw.md` / `.svg` — для визуального закрепления.

> В исходных Google Doc (ссылки внутри [[Week-1/Participant/504-W1-HW-Instructions|инструкции по ДЗ]] и PreClass) может быть та же логика; **истина для офлайн-работы в этом vault** — файлы в `Week-1/Participant/`.

## 3. Домашнее задание недели 1

- Полная инструкция: [[Week-1/Participant/504-W1-HW-Instructions|Домашнее задание — неделя 1]].
- Общий порядок сдачи и AI-помощь: [[504-HOMEWORK-GUIDE|504-HOMEWORK-GUIDE]].
- Черновик сдачи в Cursor / Claude Code: команда **`/504-hw-submit-prep`** (неделя **1**).

Каналы сдачи (Telegram + полный протокол) — **строго как в файле ДЗ**, не сокращайте без договорённости с ментором.

## 4. Навигация и контекст курса

- Обзор недели: [[Week-1/Week-1-Overview|Week-1-Overview]].
- Весь учебный процесс 504: [[504-LEARNING-JOURNEY|504-LEARNING-JOURNEY]].
- Список навыков и команд: [[Student-AI-Pack/MANIFEST|MANIFEST]] и `CLAUDE.md` в корне репозитория.

## 5. Проверка «всё на месте» (для самопроверки)

В папке `Week-1/Participant/` у вас должны быть доступны как минимум:

- `504-W1-Participant-Start-Guide.md` (этот файл)
- `504-W1-Prep-Flipped-PreClass-Participants.md`
- `504-W1-HW-Instructions.md`
- `EQ-504-Entry.md`
- `504-W1-Mentoring-Goal-Card.md`
- AI-скилл заметки: `504-W1-AI-Mentor-Communication.md`, `504-W1-AI-Skill-Situational-Leadership.md`

Если чего-то нет — обновите клон (`git pull`) или запросите актуальный архив у команды курса.
