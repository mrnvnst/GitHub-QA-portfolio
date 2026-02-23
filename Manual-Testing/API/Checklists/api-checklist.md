## Чек-листы | Checklists

## Навигация | Navigation

- [I. Kits](#i-kits)
- [II. Couriers (Fast Delivery)](#ii-couriers-fast-delivery)
- [III. Basket](#iii-basket)

### I. Kits

```
POST /api/v1/kits/{id}/products
GET /api/v1/kits/{id}
```

🇷🇺 | **RU**

| №  | Раздел        | Проверка                                           | Ожидаемый результат          | Статус | Bug ID |
| -- | ------------- | -------------------------------------------------- | ---------------------------- | ------ | ------ |
| 1  | Позитив       | Добавление продукта в существующий набор (id=1)    | 200 OK, набор изменён        | Passed | —      |
| 2  | Негатив       | Добавление продукта в несуществующий набор (id=67) | 404 Not Found                | Passed | —      |
| 3  | Негатив       | Добавление продукта, если productsList передан строкой                       | 400 Bad Request              | Passed | —      |
| 4  | Негатив       | Проверка непереданного productsList                           | 400 Bad Request              | Failed | BR-1   |
| 5  | Негатив       | Продукт не добавляется, если в productsList пустой массив                         | 400 Bad Request              | Failed | BR-2   |
| 6  | Позитив       | Продукт добавляется в набор: валидный id продукта (10), quantity=3              | 200 OK, набор изменён        | Passed | —      |
| 7  | Негатив       | Продукт не добавляется в набор: несуществующий id продукта (127)                   | 400 Bad Request              | Failed | BR-3   |
| 8  | Позитив       | Продукт добавляется в набор: валидный id (12), валидное большое quantity (157)           | 200 OK                       | Passed | —      |
| 9  | Негатив       | Продукт не добавляется в набор: id продукта отсутствует                            | 400 Bad Request              | Failed | BR-4   |
| 10 | Негатив       | Продукт не добавляется в набор: id = 0                                             | 400 Bad Request              | Failed | BR-5   |
| 11 | Негатив       | Продукт не добавляется в набор: id отрицательный (-7)                              | 400 Bad Request              | Failed | BR-6   |
| 12 | Негатив       | Продукт не добавляется в набор: id > большое (2147483795) int                                           | 400 Bad Request              | Failed | BR-7   |
| 13 | Негатив       | Продукт не добавляется в набор: id строка ("тридцать")                             | 400 Bad Request              | Failed | BR-8   |
| 14 | Негатив       | Продукт не добавляется в набор: id спецсимволы ("%^$")                             | 400 Bad Request              | Failed | BR-8   |
| 15 | Негатив       | Продукт не добавляется в набор: id boolean (true)                                  | 400 Bad Request              | Failed | BR-8   |
| 16 | Негатив       | Продукт не добавляется в набор: id пустое значение ("")                            | 400 Bad Request              | Failed | BR-8   |
| 17 | Негатив       | Продукт не добавляется в набор: quantity отсутствует                               | 400 Bad Request              | Failed | BR-9   |
| 18 | Негатив       | Продукт не добавляется в набор: quantity строка ("семь")                           | 400 Bad Request              | Failed | BR-10  |
| 19 | Негатив       | Продукт не добавляется в набор: quantity = 0                                       | 400 Bad Request              | Failed | BR-11  |
| 20 | Негатив       | Продукт не добавляется в набор: quantity дробное (7.4)                             | 400 Bad Request              | Failed | BR-12  |
| 21 | Негатив       | Продукт не добавляется в набор: quantity пустое ("")                               | 400 Bad Request              | Failed | BR-13  |
| 22 | Негатив       | Продукт не добавляется в набор: quantity отрицательное (-3)                        | 400 Bad Request              | Failed | BR-14  |
| 23 | Негатив       | Продукт не добавляется в набор: quantity > int                                     | 400 Bad Request              | Failed | BR-15  |
| 24 | Позитив | Проверка суммирования: повторное добавление id=12 (суммирование quantity) | 200 OK, количество суммируется | Passed | —      |
| 25 | Позитив            | Проверка добавления в набор: добавление 17 уникальных id                        | 200 OK                       | Passed | —      |
| 26 | Позитив            | Проверка добавления в набор: добавление 29 уникальных id                        | 200 OK                       | Passed | —      |
| 27 | Позитив            | Проверка добавления в набор: добавление 30 уникальных id                        | 200 OK                       | Passed | —      |
| 28 | Негатив   | Проверка добавления в набор: добавление 31 уникального id                       | 400 Bad Request (≤30)        | Passed | —      |
| 29 | Негатив   | Проверка добавления в набор: добавление 46 уникальных id                        | 400 Bad Request (≤30)        | Passed | —      |


🇬🇧 | **EN**

| #  | Category       | Test Case                                     | Expected Result          | Status | Bug ID |
| -- | -------------- | --------------------------------------------- | ------------------------ | ------ | ------ |
| 1  | Positive       | Add product to existing kit (id=1)            | 200 OK, kit modified     | Passed | —      |
| 2  | Negative       | Add product to non-existing kit (id=67)       | 404 Not Found            | Passed | —      |
| 3  | Negative       | productsList sent as string                   | 400 Bad Request          | Passed | —      |
| 4  | Negative       | productsList missing                          | 400 Bad Request          | Failed | BR-1   |
| 5  | Negative       | productsList empty array                      | 400 Bad Request          | Failed | BR-2   |
| 6  | Positive       | Valid product id (10), quantity=3             | 200 OK                   | Passed | —      |
| 7  | Negative       | Non-existing product id (127)                 | 400 Bad Request          | Failed | BR-3   |
| 8  | Positive       | Valid id (12), large quantity (157)           | 200 OK                   | Passed | —      |
| 9  | Negative       | Product id missing                            | 400 Bad Request          | Failed | BR-4   |
| 10 | Negative       | id = 0                                        | 400 Bad Request          | Failed | BR-5   |
| 11 | Negative       | Negative id                                   | 400 Bad Request          | Failed | BR-6   |
| 12 | Negative       | id > int                                      | 400 Bad Request          | Failed | BR-7   |
| 13 | Negative       | id as string                                  | 400 Bad Request          | Failed | BR-8   |
| 14 | Negative       | id with special symbols                       | 400 Bad Request          | Failed | BR-8   |
| 15 | Negative       | id boolean                                    | 400 Bad Request          | Failed | BR-8   |
| 16 | Negative       | id empty                                      | 400 Bad Request          | Failed | BR-8   |
| 17 | Negative       | quantity missing                              | 400 Bad Request          | Failed | BR-9   |
| 18 | Negative       | quantity as string                            | 400 Bad Request          | Failed | BR-10  |
| 19 | Negative       | quantity = 0                                  | 400 Bad Request          | Failed | BR-11  |
| 20 | Negative       | quantity decimal                              | 400 Bad Request          | Failed | BR-12  |
| 21 | Negative       | quantity empty                                | 400 Bad Request          | Failed | BR-13  |
| 22 | Negative       | quantity negative                             | 400 Bad Request          | Failed | BR-14  |
| 23 | Negative       | quantity > large int                                | 400 Bad Request          | Failed | BR-15  |
| 24 | Positive | Duplicate product addition (quantity summing) | 200 OK, quantity summed  | Passed | —      |
| 25 | Positive       | Add 17 unique products                        | 200 OK                   | Passed | —      |
| 26 | Positive       | Add 29 unique products                        | 200 OK                   | Passed | —      |
| 27 | Positive       | Add 30 unique products                        | 200 OK                   | Passed | —      |
| 28 | Negative     | Add 31 unique products                        | 400 Bad Request (max 30) | Passed | —      |
| 29 | Negative     | Add 46 unique products                        | 400 Bad Request (max 30) | Passed | —      |

---

### II. Couriers (Fast Delivery)

```
POST /fast-delivery/v3.1.1/calculate-delivery.xml
```


🇷🇺 | **RU**

| №  | Раздел        | Проверка                            | Ожидаемый результат                                                           | Статус | Bug ID |
| -- | ------------- | ----------------------------------- | ----------------------------------------------------------------------------- | ------ | ------ |
| 30 | Позитив       | Доставка успешна: productsCount=1, weight=0.1, time=7 | 200 OK, isItPossibleToDeliver=true, hostDeliveryCost=23, clientDeliveryCost=0 | Passed | —      |
| 31 | Позитив            | Доставка успешна: productsCount=14, weight=6, time=21 | 200 OK, hostDeliveryCost=43                                                   | Passed | —      |
| 32 | Негатив       | Доставка неуспешна / ошибка: Не переданы все параметры           | 400 Bad Request                                                               | Failed | BR-16  |
| 33 | Позитив            | Доставка успешна: productsCount=7                     | 200 OK, hostDeliveryCost=23                                                   | Passed | —      |
| 35 | Позитив            | Доставка успешна: productsCount=8                     | 200 OK, hostDeliveryCost=43                                                   | Passed | —      |
| 42 | Негатив       | Доставка неуспешна / ошибка: productsCount=0                     | 400 Bad Request                                                               | Failed | BR-17  |
| 59 | Негатив       | Доставка неуспешна: productsWeight=0                    | 400 Bad Request                                                               | Failed | BR-19  |
| 68 | Негатив | Проверка isItPossibleToDeliver: deliveryTime=6 (до 07:00)           | isItPossibleToDeliver=false                                                   | Failed | BR-21  |


🇬🇧 | **EN**

| #  | Category       | Test Case                             | Expected Result                                | Status | Bug ID |
| -- | -------------- | ------------------------------------- | ---------------------------------------------- | ------ | ------ |
| 30 | Positive       | productsCount=1, weight=0.1, time=7   | 200 OK, isItPossibleToDeliver=true, hostDeliveryCost=23, clientDeliveryCost=0 | Passed | —      |
| 31 | Positive       | productsCount=14, weight=6, time=21   | 200 OK, hostDeliveryCost=43                    | Passed | —      |
| 32 | Negative       | Missing required parameters           | 400 Bad Request                                | Failed | BR-16  |
| 33 | Positive       | productsCount=7                       | 200 OK, cost tier 23                           | Passed | —      |
| 35 | Positive       | productsCount=8                       | 200 OK, cost tier 43                           | Passed | —      |
| 42 | Negative       | productsCount=0                       | 400 Bad Request                                | Failed | BR-17  |
| 59 | Negative       | productsWeight=0                      | 400 Bad Request                                | Failed | BR-19  |
| 68 | Negative | deliveryTime=6 (before working hours) | isItPossibleToDeliver=false                    | Failed | BR-21  |

---

### III. Basket

```
POST /api/v1/orders
PUT /api/v1/orders/{id}
GET /api/v1/orders/{id}
PUT /api/v1/orders/{id}/complete
DELETE /api/v1/orders/{id}
```

🇷🇺 | **RU**

| №   | Раздел        | Проверка                                               | Ожидаемый результат          | Статус | Bug ID |
| --- | ------------- | ------------------------------------------------------ | ---------------------------- | ------ | ------ |
| 80  | Позитив       | Успешное добавление в корзину: добавление товаров в существующую корзину (id=6)       | 200 OK, продукты добавлены   | Passed | —      |
| 81  | Негатив       | Ошибка при добавлении в корзину: добавление товаров в несуществующую корзину            | 404 Not Found                | Passed | —      |
| 82  | Негатив       | Ошибка при добавлении в корзину: productsList передан строкой                           | 409 Conflict                 | Failed | BR-24  |
| 85  | Позитив | Успешное суммирование в корзине: повторное добавление одного id — суммирование quantity | 200 OK, quantity суммируется | Passed | —      |
| 91  | Негатив       | Ошибка при добавлении в корзину: id продукта > int                                      | 409 Conflict                 | Failed | BR-27  |
| 98  | Негатив       | Ошибка при добавлении в корзину: quantity = 0                                           | 409 Conflict                 | Failed | BR-29  |
| 105 | Позитив       | Успех: удаление существующей корзины                          | 200 OK, ok=true              | Failed | BR-31  |
| 106 | Негатив       | Ошибка: удаление несуществующей корзины                        | 404 Not Found                | Passed | —      |


🇬🇧 | **EN**

| #   | Category       | Test Case                                     | Expected Result         | Status | Bug ID |
| --- | -------------- | --------------------------------------------- | ----------------------- | ------ | ------ |
| 80  | Positive       | Add products to existing basket (id=6)        | 200 OK, products added  | Passed | —      |
| 81  | Negative       | Add products to non-existing basket           | 404 Not Found           | Passed | —      |
| 82  | Negative       | productsList passed as string                 | 409 Conflict            | Failed | BR-24  |
| 85  | Positive | Duplicate product addition — quantity summing | 200 OK, quantity summed | Passed | —      |
| 91  | Negative       | Product id > large int                              | 409 Conflict            | Failed | BR-27  |
| 98  | Negative       | quantity = 0                                  | 409 Conflict            | Failed | BR-29  |
| 105 | Positive       | Delete existing basket                        | 200 OK, ok=true         | Failed | BR-31  |
| 106 | Negative       | Delete non-existing basket                    | 404 Not Found           | Passed | —      |
