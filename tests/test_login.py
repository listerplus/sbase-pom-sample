########################################################################
### FILE:       test_login.py
###
########################################################################

from pages.login_page import LoginPage

class TestLogin(LoginPage):

    def setUp(self):
        super().setUp()
        self.do_open_page()

    def tearDown(self):
        super().tearDown()

    def test_01_locked_out(self):
        self.do_login(LoginPage.USER_LOCKED, LoginPage.PASSWORD)
        self.assert_text(LoginPage.MSG_ERROR, LoginPage.MSG_CONTAINER)
