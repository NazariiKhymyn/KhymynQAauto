from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePageRozetka:
    PAHT = r"C:\\Users\\Fikeee\\KhymynQAauto"
    DRIVER_NAME = r"\\chromedriver.exe"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePageRozetka.PAHT + BasePageRozetka.DRIVER_NAME)
        )

    def close(self):
        self.driver.close()
