from selenium.webdriver.common.by import By


class LocatorsPersonalAccount:
    PERSONAL_ACCOUNT = (By.ID, "actionmenuaction-1")
    EXIT = (By.ID, "actionmenuaction-6")
    MENU = (By.CLASS_NAME, "usermenu")
    PREFERENCES = (By.ID, "actionmenuaction-5")
