from selenium.webdriver.common.by import By


class LocatorsCourseEditPage:
    FULL_NAME = (By.ID, "id_fullname")
    SHORT_NAME = (By.ID, "id_shortname")
    SAVE_AND_RETURN = (By.ID, "id_saveandreturn")
    ERROR_SHORT_NAME = (By.ID, "id_error_shortname")
