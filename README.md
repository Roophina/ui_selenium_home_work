# ui_selenium_home_work
[![Build Status](https://app.travis-ci.com/Roophina/ui_selenium_home_work.svg?branch=master)](https://app.travis-ci.com/Roophina/ui_selenium_home)


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
