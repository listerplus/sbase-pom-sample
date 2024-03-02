########################################################################
### FILE:       main_page.py
###
########################################################################

from pages.base_page import BasePage
import requests


class MainPage(BasePage):
    # CSS Selectors
    ITEM4_IMG_ID = "#item_4_img_link"

    # Texts
    ITEM4_NAME = "Sauce Labs Backpack"
    ITEM4_IMG_SRC = "/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg"


    # Methods
    def get_num_images_broken_on_page(self):
        broken_count = 0
        url = self.get_current_url()
        image_list = self.find_elements(".img")
        print(f"Total number of images on {url} are: {len(image_list)}")

        for img in image_list:
            try:
                response = requests.get(img.get_attribute('src'), stream=True)
                if response.status_code != 200:
                    print(img.get_attribute('outerHTML') + " is broken.")
                    broken_count += 1

            except requests.exceptions.MissingSchema:
                print("Encountered MissingSchema Exception")
            except requests.exceptions.InvalidSchema:
                print("Encountered InvalidSchema Exception")
            except BaseException as e:
                print(f"Encountered Some other Exception: {e}")
        return broken_count
