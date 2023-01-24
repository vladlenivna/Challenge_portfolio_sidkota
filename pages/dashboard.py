from pages.base_page import BasePage


class Dashboard(BasePage):
    # Alternative selectors (It was my first variant, but I don't like it):
    # main_page_menu_item_xpath = "//*[text()='Main page' or text()='Strona główna']"
    # players_menu_item_xpath = "//*[text()='Players' or text()='Gracze']"
    # language_menu_item_xpath = "//*[text()='English' or text()='Polski']"
    # sign_out_xpath = "//*[text()='Sign out' or text()='Wyloguj']"
    # main_page_menu_item_xpath = "//div[contains(@class, 'jss38')]"
    # players_menu_item_xpath = "//div[contains(@class, 'jss39')]"

    main_page_menu_item_xpath = "//*[name()='path'][contains(@d, 'M10 20v')]//ancestor::div[@role='button']"
    players_menu_item_xpath = "//*[name()='path'][contains(@d, 'M12 12c2')]//ancestor::div[@role='button']"
    language_menu_item_xpath = "//*[name()='path'][contains(@d, 'M12.87')]//ancestor::div[@role='button']"
    sign_out_xpath = "//*[name()='path'][contains(@d, 'M13 3h')]//ancestor::div[@role='button']"
    players_count_xpath = "(//b)[1]"
    matches_count_xpath = "(//b)[2]"
    reports_count_xpath = "(//b)[3]"
    events_count_xpath = "(//b)[4]"
    dev_team_contact_xpath = "//*[@title='Logo Scouts Panel']//following::a"
    add_player_xpath = "//a[ends-with(@href, '/players/add')]"
    last_created_player_link_xpath = "(//a[contains(@href, 'edit')])[1]"
    last_updated_player_link_xpath = "(//a[contains(@href, 'edit')])[2]"
    last_created_match_link_xpath = "(//a[contains(@href, 'edit')])[3]"
    last_updated_match_link_xpath = "(//a[contains(@href, 'edit')])[4]"
    last_updated_report_link_xpath = "(//a[contains(@href, 'edit')])[5]"
