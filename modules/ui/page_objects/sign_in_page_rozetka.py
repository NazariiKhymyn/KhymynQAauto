from modules.ui.page_objects.base_page_rozetka import BasePageRozetka
from selenium.webdriver.common.by import By


class SingInPageRozetka(BasePageRozetka):
    URL = "https://rozetka.com.ua"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SingInPageRozetka.URL)

    # check wrong password
    def try_wrong_password(self, user_email_address, password):
        button_user_elem = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[3]/rz-user/button",
        )

        # emulate click left button mouse
        button_user_elem.click()

        # we find the field in which we will enter the email
        email_elem = self.driver.find_element(By.ID, "auth_email")

        # enter correct email address
        email_elem.send_keys(user_email_address)

        # we find the field in which we will enter the password
        pass_elem = self.driver.find_element(By.ID, "auth_pass")

        # enter correct password
        pass_elem.send_keys(password)

        # find button save me
        button_save_user_elem = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/form/fieldset/div[3]/label",
        )

        # emulate click left button mouse
        button_save_user_elem.click()

    # add the product to the card
    def add_product_is_in_the_card(self, product_name):
        # find the search field
        fild_product_search = self.driver.find_element(By.NAME, "search")

        # clear field search
        fild_product_search.clear()

        # enter the product for search
        fild_product_search.send_keys(product_name)

        button_product_search = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/button",
        )

        button_product_search.click()
        # shopping cart search for this product
        button_card = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/div/rz-category/div/main/rz-catalog/div/div/section/rz-grid/ul/li[1]/rz-catalog-tile/app-goods-tile-default/div/div[2]/div[4]/div[2]/app-buy-button/button",
        )

        button_card.click()
        # shopping cart search for all products
        button_card_oll = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[7]/rz-cart/button",
        )

        button_card_oll.click()

    # checking the selection of mobile phones
    def checking_the_selection_of_mobile_phones(self):
        self.driver.find_element(
            By.LINK_TEXT,
            "Смартфони, ТВ і електроніка",
        ).click()

        self.driver.implicitly_wait(2)

        self.driver.find_element(
            By.LINK_TEXT,
            "Мобільні телефони",
        ).click()

    # check title page
    def check_title(self, expected_title):
        return self.driver.title == expected_title
