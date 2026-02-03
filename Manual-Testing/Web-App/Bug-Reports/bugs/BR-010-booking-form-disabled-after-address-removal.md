### BR-010 – При удалении адресов из полей «Откуда» / «Куда» форма бронирования становится недоступна.

🇷🇺 | **RU** 

**Предусловия:**
- Перейти на тестовый стенд.
- Ввести в поле «Откуда»: «Хамовнический вал, 18».
- Ввести в поле «Куда»: «Усачева, 34».

**Шаги воспроизведения:**
1. Выбрать режим «Свой».
2. Выбрать вид транспорта «Каршеринг».
3. Нажать на кнопку «Забронировать».
4. Удалить адрес из поля «Откуда» или «Куда».

**Ожидаемый результат:**  
Форма бронирования остаётся активной и доступной для взаимодействия.
Пользователь может продолжить работу с формой бронирования.

**Фактический результат:**  
Форма бронирования закрывается и становится недоступной для взаимодействия.
Под полем с удалённым адресом отображается сообщение об ошибке:
«Введите адрес».

**Серьёзность:** Блокирующий

**Приоритет:** Высокий  

**Статус:** Открыт

**Окружение:**
- Операционная система: macOS Sonoma 15.2 (24C101)
- Браузер: Firefox 134.0
- Разрешение экрана: 1920×1080

**Вложения:**  
- Скриншот:

    ![BR-010 Screenshot](../attachments/BR-010-booking-form-disabled-after-address-removal.gif)

---

### BR-010 – The booking form becomes unavailable after removing addresses from the “From” / “To” fields.

🇬🇧 | **EN** 

**Preconditions:**
- Open the test environment.
- Enter “Khamovnichesky Val, 18” into the “From” field.
- Enter “Usacheva, 34” into the “To” field.

**Steps to reproduce:**
1. Select the “Custom” travel mode.
2. Select “Car sharing” as the transportation method.
3. Click the “Book” button.
3. Remove the address from the “From” or “To” field.

**Expected result:**  
The booking form remains active and available for interaction.
The user can continue working with the booking form.

**Actual result:**  
The booking form closes and becomes unavailable.
An error message “Enter address” is displayed under the cleared field.

**Severity:** Blocked

**Priority:** High

**Status:** Open

**Environment:**
- Operating System: macOS Sonoma 15.2 (24C101)
- Browser: Firefox 134.0
- Screen resolution: 1920×1080

**Attachments:**  
- Screenshot:

    ![BR-010 Screenshot](../attachments/BR-010-booking-form-disabled-after-address-removal.gif)
    
