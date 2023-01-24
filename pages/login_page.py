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

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
