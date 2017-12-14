from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

class LayoutandStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url + '/conversions/create')
        self.browser.set_window_size(1024, 768)

        inputbox = self.browser.find_element_by_id('id_Name')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2, 512,
            delta=30
        )

