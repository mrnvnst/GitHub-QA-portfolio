## Баг-репорты

🇷🇺 | **RU**

В директории представлены дефекты, выявленные при тестировании API сервиса доставки продуктов.

---

### Сводная таблица дефектов

### I. Kits – Добавление продуктов в набор.

| ID    | Эндпоинт                        | Название                 | Серьёзность | Статус |
| ----- | ------------------------------- | ---------------------------------- | -------- | ------ |
| BR-001 | POST /api/v1/kits/{id}/products | 500 при отсутствии productsList    | Критический | Открыт   |
| BR-002 | POST /api/v1/kits/{id}/products | 500 при пустом body                | Критический | Открыт   |
| BR-003 | POST /api/v1/kits/{id}/products | 200 при несуществующем id продукта | Критический | Открыт   |
| BR-004 | POST /api/v1/kits/{id}/products | 200 при отсутствии id продукта     | Критический | Открыт   |
| BR-005 | POST /api/v1/kits/{id}/products | 200 при id = 0                     | Критический | Открыт   |
| BR-006 | POST /api/v1/kits/{id}/products | 200 при отрицательном id           | Критический | Открыт   |
| BR-007 | POST /api/v1/kits/{id}/products | 500 при id > INT                   | Критический | Открыт   |
| BR-008 | POST /api/v1/kits/{id}/products | 500 при нечисловом id              | Критический | Открыт   |
| BR-009 | POST /api/v1/kits/{id}/products | 500 при отсутствии quantity        | Критический | Открыт   |
| BR-010 | POST /api/v1/kits/{id}/products | 500 при строковом quantity         | Критический | Открыт   |
| BR-011 | POST /api/v1/kits/{id}/products | 200 при quantity = 0               | Критический | Открыт   |
| BR-012 | POST /api/v1/kits/{id}/products | 500 при дробном quantity           | Критический | Открыт   |
| BR-013 | POST /api/v1/kits/{id}/products | 200 при пустом quantity            | Критический | Открыт   |
| BR-014 | POST /api/v1/kits/{id}/products | 500 при отрицательном quantity     | Критический | Открыт   |
| BR-015 | POST /api/v1/kits/{id}/products | 500 при quantity > INT             | Критический | Открыт   |

---

### II. Couriers / Fast Delivery – Проверка возможности доставки и ее стоимости.

| ID    | Эндпоинт                                          | Название                                | Серьёзность | Статус |
| ----- | ------------------------------------------------- | ----------------------------------------------- | -------- | ------ |
| BR-016 | POST /fast-delivery/v3.1.1/calculate-delivery.xml | 500 при отсутствии параметров                   | Критический | Открыт   |
| BR-017 | POST /fast-delivery/v3.1.1/calculate-delivery.xml | 200 при невалидном productsCount                | Критический | Открыт   |
| BR-018 | POST /fast-delivery/v3.1.1/calculate-delivery.xml | 500 вместо ошибки валидации (weight/time)       | Критический | Открыт   |
| BR-021 | POST /fast-delivery/v3.1.1/calculate-delivery.xml | Некорректное XML-тело ответа вне времени работы | Критический | Открыт   |

---

### III. Basket – Добавление продуктов в корзину. Удаление корзины.

| ID    | Эндпоинт                  | Название                     | Серьёзность | Статус |
| ----- | ------------------------- | -------------------------------------- | -------- | ------ |
| BR-24 | PUT /api/v1/orders/:id    | 200 при передаче строки вместо массива | Критический | Открыт   |
| BR-27 | PUT /api/v1/orders/:id    | 500 при id > INT                       | Критический | Открыт   |
| BR-29 | PUT /api/v1/orders/:id    | 200 при quantity = empty / 0 / null    | Критический | Открыт   |
| BR-31 | DELETE /api/v1/orders/:id | 404 при удалении существующей корзины  | Критический | Открыт   |

---

### Метрики

- Общее количество дефектов: 23
- Критические: 23 (100%)
- Ошибки сервера (500): 11
- Нарушение бизнес-логики: 8
- Некорректные HTTP-статусы: 4


## API Bug Reports

🇬🇧 | **EN**

All defects were identified during testing of the grocery delivery backend service using Postman.

### Summary Table

| ID | Endpoint | Issue Summary | Severity | Status |
|----|----------|--------------|----------|--------|
| BR-01 | POST /api/v1/kits/{id}/products | 500 when productsList missing | Critical | Open |
| BR-02 | POST /api/v1/kits/{id}/products | 500 on empty body | Critical | Open |
| BR-03 | POST /api/v1/kits/{id}/products | 200 when product ID does not exist | Critical | Open |
| BR-04 | POST /api/v1/kits/{id}/products | 200 when product id missing | Critical | Open |
| BR-05 | POST /api/v1/kits/{id}/products | 200 when id = 0 | Critical | Open |
| BR-06 | POST /api/v1/kits/{id}/products | 200 when id < 0 | Critical | Open |
| BR-07 | POST /api/v1/kits/{id}/products | 500 when id exceeds INT | Critical | Open |
| BR-08 | POST /api/v1/kits/{id}/products | 500 when id not numeric | Critical | Open |
| BR-09 | POST /api/v1/kits/{id}/products | 500 when quantity missing | Critical | Open |
| BR-10 | POST /api/v1/kits/{id}/products | 500 when quantity string | Critical | Open |
| BR-11 | POST /api/v1/kits/{id}/products | 200 when quantity = 0 | Critical | Open |
| BR-12 | POST /api/v1/kits/{id}/products | 500 when quantity decimal | Critical | Open |
| BR-13 | POST /api/v1/kits/{id}/products | 200 when quantity empty | Critical | Open |
| BR-14 | POST /api/v1/kits/{id}/products | 500 when quantity negative | Critical | Open |
| BR-15 | POST /api/v1/kits/{id}/products | 500 when quantity exceeds INT | Critical | Open |

---

### II. Couriers / Fast Delivery

| ID | Endpoint | Issue Summary | Severity | Status |
|----|----------|--------------|----------|--------|
| BR-16 | POST //fast-delivery/v3.1.1/calculate-delivery.xml | 500 when parameters missing | Critical | Open |
| BR-17 | POST /fast-delivery/v3.1.1/calculate-delivery.xml | 200 when invalid productsCount | Critical | Open |
| BR-21 | POST /fast-delivery/v3.1.1/calculate-delivery.xml | Incorrect XML response outside working hours | Critical | Open |
| BR-18 | POST /fast-delivery/v3.1.1/calculate-delivery.xml | 500 instead of validation error (weight/time invalid) | Critical | Open |

---

### III. Basket

| ID | Endpoint | Issue Summary | Severity | Status |
|----|----------|--------------|----------|--------|
| BR-24 | PUT /api/v1/orders/:id | 200 when productsList is string | Critical | Open |
| BR-27 | PUT /api/v1/orders/:id | 500 when id exceeds INT | Critical | Open |
| BR-29 | PUT /api/v1/orders/:id | 200 when quantity empty / 0 / null | Critical | Open |
| BR-31 | DELETE /api/v1/orders/:id | 404 when deleting existing basket | Critical | Open |

---

### Metrics

- Total defects: 23
- Critical: 23 (100%)
- Server Errors (500): 11
- Business Logic Violations: 8
- Incorrect HTTP Status Codes: 4