########################################################################
### FILE:       base_page.py
###
########################################################################

from seleniumbase import BaseCase


class BasePage(BaseCase):
    # CSS Selector
    USERNAME_FIELD = "#user-name"
    PASSWORD_FIELD = "#password"
    LOGIN_BTN = "#login-button"

    # Texts
    BASE_URL = "https://www.saucedemo.com/"
    USER_STD = "standard_user"
    PASSWORD = "secret_sauce"

    def do_open_page(self):
        self.open(self.BASE_URL)

    def do_login_std(self):
        self.type(self.USERNAME_FIELD, self.USER_STD)
        self.type(self.PASSWORD_FIELD, self.PASSWORD)
        self.click(self.LOGIN_BTN)

    def do_logout(self):
        pass



