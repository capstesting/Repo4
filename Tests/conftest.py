from selenium import webdriver
from time import sleep
import pytest


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(executable_path='E:\Python\Selenium\chromedriver.exe')
    driver.get('https://www.seleniumeasy.com/test/')
    driver.maximize_window()
    sleep(3)
    driver.find_element_by_xpath('//a[@id="at-cv-lightbox-close"]').click()
    request.cls.driver=driver
