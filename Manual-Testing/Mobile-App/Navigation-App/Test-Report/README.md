### Отчет о тестировании

🇷🇺 | **RU** 

В ходе тестирования были проверены как изменения, внесённые в приложение,
так и ключевая существующая функциональность.

**Протестировано:**
- построение маршрута;
- выбор станции на карте;
- карточки станции, маршрута и детальной информации о маршруте;
- окно с историей маршрута;
- настройки приложения;
- работа приложения в альбомной и портретной ориентациях;
- использование жестов;
- геолокация;
- работа в онлайн и офлайн режимах;
- события, соответствующие времени, установленному на устройстве;
- установка и обновление приложение;
- работа при прерываниях.

**Тестовая документация:**
- для проверки требований, затронутых рефакторингом, был составлен чек-лист: [ссылка](../Checklists/functional-checklist-ru.csv)
- для проведения регрессионого тестирования составлен чек-лист: [ссылка](../Checklists/regression-checklist-ru.csv)
- по результатам тестирования по чек-листам составлены баг-репорты: [ссылка](../Bug-Reports/README.md)

**Баги:**

В рамках основного проекта было выполнено **42 проверки**, направленные на валидацию изменений после рефакторинга, и **109 проверок** по регрессионному чек-листу.
Из них **110 проверок завершились успешно**, **41 проверка завершилась неуспешно**, по результатам чего были заведены баг-репорты различной степени критичности.

**По результатам тестирования:**
- большинство пользовательских сценариев было успешно проверено;
- выявлены дефекты различной степени критичности;
- часть обнаруженных проблем требует исправления до релиза.

**Рекомендации:**

На основании результатов рекомендуется доработка приложения перед публикацией новой версии.

---

### Test Report

🇬🇧 | **EN** 

Testing covered both updated functionality and core application features.

**Tested features:**

- route construction;
- selecting a station on the map;
- station, route, and route details cards;
- the route history window;
- app settings;
- application functionality in landscape and portrait modes;
- gesture support;
- geolocation services;
- operation in online and offline modes;
- events tied to the device time settings;
- app installation and updates;
- handling interruptions.

**Test documentation:**

- a checklist was created to verify the requirements impacted by the refactoring: [link](../Checklists/functional-checklist-ru.csv)
- a checklist for conducting regression testing was prepared: [link](../Checklists/regression-checklist-ru.csv)
- bug reports were generated based on the checklist test results: [link](../Bug-Reports/README.md)

**Bugs:**

OWithin the main project, **42 test cases** were executed to validate changes after refactoring, and **109 test cases** were executed as part of regression testing.
As a result, **110 tests passed** and **41 tests failed**, leading to the creation of bug reports with different severity levels.

**Based on test execution results:**

- the majority of user scenarios were successfully verified;
- multiple defects of varying severity were identified;
- some issues should be fixed before releasing a new version.

**Recommendations:**

Based on the results, additional stabilization is recommended prior to release.