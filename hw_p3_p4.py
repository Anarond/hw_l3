import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    opts = Options()

    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver

    driver.quit()


def test_selenium_web(driver):
    url1 = "https://www.google.com/"
    url2 = "https://github.com/"
    driver.get(url1)
    assert driver.title == "Google"
    assert driver.current_url == url1
    driver.get(url2)
    assert (
        driver.title == "GitHub · Change is constant. GitHub keeps you ahead. · GitHub"
    )
    assert driver.current_url == url2
