
Continuous Integration & Continuous Delivery
Formulation
The first lab task requires writing a simple web application that provides the user with a set of operations on the Person entity. For this application, automate the process of building, testing, and releasing on Heroku.

The application must implement the API:

GET /persons/{personId}– information about a person;
GET /persons– information on all people;
POST /persons– creating a new record about a person;
PATCH /persons/{personId}– updating an existing record about a person;
DELETE /persons/{personId}– deleting a record about a person.
API description in OpenAPI format.

Requirements
The original project is stored on Github. Use only Github Actions for building .
Requests/responses must be in JSON format.
If the record by id is not found, then return HTTP status 404 Not Found.
When creating a new record about a person (POST /person method), return HTTP status 201 Created with an empty body and Header Location: /api/v1/persons/{personId}, where personIdis the id of the created record.
The application must contain 4-5 unit tests for the implemented operations.
The application must be wrapped in Docker.
Deploy to Heroku using GitHub Actions, use Docker for deployment. You cannot use Heroku CLI or webhooks for deployment.
In build.yml add steps for assembly, running unit tests and deploying to Heroku.
The application must use a database to store records.
In [inst][heroku] Lab1.postman_environment.json replace the value baseUrlwith the address of the deployed service on Heroku.
Explanations
Example Kotlin/Spring applications.
For local development, you can use Postgres in docker, for this you need to run docker compose up -d, a container with Postgres 13 will be started, a database personsand a user will be created program:test.
After successful deployment to Heroku, integration tests are run via newman. Integration tests can be tested locally by importing the collection lab1.postman_collection.json ]) and environment [local] lab1.postman_environment.json into Postman .
To find the right build tool, use Github Marketplace .
An explanation of how Heroku works .
To connect a DB to Heroku, go to the Resources section via Dashboard and Add-onslook for Heroku Postgres in the block. To get the address, user and password, go to the DB itself and select the Settings -> section Database Credentials.
❗Heroku does not allow new users to register, so use a VPN to register.
Accepting the task
When you receive a task, a fork of that repository is created for your user.
Once all tests complete successfully, the Github Classroom Dashboard will indicate that the tests have run successfully.
❗️Since the end of November, Heroku will remove the Free Plan , only paid subscriptions will remain. In this regard, the deadline for submitting LR #1 is November 10.



# Лабораторная работа #1

![GitHub Classroom Workflow](../../workflows/GitHub%20Classroom%20Workflow/badge.svg?branch=master)

## Continuous Integration & Continuous Delivery

### Формулировка

В рамках первой лабораторной работы требуется написать простейшее веб приложение, предоставляющее пользователю набор
операций над сущностью Person. Для этого приложения автоматизировать процесс сборки, тестирования и релиза на Heroku.

Приложение должно реализовать API:

* `GET /persons/{personId}` – информация о человеке;
* `GET /persons` – информация по всем людям;
* `POST /persons` – создание новой записи о человеке;
* `PATCH /persons/{personId}` – обновление существующей записи о человеке;
* `DELETE /persons/{personId}` – удаление записи о человеке.

[Описание API](person-service.yaml) в формате OpenAPI.

### Требования

* Исходный проект хранится на Github. Для сборки использовать
  _только_ [Github Actions](https://docs.github.com/en/actions).
* Запросы / ответы должны быть в формате JSON.
* Если запись по id не найдена, то возвращать HTTP статус 404 Not Found.
* При создании новой записи о человека (метод POST /person) возвращать HTTP статус 201 Created с пустым телом и
  Header `Location: /api/v1/persons/{personId}`, где `personId` – id созданной записи.
* Приложение должно содержать 4-5 unit-тестов на реализованные операции.
* Приложение должно быть завернуто в Docker.
* Деплой на Heroku реализовать средствами GitHub Actions, для деплоя использовать docker. Для деплоя _нельзя_
  использовать Heroku CLI или webhooks.
* В [build.yml](.github/workflows/classroom.yml) дописать шаги на сборку, прогон unit-тестов и деплой на Heroku.
* Приложение должно использовать БД для хранения записей.
* В [[inst][heroku] Lab1.postman_environment.json](postman/%5Binst%5D%5Bheroku%5D%20Lab1.postman_environment.json)
  заменить значение `baseUrl` на адрес развернутого сервиса на Heroku.

### Пояснения

* [Пример](https://github.com/Romanow/person-service) приложения на Kotlin / Spring.
* Для локальной разработки можно использовать Postgres в docker, для этого нужно запустить `docker compose up -d`,
  поднимется контейнер с Postgres 13, будет создана БД `persons` и пользователь `program:test`.
* После успешного деплоя на Heroku, через newman запускаются интеграционные тесты. Интеграционные тесты можно проверить
  локально, для этого нужно импортировать в Postman
  коллекцию [lab1.postman_collection.json](postman/%5Binst%5D%20Lab1.postman_collection.json)]) и
  environment [[local] lab1.postman_environment.json](postman/%5Binst%5D%5Blocal%5D%20Lab1.postman_environment.json).
* Для поиска нужного инструмента для сборки используется [Github Marketplace](https://github.com/marketplace).
* Пояснение как работает [Heroku](https://devcenter.heroku.com/articles/how-heroku-works).
* Для подключения БД на Heroku заходите через Dashboard в раздел Resources и в блоке `Add-ons` ищете Heroku Postgres.
  Для получения адреса, пользователя и пароля переходите в саму БД и выбираете раздел `Settings`
  -> `Database Credentials`.
* ❗Heroku не позволяет регистрировать новых пользователей, поэтому для регистрации используйте VPN.

### Прием задания

1. При получении задания у вас создается fork этого репозитория для вашего пользователя.
2. После того как все тесты успешно завершатся, в Github Classroom на Dashboard будет отмечен успешный прогон тестов.
3. ❗️С конца
   ноября [Heroku убирает Free Plan](https://help.heroku.com/RSBRUH58/removal-of-heroku-free-product-plans-faq),
   останутся только платные подписки. В связи с этим, дедлайн по сдаче ЛР #1 10 ноября. 
