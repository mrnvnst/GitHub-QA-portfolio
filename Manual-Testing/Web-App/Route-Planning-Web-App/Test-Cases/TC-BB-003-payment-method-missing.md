### ID: TC-BB-003

🇷🇺 | **RU** 

#### Название :
Проверка логики кнопки бронирования при заполнении обязательных полей и адресов, при незаполненном способе оплаты.

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
4. Нажать на кнопку "Забронировать".

**Ожидаемый результат:**  
- Текст на кнопке: «Добавить оплату и забронировать».
- При нажатии на кнопку открывается окно «Добавление карты».

**Статус:**

 Failed

**Окружение:**
- ОС: MacOS Sonoma 15.2 (24C101)  
- Браузер: Firefox 134.0
- Разрешение экрана: 1920×1080

**Ссылка на баг-репорт:**

[Bug-report-011](../Bug-Reports/bugs/BR-011-booking-without-payment.md)

---

### ID: TC-BB-003

🇬🇧 | **EN** 

**Title:**
Verify booking button logic when all required fields and addresses are filled but the payment method is not selected.

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
4. Click the "Book" button.

**Expected result:**  
- The booking button displays the text “Add payment method and book”.
- After clicking the button, the the “Add card” window is displayed.

**Status:**  

Failed

**Environment:**
- OS: MacOS Sonoma 15.2 (24C101)
- Browser: Firefox 134.0
- Screen resolution: 1920×1080

**Bug Report Link**

[Bug-report-011](../Bug-Reports/bugs/BR-011-booking-without-payment.md)