from selenium.webdriver.common.by import By


class LocatorsPreferences:
    EDIT_INFORMATION = (By.LINK_TEXT, "Редактировать информацию")
    NOTIFICATION = (By.ID, "user-notifications")
