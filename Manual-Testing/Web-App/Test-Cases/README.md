### Тест-кейсы

🇷🇺 | **RU** 

Данная директория содержит демонстрационные тест-кейсы для проверки логики кнопки "Забронировать". 

Каждый тест-кейс оформлен в отдельном Markdown-файле и описывает конкретный пользовательский сценарий, связанный с различными состояниями обязательных полей формы бронирования.

В репозитории представлен сокращённый набор тест-кейсов. Полный набор использовался в рамках основного проекта.

#### Тест-сценарий

Кнопка бронирования – проверка бизнес-логики в зависимости от заполненности обязательных полей:

- адресов;
- прав;
- способа оплаты.

#### Требования для кнопки "Забронировать"

| **Заполненность полей**                                        | **Текст на кнопке**                                                   | **Результат действия**                  |
| -------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------- |
| Все обязательные поля и адреса заполнены                       | Забронировать. Маршрут составит … км и займет … мин                   | Открывается окно «Машина забронирована» |
| Все обязательные поля и адреса заполнены, кроме прав           | Добавить права и забронировать. Маршрут составит … км и займет … мин  | Открывается окно «Добавление прав»      |
| Все обязательные поля и адреса заполнены, кроме способа оплаты | Добавить оплату и забронировать. Маршрут составит … км и займет … мин | Открывается окно «Добавление карты»     |
| Все обязательные поля заполнены, адреса удалены                | Забронировать                                                         | Открывается окно «Машина забронирована» |
| Обязательные поля не заполнены и адреса удалены                | Добавить права и забронировать                                        | Открывается окно «Добавление прав»      |


#### Список тест-кейсов

[TC-BB-001](TC-BB-001-all-required-fields-filled.md)
 – Проверка логики кнопки бронирования при заполнении всех обязательных полей и адресов

[TC-BB-002](TC-BB-002-required-fields-filled-addresses-removed.md)
 – Проверка логики кнопки бронирования при заполнении обязательных полей и удалённых адресах

[TC-BB-003](TC-BB-003-payment-method-missing.md)
 – Проверка логики кнопки бронирования при заполнении обязательных полей и адресов при незаполненном способе оплаты

 #### Дополнительные тест-кейсы

В рамках основного проекта также были разработаны следующие тест-кейсы:

- Проверка логики кнопки бронирования при заполнении обязательных полей и адресов, при незаполненных правах (обнаружен дефект);

- Проверка логики кнопки бронирования при незаполненных обязательных правах и удалённых адресах (тест заблокирован).

---

### Test Cases

🇬🇧 | **EN** 

This section contains demo test cases created to verify the "Book" button logic of a web application.

Each test case is stored in a separate Markdown file and represents a specific user scenario related to different states of required booking form fields.

A reduced demo version of the test cases is presented in this repository. The full set of test cases was created and used in the main project.

#### Covered Test Scenario

Booking button — business logic validation depending on the state of required fields:

- addresses;
- driver’s license;
- payment method.

#### Test Cases List

[TC-BB-001](TC-BB-001-all-required-fields-filled.md)
 – Verify booking button logic when all required fields and addresses are filled.

[TC-BB-002](TC-BB-002-required-fields-filled-addresses-removed.md)
 – Verify booking button logic when required fields are filled and addresses are removed.

[TC-BB-003](TC-BB-003-payment-method-missing.md)
 – Verify booking button logic when required fields and addresses are filled but the payment method is missing.

#### Requirements for "Book" button

| Fields state                                                         | Button text                                                       | Action                                     |
| -------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------ |
| All required fields and addresses are filled                         | Book. The route will take … km and … min                          | “Car booked” window is displayed           |
| All required fields and addresses are filled except driver’s license | Add driver’s license and book. The route will take … km and … min | “Add driver’s license” window is displayed |
| All required fields and addresses are filled except payment method   | Add payment method and book. The route will take … km and … min   | “Add card” window is displayed             |
| All required fields are filled, addresses are removed                | Book                                                              | “Car booked” window is displayed           |
| Required fields are not filled and addresses are removed             | Add driver’s license and book                                     | “Add driver’s license” window is displayed |

 #### Additional Test Cases

 The following test cases were also created during the main project but are not included in this repository due to the demo scope:

- Verify booking button logic when required fields and addresses are filled but the driver’s license is missing (bug found);

- Verify booking button logic when the required driver’s license is missing and addresses are removed (test blocked).