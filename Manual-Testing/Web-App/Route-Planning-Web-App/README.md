### Тестирование веб-приложения: приложение для построения городских маршрутов

🇷🇺 | **RU** 

Проект посвящён ручному тестированию веб-приложения после внесённых изменений в пользовательский интерфейс и бизнес-логику бронирования транспорта.

Приложение предоставляет пользователю возможность построения маршрута, выбора тарифа поездки, выбора автомобиля и бронирования через форму с вводом пользовательских и платёжных данных.

Основная цель тестирования – проверить корректность работы пользовательских сценариев бронирования, стабильность работы интерфейса и корректность обработки пользовательских данных.

В репозитории представлен сокращённый демонстрационный вариант тестовой документации, отражающий подход к тестированию, структуру артефактов и формат оформления дефектов.

#### Тестовые артефакты

##### Чек-листы

- [чек-лист проверки вёрстки интерфейса](Checklists/layout-checklist-form-map-ru.csv)
- [чек-лист проверки логики работы окон и форм оплаты.](Checklists/logic-checklist-payment-card-ru.csv)

##### Тест-кейсы

В проекте представлены [тест-кейсы проверки логики кнопки бронирования.](Test-Cases/README.md)

##### Баг-репорты

[Баг-репорты](Bug-Reports/README.md) содержат описание дефекта, шаги воспроизведения, ожидаемый и фактический результат, окружение и вложения.


#### Подход к тестированию

Используемые типы тестирования:

- функциональное тестирование;
- регрессионное тестирование;
- UI тестирование;
- кроссбраузерное тестирование;
- тестирование бизнес-логики.

Подробнее: ```Test-Documentation/testing-approach.md```

#### Окружение

Тестирование проводилось:

- macOS Sonoma 15.2
- Firefox 134.0
- Yandex Browser 25.10
- 1920×1080 / 800×600

Подробнее: ```Test-Documentation/test-environment.md```

#### Итоги тестирования

1. Основной проект

- 409 проверок вёрстки
- 39 проверок логики платёжных окон
- 5 тест-кейсов для проверки кнопки бронирования
- 31 заведённый дефект

2. Демонстрационная версия (GitHub)

- 15 проверок верстки приложения
- 13 проверок для окон «Способ оплаты» и «Добавление карты»
- 3 тест-кейса
- 11 баг-репортов

Подробнее: ```Test-Documentation/test-summary.md```

#### Результат тестирования

В ходе тестирования были выявлены дефекты пользовательского интерфейса, отображения данных на карте и логики бронирования.

---

### Web Application Testing Project: a city route planning app

🇬🇧 | **EN** 

This project is focused on manual testing of a web application after UI and booking business logic changes.

The application allows users to build routes, select trip tariffs, choose cars, and book trips using forms with user and payment data.

The main testing goal was to verify booking user flows, UI stability, and correct processing of user input.

The repository contains a reduced demo version of test documentation, demonstrating the testing approach, documentation structure, and defect reporting format.

#### Test Artifacts

##### Checklists

- [UI layout verification checklist;](Checklists/layout-checklist-form-map-en.csv)
- [payment windows and form logic checklist.](Checklists/logic-checklist-payment-card-en.csv)

##### Test Cases

The project includes [booking button logic test cases.](Test-Cases/README.md)

##### Bug Reports

[Bug reports](Bug-Reports/README.md) include issue description, reproduction steps, expected and actual results, environment details, and attachments.

#### Testing Approach

Testing types were used:

- functional testing;
- regression testing;
- UI testing;
- cross-browser testing;
- business logic testing.

More details: ```Test-Documentation/testing-approach.md```

#### Test Environment

Testing was performed using:

- macOS Sonoma 15.2
- Firefox 134.0
- Yandex Browser 25.10
- 1920×1080 / 800×600

More details: ```Test-Documentation/test-environment.md```

#### Testing Summary

1. Main Project

- 409 layout checks
- 39 payment window logic checks
- 5 booking test cases
- 31 reported defects

2. Demo Version (GitHub)

- 15 layout checks
- 13 payment window logic checks
- 3 test cases
- 11 bug reports

More details: ```Test-Documentation/test-summary.md```

#### Testing Result

Testing revealed UI issues, map data display defects, and booking logic problems.