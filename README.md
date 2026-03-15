### Портфолио проектов по тестированию ПО

🇷🇺 | **RU**

Здесь собраны результаты практического опыта ручного тестирования веб- и мобильных приложений – примеры автоматизированного тестирования будут добавлены в этот репозиторий в скором времени.

В каждом проекте отражен полный цикл тестирования: от анализа требований к ПО до формирования отчёта о тестировании и составления рекомендаций по готовности ПО к релизу.

Работы ориентированы на структурированный подход к тестированию, применении методик тест-дизайна, соблюдении API-контракта, проверку бизнес-логики и документировании дефектов.

Все проекты представлены на русском и английском языках.

---

<details>
<summary><b>Проекты по ручному тестированию</b></summary>

<br>

#### 1. [Тестирование веб-приложения для построения городских маршрутов](https://github.com/mrnvnst/GitHub-QA-portfolio/tree/main/Manual-Testing/Web-App/Route-Planning-Web-App)

В рамках проекта выполнено функциональное и регрессионное тестирование веб-интерфейса.

**Основные задачи проекта:**

- анализ требований и пользовательских сценариев;
- составление чек-листов;
- проверка UI/UX;
- тестирование граничных значений и негативных сценариев;
- оформление баг-репортов;
- подготовка тестового отчёта.


#### 2. [Тестирование мобильного навигационного Android-приложения](https://github.com/mrnvnst/GitHub-QA-portfolio/tree/main/Manual-Testing/Mobile-App/Navigation-App)

Проект посвящён тестированию Android-приложения.

**Выполнено:**

- анализ пользовательских сценариев;
- тестирование навигации и логики экранов;
- проверка валидации данных;
- тестирование негативных сценариев;
- подготовка тестовой документации;
- документирование дефектов.


#### 3. [Тестирование веб-приложения сервиса аренды самокатов](https://github.com/mrnvnst/GitHub-QA-portfolio/tree/main/Manual-Testing/Web-App/Scouter-Rental-Web-App)

Проект посвящён тестированию веб-приложения сервиса аренды самокатов.

**В рамках проекта:**

- проведён анализ требований для экрана «Статус заказа»;
- проанализированы требования к backend-функциональности;
- разработаны чек-листы;
- подготовлены тестовые данные для проверки валидации полей формы оформления заказа;
- применены техники тест-дизайна (классы эквивалентности, граничные значения);
- проведено функциональное и UI-тестирование веб-интерфейса, проверена валидация входных параметров;
- выполнено кроссбраузерное тестирование;
- выявлены и задокументированы дефекты различной степени критичности;
- подготовлен тестовый отчёт по результатам тестирования.


#### 4. [Тестирование мобильного приложения курьера сервиса аренды самокатов](https://github.com/mrnvnst/GitHub-QA-portfolio/tree/main/Manual-Testing/Mobile-App/Scouter-Rental-Courier-App)

Проект посвящён тестированию мобильного приложения курьера, используемого для обработки и выполнения заказов сервиса аренды самокатов.

**В рамках проекта:**

- проанализированы требования к функциональности приложения;
- разработаны тест-кейсы для проверки нотификаций и работы приложения;
- протестирована работа приложения при отсутствии интернет-соединения;
- проведён прогон тестов в TestIT;
- выявлены дефекты в работе push-уведомлений и обработке сетевых ошибок;
- оформлены баг-репорты в Яндекс Трекере и Jira;
- подготовлены выводы по результатам тестирования мобильного приложения.

