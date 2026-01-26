### Баг-репорты

🇷🇺 | **RU** 

Баг-репорты оформлены в формате Markdown для удобного просмотра и навигации и содержат:
- название дефекта;
- шаги воспроизведения;
- ожидаемый и фактический результат;
- приоритет и серьёзность;
- окружение;
- ссылки на скриншоты.

Дефекты были обнаружены в ходе выполнения проверок из следующих чек-листов:
- [Функциональный чек-лист](../Checklists/functional-checklist-ru.csv)
- [Регрессионный чек-лист](../Checklists/regression-checklist-ru.csv)

Подробные описания дефектов расположены в директории `bugs/`.
Скриншоты дефектов размещены в директории `attachments/.`

#### Список багов

| ID | Название | Серьезность | Статус | Ссылка |
|------|-------------|----------|--------|------|
| BUG-001 | При изменении ориентации устройства с портретной на альбомную приложение завершает работу | Блокирующий | Открыт | [Просмотр](bugs/BUG-001-app-crash-orientation-change.md) |
| BUG-002 | В карточке станции, открытой лонг-тапом, отсутствуют кнопки "Отсюда" и "Сюда" | Стандартный | Открыт | [Просмотр](bugs/BUG-002-missing-buttons-station-card-long-tap.md) |
| BUG-003 | При отсутствии интернет-соединения не появляется уведомление об ошибке | Стандартный | Открыт | [Просмотр](bugs/BUG-003-no-network-error-notification.md) |
| BUG-004 | После обновления приложение не сохраняет настройки языка | Стандартный | Открыт | [Просмотр](bugs/BUG-004-language-settings-not-saved-update.md) |
| BUG-005 | После обновления приложение не сохраняет историю маршрутов | Стандартный | Открыт | [Просмотр](bugs/BUG-005-route-history-not-saved-update.md) |
| BUG-006 | При выборе английского языка в настройках язык приложения не меняется на английский | Критический | Открыт | [Просмотр](bugs/BUG-006-language-not-switched-to-english.md) |
| BUG-007 | При выборе режима "Автоматический" тема приложения не меняется автоматически на темную в 18:00 по Мск | Критический | Открыт | [Просмотр](bugs/BUG-007-theme-not-switched-automatic-mode.md) |
| BUG-008 | При нажатии на кнопку "Обратная связь" с помощью Webview открывается приложение почтового сервиса | Критический | Открыт | [Просмотр](bugs/BUG-008-feedback-opens-email-app.md) |

---

### Bug reports

🇬🇧 | **EN** 

Bug reports are in Markdown format for easy viewing and navigation and contain::
- clear and concise title;
- steps to reproduce;
- expected and actual results;
- severity and priority;
- test environment;
- links to related screenshots.

Defects were identified during execution of test cases from the following checklists:
- [Functional checklist](../Checklists/functional-checklist-en.csv)
- [Regression checklist](../Checklists/regression-checklist-en.csv)

Detailed bug reports are strored in the `bugs/` directory.
Screenshots are stored in the `attachments/` directory.

#### Bug list

| ID | Title | Severity | Status | Link |
|------|-------------|----------|--------|------|
| BUG-001 | Application crashes when switching device orientation from portrait to landscape | Blocker | Open | [View](bugs/BUG-001-app-crash-orientation-change.md) |
| BUG-002 | “From here” and “To here” buttons are missing in the station card opened by long tap | Major | Open | [View](bugs/BUG-002-missing-buttons-station-card-long-tap.md) |
| BUG-003 | No error notification is displayed when there is no internet connection | Major | Open | [View](bugs/BUG-003-no-network-error-notification.md) |
| BUG-004 | Application does not save language settings after update | Major | Open | [View](bugs/BUG-004-language-settings-not-saved-update.md) |
| BUG-005 | Application does not save route history after update | Major | Open | [View](bugs/BUG-005-route-history-not-saved-update.md) |
| BUG-006 | Application language does not switch to English when English is selected | Critical | Open | [View](bugs/BUG-006-language-not-switched-to-english.md) |
| BUG-007 | Application theme does not switch to dark automatically at 18:00 MSK in Automatic mode | Critical | Open | [View](bugs/BUG-007-theme-not-switched-automatic-mode.md) |
| BUG-008 | Email application opens instead of feedback screen in WebView | Critical | Open | [View](bugs/BUG-008-feedback-opens-email-app.md) |