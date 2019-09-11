import os
from datetime import datetime

import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def now():
    return datetime.now().strftime("%m/%d/%Y-%H:%M:%S")


def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="chrome", help="Type in browser type")
    parser.addoption("--url", action="store", default="https://www.facebook.com/", help="url")


@pytest.fixture(scope="class")
def driver_init(request):
    web_driver = ''
    if request.config.getoption("--driver") == "chrome":
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        web_driver = webdriver.Chrome(options=options)
        web_driver.get("about:blank")
        web_driver.implicitly_wait(5)
        web_driver.maximize_window()
    else:
        print('only chrome is supported at the moment')
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture(scope="module")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="module")
def fb_username():
    return os.environ.get('FB_USERNAME')


@pytest.fixture(scope="module")
def fb_password():
    return os.environ.get('FB_PASSWORD')
