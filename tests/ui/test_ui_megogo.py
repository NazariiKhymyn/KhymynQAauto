from modules.ui.page_objects.sing_in_page_megogo import SignInPageMegogo
import pytest
import requests


@pytest.mark.megogo
def test_check_incorrect_tittle_page():
    # creating a page object
    sign_in_page_megogo = SignInPageMegogo()

    # open page "https://megogo.net/ua"
    sign_in_page_megogo.go_to()

    # check https
    response = requests.get("https://megogo.net/ua")
    assert response.status_code == 200

    # close browser
    sign_in_page_megogo.close()


@pytest.mark.megogo
def test_check_tv_channels():
    # creating a page object
    sign_in_page_megogo = SignInPageMegogo()

    # open page "https://megogo.net/ua"

    sign_in_page_megogo.open_tv_channels()


@pytest.mark.megogo
def test_checking_selected_movies():
    # checking selected movies

    sing_in_page_megogo = SignInPageMegogo()

    sing_in_page_megogo.go_to()

    sing_in_page_megogo.open_selected_movies()
