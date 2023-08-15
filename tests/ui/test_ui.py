import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # creating an object to control the browser
    driver = webdriver.Chrome(
        service=Service(r"C:\\Users\\Користувач\\KhymynQAauto" + r"\\chromedriver.exe")
    )

    # open the page https://github.com/login
    driver.get("https://github.com/login")

    # find the field in which we will enter incorrect data
    login_elem = driver.find_element(By.ID, "login_field")

    # enter incorrect data
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")

    # find the field in which we will enter incorrect password
    pass_elem = driver.find_element(By.ID, "password")

    # enter incorrect password
    pass_elem.send_keys("wrong password")

    # find button sing in
    btn_elem = driver.find_element(By.NAME, "commit")

    # emulate a click with the left mouse button
    btn_elem.click()

    # check the name of the page
    assert driver.title == "Sign in to GitHub · GitHub"

    # close browser
    driver.close()