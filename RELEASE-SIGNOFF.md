# Согласование релиза 504-demo (зафиксировано при сборке)

Дата: 2026-04-03

Решения по умолчанию (гейт ключевых вопросов):

- **Week-2/Participant/** — включён в репозиторий вместе с W1.
- **My-Notes/** — добавлен каталог и шаблон `TEMPLATE-WN-summary.md`.
- **Концепты** — в обзорах недель и в этом vault указаны **имена** моделей; полные карточки — у команды курса (вне репозитория).
- **participant-learning-profile** — остаётся в `.cursor/skills` как опциональное расширение (не в минимальном MANIFEST участника).
- **GitHub** — выполнено: `git pull origin main --allow-unrelated-histories` (подтянут `LICENSE` с remote), затем `git push -u origin main` в [2026-03-Leadership-AI](https://github.com/cless75/2026-03-Leadership-AI). Локальный `user.name` / `user.email` заданы только для этого репозитория (`cless75` / noreply GitHub) — при необходимости замените `git config` в `C:\Obs-Vaults\504-demo`.
