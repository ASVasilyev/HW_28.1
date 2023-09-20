import pytest
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver():
   driver = webdriver.Chrome()
   driver.maximize_window()

   # Переходим на страницу авторизации
   driver.get('https://b2c.passport.rt.ru')

   yield driver

   driver.quit()


@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.datetime.now()
    yield
    end_time = datetime.datetime.now()
    print(f"\n Время выполнения теста: {end_time - start_time}")


@pytest.fixture(autouse=True)
def start_end():
    print("\n\n Старт теста")
    yield
    print(" Финиш теста")
