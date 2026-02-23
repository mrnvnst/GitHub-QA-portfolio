### Тестирование API: сервис доставки продуктов по каталогу и наборам 

🇷🇺 | **RU**

**Описание проекта**

Проект посвящён ручному тестированию API сервиса доставки продуктов после внедрения новой функциональности.

Основная цель тестирования — проверить корректность работы новых эндпоинтов, их интеграцию с существующей логикой системы и устойчивость обработки ошибок.

В рамках тестирования проверялись:

- работа с наборами товаров: добавление продуктов в набор;
- работа с курьерами и расчёт быстрой доставки: возможность доставки курьерской службой «Привезём быстро» и её стоимость;
- работа с корзиной: добавление продуктов в корзину, удаление продуктов из корзины, получение списка продуктов в корзине;
- валидация входных данных;
- обработка ошибок API;
- логика расчёта доставки.

#### Покрытие (методы и эндпоинты)

- `POST /api/v1/kits/{id}/products`
- `POST /fast-delivery/v3.1.1/calculate-delivery.xml`
- `POST /api/v1/orders`
- `PUT /api/v1/orders/{id}`
- `GET /api/v1/orders/{id}`
- `PUT /api/v1/orders/{id}/complete`
- `DELETE /api/v1/orders/{id}`

#### Структура

- `Test-Documentation/` – описание подходов к тестированию и отчет по итогам тестирования;
- `Checklists/` – чек-лист в формате .md;
- `Postman/` – коллекция, окружение и тестовые данные;
- `Bug-Report/` – баг-репорты.

#### Использованные инструменты

- Postman
- API-документация – Apidoc
- Google Sheets (составление чек-листов и баг-трекинг)

---

### API testing: grocery delivery service

🇬🇧 | **EN**

**Project description:**

This project focuses on manual testing of a backend API for a grocery delivery service after introducing new functionality.

The main testing goal was to verify correctness of new endpoints, their integration with existing system logic, and API error handling stability.

The testing covered:

- product kits management (adding products to a kit);
- courier service integration and fast delivery cost calculation;
- basket operations: adding products, retrieving basket contents, and deleting the basket;
- input data validation;
- API error handling;
- delivery cost calculation logic.


#### Covered API (methods and endpoints)


- `POST /api/v1/kits/{id}/products`
- `POST /fast-delivery/v3.1.1/calculate-delivery.xml`
- `POST /api/v1/orders`
- `PUT /api/v1/orders/{id}`
- `GET /api/v1/orders/{id}`
- `PUT /api/v1/orders/{id}/complete`
- `DELETE /api/v1/orders/{id}`


#### Project structure

- `Test-Documentation/` – testing approach and final report;
- `Checklists/` –  checklists in Markdown;
- `Postman` – collection, environment and test data;
- `Bug-Report/` – bug reports.


#### Tools Used

- Postman
- API documentation – Apidoc
- Google Sheets (checklists and bug tracking)
