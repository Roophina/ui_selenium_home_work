from selenium.webdriver.common.by import By


class LocatorsEditInformation:
    CITY = (By.ID, "id_city")
    BUTTON_UPDATE_PROFILE = (By.ID, "id_submitbutton")
    EMAIL = (By.ID, "id_email")
    ERROR_EMAIL = (By.ID, "id_error_email")
