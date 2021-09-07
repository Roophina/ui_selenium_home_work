from selenium.webdriver.common.by import By


class LocatorsLoginPage:
    LOGIN = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    BUTTON_ENTER = (By.ID, "loginbtn")
    LOGIN_ERROR_MESSAGE = (By.ID, "loginerrormessage")
