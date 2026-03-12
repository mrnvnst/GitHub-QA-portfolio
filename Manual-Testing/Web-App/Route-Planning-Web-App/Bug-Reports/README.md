### Баг-репорты

🇷🇺 | RU

В данном разделе представлены баг-репорты, заведённые в ходе ручного тестирования веб-приложения.

Баг-репорты отражают найденные дефекты пользовательского интерфейса, логики работы приложения и бизнес-сценариев.

| ID     | Название                                                                                                  | Серьёзность | Статус | Ссылка                                                                 |
| ------ | --------------------------------------------------------------------------------------------------------- | ----------- | ------ | ---------------------------------------------------------------------- |
| БР-001 | Система не проставляет пробелы автоматически при заполнении поля «Номер карты» валидными данными          | Стандартный       | Открыт   | [Просмотр](bugs/BR-001-card-number-wrong-formatting.md)                      |
| БР-002 | В окне «Способ оплаты» не отображаются последние 4 цифры добавленной карты                                | Критический    | Открыт   | [Просмотр](bugs/BR-002-card-last-digits-not-displayed.md)              |
| БР-003 | Система позволяет вводить невалидные символы в поле «Номер карты»                                         | Критический    | Открыт   | [Просмотр](bugs/BR-003-invalid-characters-card-number-allowed.md)              |
| БР-004 | Система позволяет вводить невалидные символы в поле «Код»                                                 | Критический    | Открыт   | [Просмотр](bugs/BR-004-invalid-characters-code-field.md)               |
| БР-005 | Текст надписи в описании каршеринга не соответствует макету                                               | Стандартный       | Открыт   | [Просмотр](bugs/BR-005-carsharing-text-mismatch.md)                    |
| БР-006 | Нажатие на кнопку «Отменить» в окне «Машина забронирована» не открывает окно подтверждения отмены поездки макету                                               | Блокирующий       | Открыт   | [Просмотр](bugs/BR-006-cancel-booking-no-confirmation.md)                    |
| БР-007 | Иконки машин на карте отображаются за пределами автодорог | Критический     | Открыт   | [Просмотр](bugs/BR-007-car-icons-off-roads.md)              |
| БР-008 | На карте отображаются машины только выбранного тарифа | Критический | Открыт | [Просмотр](bugs/BR-008-map-shows-only-selected-tariff.md) |
| БР-009 | Автоматически выбранная машина не выделяется на карте | Критический | Открыт | [Просмотр](bugs/BR-009-selected-car-not-highlighted.md) |
| БР-010 | При удалении адресов форма бронирования становится недоступна | Блокирующий | Открыт | [Просмотр](bugs/BR-010-booking-form-disabled-after-address-removal.md) |
| БР-011 | Бронирование выполняется без выбора способа оплаты | Критический | Открыт | [Просмотр](bugs/BR-011-booking-without-payment.md) |

#### Структура баг-репортов

Каждый баг-репорт содержит:
- название;
- серьёзность, приоритет и статус;
- предусловия и шаги воспроизведения;
- ожидаемый и фактический результат;
- информацию об окружении;
- вложения (скриншоты).

--- 

🇬🇧 | EN

This section contains bug reports created during manual testing of a web application.

The reports cover UI issues, application logic defects, and business flow violations.

| ID     | Title                                                                                 | Severity | Status | Link                                                               |
| ------ | ------------------------------------------------------------------------------------- | -------- | ------ | ------------------------------------------------------------------ |
| BR-001 | The system does not automatically insert spaces in the card number field              | Minor    | Open   | [View](bugs/BR-001-card-number-wrong-formatting.md)                      |
| BR-002 | The last four digits of the added card are not displayed in the payment method window | Critical | Open   | [View](bugs/BR-002-card-last-digits-not-displayed.md)              |
| BR-003 | The system allows entering invalid characters in the card number field                | Critical | Open   | [View](bugs/BR-003-invalid-characters-card-number-allowed.md)              |
| BR-004 | The system allows entering invalid characters in the code field                       | Critical | Open   | [View](bugs/BR-004-invalid-characters-code-field.md)               |
| BR-005 | The car sharing description text does not match the mockup                            | Minor    | Open   | [View](bugs/BR-005-carsharing-text-mismatch.md)                    |
| BR-006 | Clicking the “Cancel” button does not open the trip cancellation confirmation dialog  | Blocker  | Open   | [View](bugs/BR-006-cancel-booking-no-confirmation.md)              |
| BR-007 | Car icons are displayed outside the road network                                      | Critical | Open   | [View](bugs/BR-007-car-icons-off-roads.md)                         |
| BR-008 | The map displays only cars of the selected tariff                          | Critical | Open   | [View](bugs/BR-008-map-shows-only-selected-tariff.md)  |
| BR-009 | The automatically selected car is not highlighted on the map                          | Critical | Open   | [View](bugs/BR-009-selected-car-not-highlighted.md)                |
| BR-010 | The booking form becomes unavailable after removing addresses                         | Blocker  | Open   | [View](bugs/BR-010-booking-form-disabled-after-address-removal.md) |
| BR-011 | Booking is allowed without selecting a payment method                                 | Critical | Open   | [View](bugs/BR-011-booking-without-payment.md)                     |

#### Bug Report Structure

Each bug report includes:

- title;
- severity, priority, and status;
- preconditions and steps to reproduce;
- expected and actual results;
- environment details;
- attachments (screenshots).