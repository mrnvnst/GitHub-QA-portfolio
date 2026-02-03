### Объём и подход к тестированию

🇷🇺 | RU

#### Объём тестирования

В рамках проекта была протестирована следующая функциональность приложения:
- построение маршрута различными способами;
- выбор станции на карте;
- поведение карточек станции и маршрута;
- работа истории маршрутов;
- корректность отображения при смене ориентации экрана;
- работа приложения при отсутствии сети;
- события, зависящие от времени устройства.

#### Подход к тестированию

Тестирование проводилось вручную с использованием спроектированных чек-листов.
Основной фокус был сделан на функциональности, затронутой рефакторингом, а также на проверке ключевых пользовательских сценариев.

В рамках тестирования:

- выполнено функциональное тестирование изменений;
- проведено регрессионное тестирование основной функциональности;
- учтены мобильные особенности (ориентация экрана, сеть, прерывания);
- дефекты зафиксированы с указанием приоритета и серьёзности.

#### Тестовая среда

Конфигурация:

- Платформа: Android
- Устройство: Honor 8 (эмулятор)
- Версия ОС: Android 9.0
- Разрешение экрана: 1080×1920
- Диагональ экрана: 5.5"
- Инструмент: Android Studio Emulator
- Версия приложения: 3.6

---

### Scope and Testing Approach

🇬🇧 | EN

#### Testing Scope

The following application areas were covered during testing:

- route building using different input methods;
- station selection on the map;
- route and station cards behavior;
- route history handling;
- application behavior in portrait and landscape modes;
- offline scenarios and network interruptions;
- time-dependent events.

#### Testing Approach

Testing was performed manually using self-designed checklist-based testing.
The primary focus was on functionality affected by refactoring and verification of critical user flows.

The approach included:

- functional testing of updated features;
- regression testing of core functionality;
- consideration of mobile-specific scenarios (orientation changes, network state, interruptions);
- defect reporting with severity and priority assessment.

#### Test Environment

Configuration:

- Platform: Android
- Device: Honor 8 (emulator)
- OS version: Android 9.0
- Screen resolution: 1080×1920
- Screen size: 5.5"
- Tool: Android Studio Emulator
- Application version: 3.6