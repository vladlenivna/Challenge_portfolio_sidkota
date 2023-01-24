from pages.base_page import BasePage


class AddMatchForm(BasePage):
    # Menu Items
    main_page_menu_item_xpath = "//*[name()='path'][contains(@d, 'M10 20v')]//ancestor::div[@role='button']"
    players_menu_item_xpath = "//*[name()='path'][contains(@d, 'M12 12c2')]//ancestor::div[@role='button']"
    players_name_menu_item_xpath = "//*[name()='path'][contains(@d, 'M13.49')]//ancestor::div[@role='button']"
    matches_menu_item_xpath = "//*[name()='path'][contains(@d, 'M12 2C6')]//ancestor::div[@role='button']"
    reports__menu_item_xpath = "//*[name()='path'][contains(@d, 'M19 3h')]//ancestor::div[@role='button']"
    language_menu_item_xpath = "//*[name()='path'][contains(@d, 'M12.87')]//ancestor::div[@role='button']"
    sign_out_xpath = "//*[name()='path'][contains(@d, 'M13 3h')]//ancestor::div[@role='button']"
    # Form Fields
    input_my_team_xpath = "//input[@name='myTeam']"
    input_enemy_team_xpath = "//input[@name='enemyTeam']"
    input_my_team_score_xpath = "//input[@name='myTeamScore']"
    input_my_enemy_team_score_xpath = "//input[@name='enemyTeamScore']"
    input_date_xpath = "//input[@name='date']"
    input_tshirt_xpath = "//input[@name='tshirt']"
    input_league_xpath = "//input[@name='league']"
    input_time_played_xpath = "//input[@name='timePlayed']"
    input_number_xpath = "//input[@name='number']"
    input_web_match_xpath = "//input[@name='webMatch']"
    input_general_xpath = "//input[@name='general']"
    input_rating_xpath = "//input[@name='rating']"
    # Radio Buttons
    match_in_home_radio_xpath = "//form//label[@type='radio'][1]"
    match_out_home_radio_xpath = "//form//label[@type='radio'][1]"
    # Buttons
    submit_button_xpath = "//form//button[@type='submit']"
    clear_button_xpath = "//form//button[@type='button']"


