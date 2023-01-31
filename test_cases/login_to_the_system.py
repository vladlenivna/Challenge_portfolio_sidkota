import unittest
from selenium import webdriver
from utils.settings import IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.dashboard import Dashboard


class TestLoginPage(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # self.driver.get('https://scouts-test.futbolkolektyw.pl/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_login_to_the_system(self):
        # self.driver.get('https://scouts-test.futbolkolektyw.pl/')
        # assert self.driver.title == 'Scouts panel - sign in'
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()

        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
