from modules.ui.page_objects.sign_in_page_rozetka import SingInPageRozetka
import pytest
import requests


@pytest.mark.rozetka
def test_check_incorrect_username_page():
    # creating a page object
    sign_in_page_rozetka = SingInPageRozetka()

    # open page "https://rozetka.com.ua"
    sign_in_page_rozetka.go_to()

    # we try to log in GitHub
    sign_in_page_rozetka.try_wrong_password("mizuna@ukr.net", "wrong password")

    # check https
    response = requests.get("https://rozetka.com.ua/ua/")
    assert response.status_code == 200

    # close browser
    sign_in_page_rozetka.close()


@pytest.mark.rozetka
def test_check_product_is_in_the_card():
    # creating a page object
    sign_in_page_rozetka = SingInPageRozetka()

    # open page "https://rozetka.com.ua"
    sign_in_page_rozetka.go_to()

    # add the product to the basket for checking
    sign_in_page_rozetka.add_product_is_in_the_card("ноутбук lenovo")

    # check https
    response = requests.get(
        "https://rozetka.com.ua/ua/search/?text=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA+lenovo+legion+5"
    )
    assert response.status_code == 200

    # close browser
    sign_in_page_rozetka.close()


@pytest.mark.rozetka
def test_checking_the_selection_of_mobile_phones():
    # creating a page object
    sign_in_page_rozetka = SingInPageRozetka()

    # open page "https://rozetka.com.ua"
    sign_in_page_rozetka.go_to()

    sign_in_page_rozetka.checking_the_selection_of_mobile_phones()

    # check https mobile phones
    response = requests.get("https://rozetka.com.ua/ua/mobile-phones/c80003/")
    assert response.status_code == 200

    # close browser
    sign_in_page_rozetka.close()
