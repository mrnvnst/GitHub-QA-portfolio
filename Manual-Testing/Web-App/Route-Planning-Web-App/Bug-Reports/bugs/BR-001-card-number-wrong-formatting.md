### BR-001 – Система не проставляет пробелы автоматически при заполнении поля «Номер карты» валидными данными

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
1. Нажать на поле «Способ оплаты».
2. В форме добавления карты ввести данные:
    - Номер карты: 463801983657
3. Снять фокус с поля «Номер карты».

**Ожидаемый результат:**  
Система автоматически проставляет пробелы в номере карты, и в поле отображается значение:
4638 0198 3657.

**Фактический результат:**  
Номер карты отображается без пробелов:
463801983657.

**Серьёзность:** Низкий  
**Приоритет:** Стандартный  
**Статус:** Открыт

**Окружение:**
- Операционная система: macOS Sonoma 15.2 (24C101)
- Браузер: Firefox 134.0
- Разрешение экрана: 1920×1080

**Вложения:**  
- Скриншот:

    ![BR-001 Screenshot](../attachments/BR-001-card-number-formatting.png)

---

### BR-001 – The system does not automatically insert spaces when valid data is entered into the “Card number” field

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
1. Click the “Payment method” field.
2. In the add card form, enter:
    - Card number: 463801983657
3. Remove focus from the “Card number” field.

**Expected result:**  
The system automatically inserts spaces in the card number field, and the value is displayed as:
4638 0198 3657.

**Actual result:**  
The card number is displayed without spaces:
463801983657.

**Severity:** Low

**Priority:** Standart

**Status:** Open

**Environment:**
- Operating System: macOS Sonoma 15.2 (24C101)
- Browser: Firefox 134.0
- Screen resolution: 1920×1080

**Attachments:**  
- Screenshot:

    ![BR-001 Screenshot](../attachments/BR-001-card-number-formatting.png)
    
