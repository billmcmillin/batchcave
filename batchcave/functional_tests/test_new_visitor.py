from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip

class NewVisitorTest(FunctionalTest):

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url + '/conversions/create')
        self.browser.set_window_size(1024, 768)

        inputbox = self.browser.find_element_by_id('id_Name')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2, 512,
            delta=30
        )

    @skip
    def test_user_can_choose_from_main_menu(self):
        #User has batch records to convert, goes to batchcave homepage
        self.browser.get(self.live_server_url)

        #User is presented with basic info about the app
        self.assertIn('BatchCave', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('BatchCave', header_text)

        #User can choose to start a new conversion
        first_choice = self.browser.find_element_by_id('id_menu_createConversion')
        self.assertIn('Create New Conversion', first_choice.text)
        #User can view an index of past conversions
        second_choice = self.browser.find_element_by_id('id_menu_indexConversion')
        self.assertIn('View Past Conversions', second_choice.text)

