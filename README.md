# Тесты для приложения "Курсы" (https://qacoursemoodle.innopolis.university/)
[![Build Status](https://app.travis-ci.com/Roophina/ui_selenium_home_work.svg?branch=master)](https://app.travis-ci.com/Roophina/ui_selenium_home)


Описание проекта:

1) Тесты на авторизацию: авторизация с валидными логином и паролем, авторизация с пустым логином, авторизация с пустым паролем, авторизация с неправильным логином

2) Тесты на редактирование данных пользователя: редактирование данных с заполнением обязательных полей, редактирование данных без заполнения обязательного поля

3) Тесты на добавление курса: создание курса с заполнением обязательных полей (в тесте реализовано удаление курса после создания), создание курса без заполнения обязательного поля


Локальная установка проекта:

1) Установить Python3 (оптимальная версия 3.9)

2) Установить PyCharm

3) Создать в PycharmProjects пустую директорию

4) Инициировать git (git init)

5) Скачать файлы из репозитория (git clone https://github.com/Roophina/ui_selenium_home_work)

6) Открыть проект

7) Установить пакеты из файла requirements.txt (pip install -r requirements.txt)



Отчеты при помощи Allure:

1) Установить локально Allure commandline application

2) Выполнить в терминале команду pytest --alluredir=allure_reports

3) Перезапустить PyCharm

4) Выполнить в терминале команду allure serve allure_reports

И/ИЛИ

1) Установить allure-pytest (pip install allure-pytest)

2) Созlать папку для загрузки временных результатов тестов (pytest --alluredir reposts)

3) Запустить тесты (python -m pytest tests путь к файлу\reposts)

4) Сформировать отчет: (allure serve путь к файлу\reposts)
