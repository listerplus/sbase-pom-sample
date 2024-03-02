########################################################################
### FILE:       test_main_page.py
###
########################################################################

from pages.main_page import MainPage
#import pytest_check as pycheck
from time import sleep

class TestMainPage(MainPage):

    def setUp(self):
        super().setUp()
        self.do_open_page()
        self.do_login_std()

    def tearDown(self):
        super().tearDown()

    def test_01_images(self):
        sleep(1)
        broken_img_count = self.get_num_images_broken_on_page()
        print(f"Total broken image count: {broken_img_count}")
        # pycheck.equal(broken_img_count, 0)
        # use assert or deferred_assert as dashboard and report incorrectly reflect failure with pytest-check
        self.assert_equal(broken_img_count, 0)