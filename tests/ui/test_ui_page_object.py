from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # creating a page object
    sign_in_page = SignInPage()

    # open page https://github.com/login
    sign_in_page.go_to()

    # we try to log in GitHub
    sign_in_page.try_login("page_objeck@gmail.com", "wrong password")

    # check the name of the page
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # close browser
    sign_in_page.close()
