from selenium.webdriver.common.by import By


class LocatorsCourseManagementPage:
    CREATE_NEW_COURSE = (By.LINK_TEXT, "Создать новый курс")
    SEARCH = (By.NAME, "search")
    SEARCH_BUTTON = (By.XPATH, "//*[contains(@class,'icon fa fa-search fa-fw')]")
    SEARCH_RESULT = (
        By.XPATH,
        "//*[contains(@class,'listing-pagination-totals text-muted')]",
    )
    DELETE = (By.XPATH, "//*[contains(@class,'icon fa fa-trash fa-fw')]")
