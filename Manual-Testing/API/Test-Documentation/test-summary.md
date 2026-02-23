### Отчет о тестировании

🇷🇺 | **RU**

#### Тестовое покрытие


| Раздел    | Всего проверок | Failed | Passed | % дефектов |
| --------- | -------------- | ------ | ------ | ---------- |
| Kits      | 29             | 15     | 14     | 51.7%      |
| Couriers  | 8              | 4      | 4      | 50%        |
| Basket    | 8              | 4      | 4      | 50%        |
| **Итого** | **45**         | **23** | **22** | **51.1%**  |

#### Выводы

Тестирование показало наличие критических дефектов в логике валидации входных данных.

Наиболее проблемные зоны:

- отсутствие корректной серверной валидации обязательных параметров;
- некорректная обработка невалидных типов данных;
- ошибки в бизнес-логике.

Релиз протестированной функциональности не готов к выпуску в продакшен,
так как дефекты затрагивают:

- валидацию данных,
- корректность расчётов,
- стабильность API.

Рекомендуется исправление дефектов критического уровня и повторное регрессионное тестирование.

---

🇬🇧 | **EN**

### Test Summary

#### Test coverage summary

| Section   | Total Tests | Failed | Passed | Defect Rate |
| --------- | ----------- | ------ | ------ | ----------- |
| Kits      | 29          | 15     | 14     | 51.7%       |
| Couriers  | 8           | 4      | 4      | 50%         |
| Basket    | 8           | 4      | 4      | 50%         |
| **Total** | **45**      | **23** | **22** | **51.1%**   |

#### Conclusion

Testing revealed multiple critical issues related to input validation and business logic implementation.

Main problem areas:

- missing server-side validation for required parameters;
- incorrect handling of invalid data types;
- business logic inconsistencies (limits, delivery working hours);
- basket deletion instability (500 instead of 200).

**Final Assessment**

The tested functionality is not ready for production release,
as defects affect:

- data validation,
- calculation correctness,
- API stability.

Fixing Critical issues and performing regression testing is required before release.