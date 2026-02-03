### BR-011 – Нажатие на кнопку «Забронировать» при незаполненном способе оплаты открывает окно «Машина забронирована»

🇷🇺 | **RU** 

**Предусловия:**
- Перейти на тестовый стенд.
- Ввести в поле «Откуда»: «Хамовнический вал, 18».
- Ввести в поле «Куда»: «Усачева, 34».
- Выбрать режим «Свой».
- Выбрать вид транспорта «Каршеринг».
- Нажать на кнопку «Забронировать».
- В селекторе выбора тарифа выбрать тариф «Походный».

**Шаги воспроизведения:**
1. Нажать на поле «Добавить права».
2. В форме добавления прав ввести данные:

    - Имя: Евгений
    - Фамилия: Петров
    - Дата рождения: 01.04.1976
    - Номер: 0909123456

3. В окне «Способ оплаты» нажать на кнопку закрытия (крестик), не добавляя карту.
4. Нажать на кнопку «Забронировать».

**Ожидаемый результат:**  
- На кнопке отображается текст «Добавить оплату и забронировать».
- При нажатии на кнопку открывается окно «Добавление карты».

**Фактический результат:**  
- На кнопке отображается текст «Добавить оплату и забронировать» и дополнительный текст:
«Маршрут составит n км и займет n мин».
- При нажатии на кнопку открывается окно «Машина забронирована».

**Серьёзность:** Критический
**Приоритет:** Высокий  
**Статус:** Открыт

**Окружение:**
- Операционная система: macOS Sonoma 15.2 (24C101)
- Браузер: Firefox 134.0
- Разрешение экрана: 1920×1080

**Вложения:**  
- Скриншот:

    ![BR-011 Screenshot](../attachments/BR-011-booking-without-payment.gif)

---

### BR-011 – Clicking the “Book” button without a selected payment method opens the “Car booked” window.

🇬🇧 | **EN** 

**Preconditions:**
- Open the test environment.
- Enter “Khamovnichesky Val, 18” into the “From” field.
- Enter “Usacheva, 34” into the “To” field.
- Select the “Custom” travel mode.
- Select “Car sharing” as the transportation method.
- Click the “Book” button.
- In the tariff selector, choose the “Hiking” tariff.

**Steps to reproduce:**
1. Click the “Add driver’s license” field.
2. In the add driver’s license form, enter:

- First name: Evgeniy
- Last name: Petrov
- Date of birth: 01.04.1976
- License number: 0909123456

3. Close the “Payment method” window without adding a card.
4. Click the “Book” button.

**Expected result:**  
- The button displays the text “Add payment method and book”.
- Clicking the button opens the “Add card” window.

**Actual result:**  
- The button displays the text “Add payment method and book” along with:
“The route will be n km and take n minutes”.
- Clicking the button opens the “Car booked” window.

**Severity:** Critical

**Priority:** High

**Status:** Open

**Environment:**
- Operating System: macOS Sonoma 15.2 (24C101)
- Browser: Firefox 134.0
- Screen resolution: 1920×1080

**Attachments:**  
- Screenshot:

    ![BR-011 Screenshot](../attachments/BR-011-booking-without-payment.gif)
