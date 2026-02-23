### Postman — Тестирование API

🇷🇺 | **RU**

#### Описание

В данной директории представлена часть тестирования API сервиса доставки продуктов с применением инструментов Postman.
Возможен запуск как в режиме автоматизированного тестирования – во вкладке Scripts каждого метода коллекции реализованы проверки на JavaScript, – так и в режиме ручного тестирования.

Коллекция Postman реализует:
- проверку новой функциональности;
- покрытие позитивных и негативных сценариев (тестирование КЭ и ГЗ, проверка поведения при отсутствии параметров, бизнес-логика).

Для каждого запроса:

- добавлено описание во вкладке Docs;
- прописаны Pre-request и реализованы проверки во вкладке Scripts (Post-response);
- используются тестовые данные из папки test-data/.

#### Структура

- ```collection/``` – Postman collection (.json) с реализованными тестами;
- ```environment/``` – файл окружения с переменными;
- ```test-data/``` – JSON-файлы с наборами тестовых данных.

#### Покрытые ручки

**Работа с продуктовыми наборами**
- `POST /api/v1/kits/{id}/products`

**Быстрая доставка**
- `POST /fast-delivery/v3.1.1/calculate-delivery.xml`

**Работа с корзиной**
- `POST /api/v1/orders`
- `PUT /api/v1/orders/{id}`
- `GET /api/v1/orders/{id}`
- `PUT /api/v1/orders/{id}/complete`
- `DELETE /api/v1/orders/{id}`

#### Наборы

**I. Kits**

Проверяется первоначальное состояние набора, добавление продуктов в набор, состояние после изменения, корректность HTTP-ответа: кода и его структуры.

Используется сравнение состояния через переменную окружения:

```
kitBeforeState
```

**II. Couriers (Fast Delivery)**

Проверяется доставка курьерской службой «Привезём быстро» и ее стоимость. В частности: 

- корректность XML-ответа, его статус, наличие тега ```<response>```;
- валидация входных параметров;
- расчёт стоимости доставки;
- граничные значения;
- обработка невалидных данных;
- атрибуты:
```
isItPossibleToDeliver – возможна ли доставка: true/false

hostDeliveryCost – стоимость доставки для сервиса

clientDeliveryCost – стоимость доставки для клиента
```

**III. Basket**

Покрываются сценарии:

- создание корзины;
- добавление товаров в корзину;
- получение списка продуктов, добавленных в корзину;
- оформление заказа;
- удаление корзины.


#### Как запустить:

1. Открыть коллекцию;  
2. Выбрать окружение;  
3. Запустить нужный набор из коллекции с соответствующим набором данных JSON.

---

### Postman: API Testing

🇬🇧 | **EN**

#### Description

This directory contains a partial demonstration of API testing for a grocery delivery service using Postman.

The collection can be executed both in automated mode — JavaScript test scripts are implemented in the Scripts tab of each request — and in manual testing mode.

The Postman collection includes:

- validation of the newly implemented functionality;
- coverage of both positive and negative scenarios (boundary value analysis, equivalence partitioning, missing parameter validation, and business logic verification).

For each request:

- a description is provided in the Docs tab;
- Pre-request scripts and Post-response test scripts are implemented in the Scripts tab;
- test data is loaded from the test-data/ directory.

#### Structure

- ```collection/``` – Postman collection (.json) with implemented test scripts
- ```environment/``` – environment file containing variables
- ```test-data/``` – JSON files with structured test datasets

#### Covered Endpoints

**Kits**

- ```POST /api/v1/kits/{id}/products```

**Fast delivery**

- ```POST /fast-delivery/v3.1.1/calculate-delivery.xml```

**Basket**

- ```POST /api/v1/orders```
- ```PUT /api/v1/orders/{id}```
- ```GET /api/v1/orders/{id}```
- ```PUT /api/v1/orders/{id}/complete```
- ```DELETE /api/v1/orders/{id}```

#### Collection kits

**I. Kits**

The following is validated: the initial state of a kit, adding products to the kit, the state after modification, and the correctness of the HTTP response (status code and response structure).

State comparison is performed using the environment variable:

```
kitBeforeState
```

**II. Couriers (Fast Delivery)**

Validation covers delivery availability via the “Fast Delivery” courier service and cost calculation.

Specifically, the following is verified:

- correctness of the XML response, its status, and presence of the <response> tag;
- input parameter validation;
- delivery cost calculation logic;
- boundary value cases;
- handling of invalid input data;
- response attributes:
```
isItPossibleToDeliver – whether delivery is possible (true/false)

hostDeliveryCost – delivery cost for the service

clientDeliveryCost – delivery cost for the customer
```

**III. Basket**

The following scenarios are covered:

- basket creation;
- adding products to the basket;
- retrieving the list of products added to the basket;
- order completion;
- basket deletion.


#### Launch
1. Open collection;
2. Choose Environment;
3. Run the required set from the collection with the corresponding set of JSON data.