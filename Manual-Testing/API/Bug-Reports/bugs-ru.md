## Баг-репорты
### Навигация

1. Добавление продукта в набор: POST /api/v1/kits/{id}/products 
- [BR-001: POST /api/v1/kits/{id}/products статус 500 при непереданном productsList](#br-001)
- [BR-002: POST /api/v1/kits/{id}/products статус 500 при пустом JSON body](#br-002)
- [BR-003: POST /api/v1/kits/{id}/products статус 200 при несуществующем в БД id продукта](#br-003)
- [BR-004: POST /api/v1/kits/{id}/products статус 200 при отсутствии id продукта в запросе](#br-004)
- [BR-005: POST /api/v1/kits/{id}/products статус 200 при переданном id = 0 продукта](#br-005)
- [BR-006: POST /api/v1/kits/{id}/products статус 200 при отрицательном значении в id продукта](#br-006)
- [BR-007: POST /api/v1/kits/{id}/products статус 500 при передаче id продукта в значении, превышающим допустимый диапазон integer](#br-007)
- [BR-008: POST /api/v1/kits/{id}/products статус 500 при id продукта в нечисловом значении](#br-008)
- [BR-009: POST /api/v1/kits/{id}/products статус 500 при непереданном quantity продукта](#br-009)
- [BR-010: POST /api/v1/kits/{id}/products статус 500 при передаче строки в quantity продукта](#br-010)
- [BR-011: POST /api/v1/kits/{id}/products статус 200 при quantity = 0](#br-011)
- [BR-012: POST /api/v1/kits/{id}/products статус 500 при дробном значении quantity](#br-012)
- [BR-013: POST /api/v1/kits/{id}/products статус 200 при пустом значении в quantity продукта](#br-013)
- [BR-014: POST /api/v1/kits/{id}/products статус 500 при отрицательном числовом значении в quantity продукта](#br-014)
- [BR-015: POST /api/v1/kits/{id}/products статус 500 при передаче в quantity продукта значения, превышающего допустимый диапазон integer](#br-015)

2. Проверка возможности доставки и ее стоимости: POST /fast-delivery/v3.1.1/calculate-delivery.xml
- [BR-016: POST /fast-delivery/v3.1.1/calculate-delivery.xml возвращает 500 при непереданных параметрах](#br-016)
- [BR-017: POST /fast-delivery/v3.1.1/calculate-delivery.xml возвращает 200 OK при невалидном значении productsCount](#br-017)
- [BR-019: POST /fast-delivery/v3.1.1/calculate-delivery.xml возвращает 200 OK при невалидном значении productsWeight](#br-019)
- [BR-021: POST /fast-delivery/v3.1.1/calculate-delivery.xml ошибка в теле ответа при delieveryTime, заданном вне рабочего диапазона доставки](#br-021)

3. Добавление продуктов в корзину: PUT /api/v1/orders/:id
- [BR-024: PUT /api/v1/orders/:id статус 200 при передаче строки вместо массива](#br-024)
- [BR-027: PUT /api/v1/orders/:id статус 500 при передаче id продукта, превышающего допустимый диапазон типа integer](#br-027)
- [BR-029: PUT /api/v1/orders/:id статус 200 при передаче quantity продукта в формате null, 0 и при пустом значении](#br-029)

4. Удаление корзины: DELETE /api/v1/orders/:id 
- [BR-031: DELETE /api/v1/orders/:id статус 404 при удалении существующей корзины](#br-031)

## BR-001
## POST /api/v1/kits/{id}/products статус 500 при непереданном productsList

### Описание

При отправке POST-запроса без передачи обязательного параметра productsList сервер возвращает 500 Internal Server Error.

Согласно требованиям API, при отсутствии обязательных параметров должен возвращаться 400 Bad Request.

### Предусловия

1. Сервер запущен.
2. Создан набор id = 7.

### Шаги воспроизведения

1. Отправить POST-запрос на
 /api/v1/kits/:id/products
2. Передать пустое тело запроса.


### ОР

1. 400 Bad Request.

### ФР  

1. 500 Internal Server Error.


### Вложение     

```
curl --location --request POST 'https://teststand.ru/api/v1/kits/7/products' \
--data ''
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-002
## POST /api/v1/kits/{id}/products статус 500 при пустом JSON body

### Описание

Передача пустого JSON ({}) приводит к 500 Internal Server Error.

Ожидается 400 Bad Request.

### Предусловия

1. Сервер запущен.
2. Создан набор id = 7.

### Шаги воспроизведения

1. Отправить POST-запрос на
 /api/v1/kits/:id/products
2. Передать пустое тело запроса.


### ОР

1. 400 Bad Request.

### ФР  

1. 500 Internal Server Error.


### Вложение     

```
"curl --location --request POST 'https://teststand.ru/api/v1/kits/7/products' \
--data '"
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-003
## POST /api/v1/kits/{id}/products статус 200 при несуществующем в БД id продукта

### Описание

API позволяет добавить продукт с id, отсутствующим в базе данных.

### Предусловия

1. Сервер запущен.
2. Создан набор id = 7.

### Шаги воспроизведения

1. Отправить POST-запрос на
 /api/v1/kits/:id/products
2. В теле запроса указать:

```json
{
  "productsList": [
    { "id": 127, "quantity": 2 }
  ]
}
```

### ОР

1. 400 Bad Request.
2. Продукт не добавляется в набор.

### ФР  

1. 200 OK.
2. Продукт добавляется в набор.


### Вложение     

```
"curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 127,
            ""quantity"": 2
        }
    ]
}'"
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-004
## POST /api/v1/kits/{id}/products статус 200 при отсутствии id продукта в запросе

### Описание

При отсутствии поля id внутри объекта productsList сервер возвращает 200 OK.

Продукт добавляется с некорректным значением (id: undefined).

### Предусловия

1. Сервер запущен.
2. Создан набор id = 7.

### Шаги воспроизведения

1. Отправить POST-запрос на
 /api/v1/kits/:id/products
2. В теле запроса указать:

```json
{
    "productsList": [
        {
            "quantity": 3
        }
    ]
}
```

### ОР

1. 400 Bad Request.
2. Продукт не добавляется в набор.

### ФР  

1. 200 OK.
2. Продукт добавляется в набор:

```json
 [id:undefined; quantity:3]
```


### Вложение     

```
"curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""quantity"": 3
        }
    ]
}'"
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-005
## POST /api/v1/kits/{id}/products статус 200 при переданном id = 0 продукта

### Описание

Передача id = 0 приводит к успешному добавлению продукта.

### Предусловия

1. Сервер запущен.
2. Создан набор id = 7.

### Шаги воспроизведения

1. Отправить POST-запрос на
 /api/v1/kits/:id/products
2. В теле запроса указать:

```json
{
    "productsList": [
        {
            "id": 0,
            "quantity": 1
        }
    ]
```

### ОР

1. 400 Bad Request.
2. Продукт не добавляется в набор.

### ФР  

1. 200 OK.
2. Продукт добавляется в набор:

```json
 [id:0; quantity:1]
```


### Вложение     

```
"curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 0,
            ""quantity"": 1
        }
    ]
}'"
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-006
## POST /api/v1/kits/{id}/products статус 200 при отрицательном значении в id продукта

### Описание

При передаче отрицательного значения id сервер возвращает 200 OK и добавляет продукт.

### Предусловия

1. Сервер запущен.
2. Создан набор id = 7.

### Шаги воспроизведения

1. Отправить POST-запрос на
 /api/v1/kits/:id/products
2. В теле запроса указать:

```json
{
    "productsList": [
        {
            "id": -7,
            "quantity": 1
        }
    ]
}
```

### ОР

1. 400 Bad Request.
2. Продукт не добавляется в набор.

### ФР  

1. 200 OK.
2. Продукт добавляется в набор:

```json
 [id:-7; quantity:1]
```


### Вложение     

```
curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    "productsList": [
        {
            "id": -7,
            "quantity": 1
        }
    ]
}'
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-007
## POST /api/v1/kits/{id}/products статус 500 при передаче id продукта в значении, превышающим допустимый диапазон integer

### Описание

При передаче значения id, превышающего допустимый диапазон integer, сервер возвращает 500 Internal Server Error.

Согласно требованиям должен возвращаться 400 Bad Request.

### Предусловия

1. Сервер запущен.
2. Создан набор id = 7.

### Шаги воспроизведения

1. Отправить POST-запрос на
 /api/v1/kits/:id/products
2. В теле запроса указать:

```json
{
  "productsList": [
    { "id": 2147483795, "quantity": 1 }
  ]
}
```

### ОР

1. 400 Bad Request.
2. Продукт не добавляется в набор.

### ФР  

1. 500 Internal Server Error.


### Вложение     

```
"curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 2147483795,
            ""quantity"": 1
        }
    ]
}'"
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-008
## POST /api/v1/kits/{id}/products статус 500 при id продукта в нечисловом значении

### Описание

При передаче id продукта в нечисловом формате (строка, спецсимволы, boolean, пустая строка) сервер возвращает 500 Internal Server Error.

Ожидается 400 Bad Request.

### Предусловия

1. Сервер запущен.
2. Создан набор id = 7.

### Шаги воспроизведения

1. Отправить POST-запрос на
 /api/v1/kits/:id/products
2. В теле запроса указать:

```json
{
    "productsList": [
        {
            "id": "тридцать",
или
            "id": "%^$",
или
            "id": true,
или
            "id": "",

            "quantity": 1
        }
    ]
}
```

### ОР

1. 400 Bad Request.

### ФР  

1. 500 Internal Server Error.

### Вложение     

```
"1. curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": ""тридцать"",
            ""quantity"": 1
        }
    ]
}'

2. curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": ""%^$"",
            ""quantity"": 1
        }
    ]
}'

3.  curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": """",
            ""quantity"": 1
        }
    ]
}'

4. curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": true,
            ""quantity"": 1
        }
    ]
}'"
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-009
## POST /api/v1/kits/{id}/products статус 500 при непереданном quantity продукта

### Описание

При отсутствии поля quantity сервер возвращает 500 Internal Server Error.

Ожидается 400 Bad Request.

### Предусловия

1. Сервер запущен.
2. Создан набор id = 7.

### Шаги воспроизведения

1. Отправить POST-запрос на
 /api/v1/kits/:id/products
2. В теле запроса указать:

```json
{
    "productsList": [
        {
            "id": 28
        }
    ]
}
```

### ОР

1. 400 Bad Request.

### ФР  

1. 500 Internal Server Error:

```json
{"code":500,"message":"invalid input syntax for integer: \"3undefined\""}
```

### Вложение     

```
"curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 28
        }
    ]
}'"
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-010
## POST /api/v1/kits/{id}/products статус 500 при передаче строки в quantity продукта

### Описание

Передача quantity в виде строки ("семь") приводит к 500 Internal Server Error.

### Предусловия

1. Сервер запущен.
2. Создан набор id = 7.

### Шаги воспроизведения

1. Отправить POST-запрос на
 /api/v1/kits/:id/products
2. В теле запроса указать:

```json
{
    "productsList": [
        {
            "id": 3,
            "quantity": "семь"
        }
    ]
}
```

### ОР

1. 400 Bad Request.

### ФР  

1. 500 Internal Server Error.

### Вложение     

```
"curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 3,
            ""quantity"": ""семь""
        }
    ]
}'"
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-011
## POST /api/v1/kits/{id}/products статус 200 при quantity = 0

### Описание

Передача quantity = 0 приводит к успешному добавлению продукта.

### Предусловия

1. Сервер запущен.
2. Создан набор id = 7.

### Шаги воспроизведения

1. Отправить POST-запрос на
 /api/v1/kits/:id/products
2. В теле запроса указать:

```json
{
    "productsList": [
        {
            "id": 3,
            "quantity": 0
        }
    ]
}
```

### ОР

1. 400 Bad Request.

### ФР  

1. 200 OK.
2. Продукт добавляется в набор:

```json
[id:3; quantity:0]
```

### Вложение     

```
curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 3,
            ""quantity"": 0
        }
    ]
} 
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-012
## POST /api/v1/kits/{id}/products статус 500 при дробном значении quantity

### Описание

Передача дробного значения (7.4) в поле quantity приводит к 500 Internal Server Error.

### Предусловия

1. Сервер запущен.
2. Создан набор id = 7.

### Шаги воспроизведения

1. Отправить POST-запрос на
 /api/v1/kits/:id/products
2. В теле запроса указать:

```json
{
    "productsList": [
        {
            "id": 12,
            "quantity": 7.4
        }
    ]
}
```

### ОР

1. 400 Bad Request.

### ФР  

1. 500 Internal Server Error:

```json
"code":500,"message":"invalid input syntax for integer: \"10.4\""
```

### Вложение     

```
curl --location 'https://144b85d2-7f95-4653-b594-be7173cae0da.serverhub.praktikum-services.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 12,
            ""quantity"": 7.4

        }
    ]
}
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-013
## POST /api/v1/kits/{id}/products статус 200 при пустом значении в quantity продукта

### Описание

Передача пустой строки в quantity приводит к успешному добавлению продукта.

### Предусловия

1. Сервер запущен.
2. Создан набор id = 7.

### Шаги воспроизведения

1. Отправить POST-запрос на
 /api/v1/kits/:id/products
2. В теле запроса указать:

```json
{
    "productsList": [
        {
            "id": 12,
            "quantity": ""
        }
    ]
}
}
```

### ОР

1. 400 Bad Request.

### ФР  

1. 500 Internal Server Error.
2. Продукт добавляется в набор:

```json
[id:12; quantity:]
```

### Вложение     

```"curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 12,
            ""quantity"": """"
        }
    ]
}'"
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-014
## POST /api/v1/kits/{id}/products статус 500 при отрицательном числовом значении в quantity продукта

### Описание

Передача отрицательного значения количества приводит к 500 Internal Server Error.

Ожидается 400 Bad Request.

### Предусловия

1. Сервер запущен.
2. Создан набор id = 7.

### Шаги воспроизведения

1. Отправить POST-запрос на
 /api/v1/kits/:id/products
2. В теле запроса указать:

```json
{
    "productsList": [
        {
            "id": 17,
            "quantity":-3
        }
    ]
}
```

### ОР

1. 400 Bad Request.

### ФР  

1. 500 Internal Server Error:

```json
{"code":500,"message":"invalid input syntax for integer: \"3-3\""}

```

### Вложение     

```
"curl --location 'https://teststand.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 17,
            ""quantity"":-3
        }
    ]
}'"
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-015
## POST /api/v1/kits/{id}/products статус 500 при передаче в quantity продукта значения, превышающего допустимый диапазон integer 

### Описание

Передача значения quantity, превышающего допустимый диапазон integer, вызывает 500 Internal Server Error.

Ожидается 400 Bad Request.

### Предусловия

1. Сервер запущен.
2. Создан набор id = 7.

### Шаги воспроизведения

1. Отправить POST-запрос на
 /api/v1/kits/:id/products
2. В теле запроса указать:

```json
{
    "productsList": [
        {
            "id": 25,
            "quantity":2147483647
        }
    ]
}
```

### ОР

1. 400 Bad Request.

### ФР  

1. 500 Internal Server Error:

```json

{"code":500,"message":"value \"32147483647\" is out of range for type integer"}
```

### Вложение     

```
"curl --location 'https://144b85d2-7f95-4653-b594-be7173cae0da.serverhub.praktikum-services.ru/api/v1/kits/7/products' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 25,
            ""quantity"":2147483647
        }
    ]
}'
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-016
## POST /fast-delivery/v3.1.1/calculate-delivery.xml возвращает 500 при непереданных параметрах

### Описание

При отправке запроса на расчёт быстрой доставки без передачи обязательных параметров (productsCount, productsWeight, deliveryTime) сервер возвращает 500 Internal Server Error.

Согласно требованиям, при отсутствии обязательных параметров API должно возвращать 400 Bad Request с сообщением о некорректных входных данных.

### Предусловия

Сервер запущен.

### Шаги воспроизведения

1. Отправить POST-запрос на
/fast-delivery/v3.1.1/calculate-delivery.xml
2. Передать пустое тело запроса.


### ОР

1. 400 Bad Request.
2. Доставка невозможна, стоимость доставки не рассчитывается.

### ФР  

1. 500 Internal Server Error.


### Вложение     

```
"curl --location 
--request POST 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--data ''"
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-017
## POST /fast-delivery/v3.1.1/calculate-delivery.xml возвращает 200 OK при невалидном значении productsCount


### Описание

При передаче в параметре productsCount значений:
- 0
- отрицательных чисел
- строки
- пустого значения
- числа > большого INT

API возвращает 200 OK и рассчитывает доставку,
вместо возврата ошибки валидации.

### Предусловия

Сервер запущен.

### Шаги воспроизведения

1. Отправить POST-запрос на
/fast-delivery/v3.1.1/calculate-delivery.xml

2. Передать тело запроса (0):

```xml
<InputModel>
    <productsCount>0</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```
или (отрицательное значение):

```xml
<InputModel>
    <productsCount>-1</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```
или (пустое значение):

```xml
<InputModel>
    <productsCount>""</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```

или (строка):

```xml
<InputModel>
    <productsCount>шесть</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```

или (большое числовое значение):

```xml
<InputModel>
    <productsCount>2147483700</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```

### ОР

1. 400 Bad Request
2. Доставка невозможна, стоимость доставки не рассчитывается.

### ФР  

1. 200 OK, в теле ответа:
    ```
    <response name="Привезём быстро" isItPossibleToDeliver="true"
    ```

2. Доставка возможна, рассчитана стоимость заказа.


### Вложение     

```
1. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>0</productsCount>    <productsWeight>0.1</productsWeight>    <deliveryTime>7</deliveryTime>
</InputModel>'

---

2. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>-1</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>'

---

3. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>""""</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>'

---

4. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>шесть</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>'

---

5. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>2147483700</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>'"
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-019
## POST /fast-delivery/v3.1.1/calculate-delivery.xml возвращает 200 OK при невалидном значении productsWeight

### Описание

При передаче в параметре productsWeight значений:
- 0
- отрицательных чисел
- строки
- пустого значения
- числа > большого INT

API возвращает 200 OK и рассчитывает доставку,
вместо возврата ошибки валидации.

### Предусловия

Сервер запущен.

### Шаги воспроизведения

1. Отправить POST-запрос на
/fast-delivery/v3.1.1/calculate-delivery.xml
2. Передать тело запроса (0):

```xml
<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>0</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```
или (непереданное значение):

```xml
<InputModel>
    <productsCount>1</productsCount>
    <productsWeight></productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```
или (пустое значение):

```xml
<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>""</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```

или (строка):

```xml
<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>два</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```

или (большое числовое значение):

```xml
<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>2147483700</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>
```

### ОР

1. 400 Bad Request.
2. Доставка невозможна, стоимость доставки не рассчитывается.

### ФР  

1. 200 OK, в теле ответа:

    ```xml
    <response name="Привезём быстро" isItPossibleToDeliver="true">
    ```
2. Доставка возможна, рассчитана стоимость заказа.

### Вложение  

```
1. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>0</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>'

2. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>1</productsCount>
    <productsWeight></productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>'

3. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>""""</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>'

4. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>два</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>'

5. curl --location 'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>2147483700</productsWeight>
    <deliveryTime>7</deliveryTime>
</InputModel>'"
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-021
## POST /fast-delivery/v3.1.1/calculate-delivery.xml ошибка в теле ответа при delieveryTime, заданном вне рабочего диапазона доставки

### Описание

При передаче значения deliveryTime, выходящего за границы рабочего времени службы доставки, сервер возвращает HTTP 200, однако в теле ответа отсутствует обязательный атрибут isItPossibleToDeliver.

### Предусловия

Сервер запущен.

### Шаги воспроизведения

1. Отправить POST-запрос на
/fast-delivery/v3.1.1/calculate-delivery.xml
2. Передать тело запроса:
```xml
<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>6</deliveryTime>
</InputModel>
```

### ОР

1. 200 OK, в теле ответа:

    ```
    <response name="Привезём быстро" isItPossibleToDeliver="false"/>
    ```

### ФР  

1. 200 OK, в теле ответа:

    ```
    <response name="Привезём быстро"/>
    ```

### Вложение  

```
curl --location \
'https://teststand.ru/fast-delivery/v3.1.1/calculate-delivery.xml' \
--header 'Content-Type: application/xml' \
--data '<InputModel>
    <productsCount>1</productsCount>
    <productsWeight>0.1</productsWeight>
    <deliveryTime>6</deliveryTime>
</InputModel>'
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-024
## PUT /api/v1/orders/:id статус 200 при передаче строки вместо массива

### Описание

При передаче параметра productsList в виде строки вместо массива сервер возвращает 200 OK и обрабатывает запрос как валидный.

Согласно требованиям, при некорректном типе данных должен возвращаться 409 Conflict и сообщение «Нет склада, способного обработать Ваш заказ».

### Предусловия

1. Сервер запущен.
2. Создана корзина id = 6.

### Шаги воспроизведения

1. Отправить PUT-запрос на
 /api/v1/orders/:id
2. В теле запроса указать:
```json
{
  "productsList": ""
}
```

### ОР

1. 409 OK, сообщение:

    ```json
    "message": «Нет склада, способного обработать Ваш заказ»
    ```

### ФР  

1. 200 OK.

### Вложение  

```
curl --location --request PUT \
'https://teststand.ru/api/v1/orders/6' \
--header 'Content-Type: application/json' \
--data '{"productsList": ""}'
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-027
## PUT /api/v1/orders/:id статус 500 при передаче id продукта, превышающего допустимый диапазон типа integer

### Описание

При передаче id продукта, превышающего допустимый диапазон типа integer, сервер возвращает 500 Internal Server Error.

Согласно требованиям, должен возвращаться 409 Conflict.

### Предусловия

1. Сервер запущен.
2. Создана корзина id = 2.

### Шаги воспроизведения

1. Отправить PUT-запрос на
 /api/v1/orders/:id
2. В теле запроса указать:
```json
{
  "productsList": [
    {
      "id": 2147483948,
      "quantity": 3
    }
  ]
}
```

### ОР

1. 409 OK, сообщение:

    ```json
    "message": «Нет склада, способного обработать Ваш заказ»
    ```

### ФР  

1. 500 Internal Server Error.

### Вложение  

```
curl --location --request PUT \
'https://<host>/api/v1/orders/2' \
--header 'Content-Type: application/json' \
--data '{"productsList":[{"id":2147483948,"quantity":3}]}'
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-029
## PUT /api/v1/orders/:id статус 200 при передаче quantity продукта в формате null, 0 и при пустом значении ""

### Описание

При передаче некорректного значения quantity (пустая строка, 0 или null) сервер возвращает 200 OK и добавляет продукт в корзину.

Согласно требованиям, должен возвращаться 409 Conflict.

### Предусловия

1. Сервер запущен.
2. Создана корзина id = 6.

### Шаги воспроизведения

1. Отправить PUT-запрос на
 /api/v1/orders/:id
2. В теле запроса указать:
```json
{
    "productsList": [
        {
            "id": 7,
            "quantity": ""

или

           "quantity": 0

или

            "quantity": null


        }
    ]
}
```

### ОР

1. 409 OK, сообщение:

    ```json
    "message": «Нет склада, способного обработать Ваш заказ»
    ```

### ФР  

1. 200 OK.
2. Продукты добавляются в корзину.

### Вложение  

```
1. curl --location --request PUT 'https://teststand.ru/api/v1/orders/6' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 7,
            ""quantity"": """"
        }
    ]
}'

2. curl --location --request PUT 'https://teststand.ru/api/v1/orders/6' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 7,
            ""quantity"": 0
        }
    ]
}'

3. curl --location --request PUT 'https://teststand.ru/api/v1/orders/6' \
--header 'Content-Type: application/json' \
--data '{
    ""productsList"": [
        {
            ""id"": 7,
            ""quantity"": null
        }
    ]
}'
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт

---

## BR-031
## DELETE /api/v1/orders/:id статус 404 при удалении существующей корзины

### Описание

При удалении существующей корзины сервер возвращает 404 Not Found вместо 200 OK.

### Предусловия

1. Сервер запущен.
2. Создана корзина id = 6.

### Шаги воспроизведения

1. Отправить DELETE-запрос на
 /api/v1/orders/6

### ОР

1. 200 OK. 
2. Корзина удалена.

### ФР  

1. 404 Not Found.
2. Корзина не удалена.

### Вложение  

```
curl --location --request DELETE 'https://teststand.ru/api/v1/orders/6'
```

### Окружение
- Стенд: https://teststand.ru.
- Версия API: /api/v3.1.1.
- Инструменты: Postman 11.85.1.

#### Серьёезность: Критический
#### Статус: Открыт
