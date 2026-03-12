### ID: TC-BB-002

🇷🇺 | **RU** 

#### Название:
Проверка логики кнопки бронирования при заполнении обязательных полей формы бронирования и удалённых адресах.

**Предусловия:**
1. Перейти на тестовый стенд.
2. Ввести в поле "Откуда": "Хамовнический вал, 18".
3. Ввести в поле "Куда": "Усачева, 3".
4. Выбрать режим "Свой".
5. Выбрать вид транспорта "Каршеринг".
6. Нажать на кнопку "Забронировать".

**Описание шага:**
1. Нажать на поле "Добавить права".
2. В форму "Добавить права" ввести:

    - Имя: Евгений
    - Фамилия: Петров
    - Дата рождения: 01.04.1976
    - Номер: 0909123456

3. Нажать на кнопку "Добавить".
4. Нажать на поле "Способ оплаты".
5. В форме добавления банковской карты ввести:

    - Номер: 463801983657
    - Код: 76

6. Нажать на кнопку закрытия крестик.
7. Удалить адрес в поле «Откуда».
8. Удалить адрес в поле «Куда».
9. Нажать на кнопку "Забронировать".

**Ожидаемый результат:**  
- Текст на кнопке: "Забронировать".
- При нажатии на кнопку открывается окно "Машина забронирована"

**Статус:**

 Blocked

**Окружение:**
- ОС: MacOS Sonoma 15.2 (24C101)
- Браузер: Firefox 134.0
- Разрешение экрана: 1920×1080

**Ссылка на баг-репорт:**

[Bug-report-010](../Bug-Reports/bugs/BR-010-booking-form-disabled-after-address-removal.md)

---

### ID: TC-BB-002

🇬🇧 | **EN** 

**Title:**
Verify booking button logic when required booking form fields are filled and addresses are removed.

**Preconditions:**
1. Open the test environment.
2. Enter “Khamovnichesky Val, 18” into the “From” field.
3. Enter “Usacheva, 3” into the “To” field.
4. Select the “Custom” travel mode.
5. Select “Car sharing” as the transportation method.
6. Click the “Book” button.

**Test Steps:**
1. Click the “Add driver’s license” field.
2. In the “Add driver’s license” form, enter the following data:

    - First name: Evgeniy
    - Last name: Petrov
    - Date of birth: 01.04.1976
    - License number: 0909123456

3. Click the “Add” button.
4. Click the “Payment method” field.
5. In the bank card form, enter the following data:

    - Card number: 463801983657
    - Security code: 76

6. Click the close (×) icon.
7. Click the "Book" button.

**Expected result:**  
- The booking button displays the text “Book”.
- After clicking the button, the “Car booked” confirmation window is displayed.

**Status:**  

Blocked

**Environment:**
- OS: MacOS Sonoma 15.2 (24C101)
- Browser: Firefox 134.0
- Screen resolution: 1920×1080

**Bug Report Link**

[Bug-report-010](../Bug-Reports/bugs/BR-010-booking-form-disabled-after-address-removal.md)