from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pytest

website = "https://the-internet.herokuapp.com/"

@pytest.mark.web
def test_example(selenium):
    selenium.get(website)

@pytest.mark.web
def test_app_loads():
    driver = webdriver.Chrome()  
    driver.get(website) 
    assert "The Internet" in driver.title
    driver.quit() 
