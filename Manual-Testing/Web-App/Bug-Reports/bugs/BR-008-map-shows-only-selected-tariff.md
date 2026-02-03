### BR-008 – На карте отображаются машины только выбранного тарифа

🇷🇺 | **RU** 

**Предусловия:**
- Перейти на тестовый стенд.
- Ввести в поле «Откуда»: «Хамовнический вал, 18».
- Ввести в поле «Куда»: «Усачева, 34».
- Выбрать режим «Свой».
- Выбрать вид транспорта «Каршеринг».
- Нажать на кнопку «Забронировать».

**Шаги воспроизведения:**
1. В селекторе выбора тарифа выбрать тариф «Походный».
2. Проверить расположение иконок машин на карте.
3. Навести курсор на иконки автомобилей.
4. Проверить плашки с маркой автомобиля.

**Ожидаемый результат:**  
На карте отображаются автомобили всех тарифов, например: BMW 750, Kia Rio, Porsche 911.

**Фактический результат:**  
На карте отображаются только автомобили выбранного тарифа «Походный» — Kia Rio.

**Серьёзность:** Критический  
**Приоритет:** Высокий  
**Статус:** Открыт

**Окружение:**
- Операционная система: macOS Sonoma 15.2 (24C101)
- Браузер: Firefox 134.0
- Разрешение экрана: 1920×1080

**Вложения:**  
- Скриншот:

    ![BR-008 Screenshot](../attachments/BR-008-map-shows-only-selected-tariff.gif)

---

### BR-008 – The map displays only cars of the selected tariff

🇬🇧 | **EN** 

**Preconditions:**
- Open the test environment.
- Enter “Khamovnichesky Val, 18” into the “From” field.
- Enter “Usacheva, 34” into the “To” field.
- Select the “Custom” travel mode.
- Select “Car sharing” as the transportation method.
- Click the “Book” button.

**Steps to reproduce:**
1. In the tariff selector, choose the “Hiking” tariff.
2. Observe the vehicles displayed on the map.
3. Hover over vehicle icons.
4. Check the car brand labels.

**Expected result:**  
Cars of all tariffs are displayed on the map, for example: BMW 750, Kia Rio, Porsche 911.

**Actual result:**  
Only cars of the selected “Hiking” tariff are displayed on the map — Kia Rio.

**Severity:** Critical

**Priority:** High

**Status:** Open

**Environment:**
- Operating System: macOS Sonoma 15.2 (24C101)
- Browser: Firefox 134.0
- Screen resolution: 1920×1080

**Attachments:**  
- Screenshot:

    ![BR-008 Screenshot](../attachments/BR-008-map-shows-only-selected-tariff.gif)