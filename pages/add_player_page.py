from pages.base_page import BasePage


class AddPlayerPage(BasePage):
    expected_title = "Add player"
    page_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'

    def title_of_page(self):
        assert self.get_page_title(self.page_url) == self.expected_title

