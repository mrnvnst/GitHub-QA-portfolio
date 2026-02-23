### Проектирование тестов

🇷🇺 | **RU**

**При составлении чек-листа использовались следующие техники тест-дизайна:**

- Классы эквивалентности (КЭ)
    
    Проверка валидных и невалидных типов данных:

    - корректные числовые значения;
    - строковые значения;
    - пустые значения;
    - null;
    - значения вне допустимого диапазона.


- Граничные значения (ГЗ)
    
    Проверка:
    
    - минимальных допустимых значений;
    - максимальных допустимых значений;
    - значений на границе и за её пределами.


- Негативное тестирование
    
Проверка отсутствующих параметров, неверных типов данных и превышения ограничений.


- Проверка бизнес-логики

    - суммирование продуктов одной категории при добавлении их в корзину (quantity);
    - ограничения количества продуктов в наборе;
    - временные ограничения работы курьерской службы;
    - лимиты склада.


#### Источник требований

Тестовые данные сформированы на основании:

- API-документации (Apidoc);
- описанных ограничений (максимум 30 продуктов в наборе);
- диапазонов значений (вес, количество, время доставки);
- ожидаемой логики обработки ошибок (400 / 404 / 409 / 401).

---

### Test Design Techniques 

🇬🇧 | **EN**

**The checklist was designed using the following test design techniques:**

- Equivalence Partitioning (EP)
    
    Validation of:

    - valid numeric values;
    - string inputs;
    - empty values;
    - null values;
    - out-of-range values.

- Boundary Value Analysis (BVA)
    
    Validation of:

    - minimum allowed values;
    - maximum allowed values;
    - edge cases at and beyond limits.

- Negative Testing

Missing parameters, invalid types, and constraint violations.

- Business Logic Validation

    - quantity summation;
    - product count limits per kit;
    - delivery working hours restrictions;
    - warehouse limitations.

#### Requirements Source

Test data was derived from:

- API documentation (Apidoc);
- defined constraints (e.g., max 30 products per kit);
- numeric ranges (weight, count, delivery time);
- expected error handling logic (400 / 404 / 409 / 401).
