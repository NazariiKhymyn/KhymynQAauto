from modules.ui.page_objects.base_page_megogo import BasePageMegogo
from selenium.webdriver.common.by import By


class SignInPageMegogo(BasePageMegogo):
    URL = "https://megogo.net/ua"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPageMegogo.URL)

    def check_title(self, expected_title):
        return self.driver.title == expected_title

    def open_tv_channels(self):
        self.driver.get(SignInPageMegogo.URL)

        find_elm_tv_channels = self.driver.find_element(
            By.XPATH,
            "/html/body/div/div[4]/header/div[2]/div/div/div[2]/nav/ul/li[1]/a",
        )
        find_elm_tv_channels.click()

    def open_selected_movies(self):
        open_elem_I_see = self.driver.find_element(By.LINK_TEXT, "Я дивлюся")

        open_elem_I_see.click()
