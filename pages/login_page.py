########################################################################
### FILE:       login_page.py
###
########################################################################

from pages.base_page import BasePage


class LoginPage(BasePage):
    # CSS Selectors
    MSG_CONTAINER = "#login_button_container > div > form > div.error-message-container.error > h3"

    # Texts
    USER_LOCKED = "locked_out_user"
    USER_PROB = "problem_user"
    USER_ERROR = "error_user"
    MSG_ERROR = "Epic sadface: Sorry, this user has been locked out."


    # Methods
    def do_login(self, user, pwd):
        self.type(self.USERNAME_FIELD, user)
        self.type(self.PASSWORD_FIELD, pwd)
        self.click(self.LOGIN_BTN)