Проекты [№3](#3-тестирование-веб-приложения-сервиса-аренды-самокатов) и [№4](#4-тестирование-мобильного-приложения-курьера-сервиса-аренды-самокатов) демонстрируют тестирование различных уровней системы сервиса доставки:

- пользовательского веб-приложения;
- мобильного приложения курьера;
- API-сервисов.

В совокупности они отражают тестирование **сквозного (end-to-end) пользовательского сценария**: создание заказа, его обработку, выполнение доставки и отслеживание статуса.


#### 5. [Тестирование API сервиса доставки](https://github.com/mrnvnst/GitHub-QA-portfolio/tree/main/Manual-Testing/API)

Проект демонстрирует ручное и частично автоматизированное тестирование REST API.

**В рамках проекта:**

- проанализированы требования к backend-функциональности;
- разработаны чек-листы с применением техник тест-дизайна (КЭ, ГЗ, негативные сценарии);
- протестированы эндпоинты;
- проверена валидация входных параметров и корректность HTTP-статусов;
- выполнено тестирование бизнес-логики;
- оформлены баг-репорты
- подготовлен итоговый отчёт с метриками дефектов и выводом о готовности продукта к релизу.


#### Инструменты

- Postman (Requests, Scripts, Collections, Environment, JSON, XML)
- Chrome DevTools
- Swagger, apiDoc
- Git, GitHub
- TestIT
- Jira
- Яндекс Трекер
- Android Studio (эмулятор)
- SQL

</details>

<details>
<summary><b>Проекты по автоматизированному тестированию</b></summary>

<br>

#### 1. [Юнит-тестирование веб-приложения для создания бургеров](https://github.com/mrnvnst/GitHub-QA-portfolio/tree/main/Automation-Testing/Unit-Tests)

Проект посвящён разработке юнит-тестов для приложения, которое позволяет пользователю собирать и заказывать бургеры.

**В рамках проекта:**

- разработаны юнит-тесты для класса `Burger`;
- протестированы операции добавления, удаления и перемещения ингредиентов;
- проверен расчёт стоимости заказа и формирование чека;
- применены фикстуры `pytest` и параметризация тестов;
- использованы mock-объекты для изоляции тестируемых компонентов;
- достигнуто **100% покрытие тестируемого класса**;
- сформирован HTML-отчёт о покрытии (`pytest-cov`).

#### 2. [Автоматизированное тестирование REST API сервиса оформления заказов](https://github.com/mrnvnst/GitHub-QA-portfolio/tree/main/Automation-Testing/API)

Проект демонстрирует разработку автотестов для REST API сервиса регистрации пользователей, авторизации и оформления заказов.

**В рамках проекта:**

- реализованы API-тесты для эндпоинтов регистрации пользователя, авторизации и создания заказа;
- применены позитивные и негативные сценарии;
- реализована генерация тестовых данных;
- использованы фикстуры pytest;
- реализована параметризация тестов;
- подготовлен отчёт о выполнении тестов в Allure;
- оформлен баг-репорт для выявленного дефекта.

#### 3. [Автоматизированное UI-тестирование веб-приложения конструктора бургеров](https://github.com/mrnvnst/GitHub-QA-portfolio/tree/main/Automation-Testing/UI-Tests)

Проект демонстрирует автоматизацию пользовательского интерфейса веб-приложения.

Тесты реализованы на **Python** с использованием **pytest** и **Selenium WebDriver**.  
Для построения архитектуры тестов применяется паттерн **Page Object Model (POM)**.  
Результаты выполнения тестов визуализируются в **Allure Report**.

**В рамках проекта:**

- реализованы UI-автотесты для ключевых пользовательских сценариев;
- протестирована основная функциональность конструктора бургеров;
- проверена работа раздела «Лента заказов»;
- реализована проверка всплывающих окон интерфейса;
- протестировано добавление ингредиентов в заказ и обновление счётчиков;
- выполнено кроссбраузерное тестирование (Chrome, Firefox);
- реализована архитектура автотестов с использованием Page Object Model;
- подготовлен отчёт о выполнении тестов в Allure.


#### Инструменты

- Python
- Pytest
- Pytest-cov
- Requests
- Allure Report
- Faker
- Selenium WebDriver
- Page Object Model (POM)
- webdriver-manager

</details>


---

### Software Testing Portfolio

🇬🇧 | **EN**

This section contains the results of practical experience in manual testing of web and mobile applications. Examples of automated testing will be added to this repository in the near future.

Each project reflects a complete testing lifecycle — from software requirements analysis to preparation of a test summary report and release readiness recommendations.

The work is based on a structured testing approach, API contract validation, business logic verification, and proper defect documentation.

All projects are available in both Russian and English.

---

<details>
<summary><b>Manual Testing Projects</b></summary>

<br>

#### 1. [Urban Route Planning Web Application Testing](https://github.com/mrnvnst/GitHub-QA-portfolio/tree/main/Manual-Testing/Web-App/Route-Planning-Web-App)

The project includes functional and regression testing of a web application.

**Scope of work:**

- requirements and user flow analysis;
- checklist design;
- UI/UX verification;
- boundary and negative testing;
- structured bug reporting;
- preparation of a test summary report.


#### 2. [Android Navigation Application Testing](https://github.com/mrnvnst/GitHub-QA-portfolio/tree/main/Manual-Testing/Mobile-App/Navigation-App)

The project demonstrates Android application testing.

**Performed activities:**

- user scenario analysis;
- navigation flow validation;
- input validation testing;
- negative testing;
- test documentation preparation;
- defect reporting.


#### 3. [Scooter Rental Web Application Testing](https://github.com/mrnvnst/GitHub-QA-portfolio/tree/main/Manual-Testing/Web-App/Scouter-Rental-Web-App)

This project focuses on testing a customer-facing web application for a scooter rental service.

**Within the project:**

- requirements for the **“Order Status”** screen were analyzed;
- backend-related functional requirements were reviewed;
- checklists were designed based on the requirements;
- test data for **order form validation** was prepared;
- test design techniques were applied (Equivalence Classes, Boundary Value Analysis);
- functional and UI testing of the web interface was performed, including validation of input parameters;
- cross-browser testing was conducted;
- defects of different severity levels were identified and documented;
- a final **test report** summarizing the testing results was prepared.


#### 4. [Scooter Rental Courier Mobile Application Testing](https://github.com/mrnvnst/GitHub-QA-portfolio/tree/main/Manual-Testing/Mobile-App/Scouter-Rental-Courier-App)

This project focuses on testing a courier mobile application used to process and complete scooter rental orders.

**Within the project:**

- functional requirements for the mobile application were analyzed;
- test cases were designed to verify **notifications and application behavior**;
- application behavior was tested under **no internet connection conditions**;
- test execution was performed in **TestIT (Test Management System)**;
- defects related to **push notifications and network error handling** were identified;
- bug reports were documented in **Yandex Tracker and Jira**;
- testing results and conclusions for the mobile application were prepared.

Projects [#3](#3-scooter-rental-web-application-testing) and [#4](#4-scooter-rental-courier-mobile-application-testing) demonstrate testing of different layers of a delivery platform:

- customer web application
- courier mobile application
- backend API services.

Together they represent testing of a **complete end-to-end workflow**: order creation, processing, delivery, and status tracking.

#### 5. [Grocery Delivery Service API Testing](https://github.com/mrnvnst/GitHub-QA-portfolio/tree/main/Manual-Testing/API)

This project demonstrates manual and partially automated REST API testing.

**The project includes:**

- backend requirements analysis;
- checklist design using test design techniques (BVA, equivalence partitioning, negative scenarios);
- endpoint testing (Kits, Fast Delivery, Basket);
- input validation and HTTP status verification;
- business logic validation;
- enterprise-style defect documentation;
- defect metrics and release readiness conclusion.


#### Tools

- Postman (Requests, Scripts, Collections, Environment, JSON, XML)
- Chrome DevTools
- Swagger, apiDoc
- Git, GitHub
- TestIT
- Jira
- Yandex Tracker
- Android Studio (emulator)
- SQL

</details>

<details>
<summary><b>Test Automation Projects</b></summary>

<br>

### Automation Testing Projects

#### 1. [Automated Testing of Backend Logic for a Burger Builder Web Application](https://github.com/mrnvnst/GitHub-QA-portfolio/tree/main/Automation-Testing/Stellar-Burgers)

This project demonstrates automated unit testing of the backend logic for the **Stellar Burgers** application.

The tests validate the functionality of the `Burger` class responsible for burger composition, ingredient management, and price calculation.

**Project highlights:**

- unit tests implemented for the `Burger` class;
- testing ingredient addition, removal, and reordering;
- verification of price calculation and receipt generation;
- usage of `pytest` fixtures and parameterized tests;
- use of mock objects to isolate dependencies;
- **100% test coverage achieved**;
- HTML coverage report generated with `pytest-cov`.

#### 2. [Automated Testing of Order Processing REST API](https://github.com/mrnvnst/GitHub-QA-portfolio/tree/main/Automation-Testing/API)

This project demonstrates automated testing of a REST API responsible for user registration, authentication, and order creation.

**Within the project:**

- API tests were implemented for user registration, login, and order creation endpoints;
- positive and negative test scenarios were implemented;
- dynamic test data generation was used;
- pytest fixtures and parameterization were applied;
- Allure reports were generated for test execution results;
- a defect in the order creation endpoint was identified.

#### 3. [Automated UI Testing of a Burger Builder Web Application](https://github.com/mrnvnst/GitHub-QA-portfolio/tree/main/Automation-Testing/UI-Automation-Burger-Builder)

This project demonstrates automated UI testing of a web application.

Tests are implemented in **Python** using **pytest** and **Selenium WebDriver**.  
The test architecture follows the **Page Object Model (POM)** design pattern.  
Test execution results are visualized using **Allure Report**.

**Project scope includes:**

- implementation of UI automated tests for key user scenarios;
- testing of core burger builder functionality;
- validation of the **Order Feed** section behavior;
- verification of modal windows and interface interactions;
- testing ingredient addition and counter updates;
- cross-browser testing (Chrome, Firefox);
- implementation of a Page Object Model test architecture;
- generation of test execution reports with Allure.


#### Tools

- Python
- Pytest
- Pytest-cov
- Requests
- Allure Report
- Faker
- Selenium WebDriver
- Page Object Model (POM)
- webdriver-manager

</details>
