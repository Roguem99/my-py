from selenium import webdriver
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

# def test_ap_loads():
#     driver = webdriver.Chrome()
#     driver.get("https://google.com")
#     assert "My Application" in driver.title
#     driver.quit()