import time

from pages.base_page import BasePage

class LoginPage(BasePage):
    header_xpath = "//h5"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    remind_password_link_xpath = "//a[@tabindex='-1']"
    sign_in_button_xpath = "//button[@type='submit']"
    dropdown_language_xpath = "//div[@role='button']"
    menu_item_pl_xpath = "//li[@data-value='pl']"
    menu_item_en_xpath = "//li[@data-value='en']"

    expected_title = "Scouts panel - sign in"
    page_url = 'https://scouts-test.futbolkolektyw.pl/'

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.page_url) == self.expected_title

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, login):
        self.field_send_keys(self.password_field_xpath, login)

    def click_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)


