from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from unittest import skip
from selenium.webdriver.common.keys import Keys

class NewConversionTest(FunctionalTest):
    #User is presented with a list of processes to choose from
    def test_user_can_choose_type(self):
        self.browser.get(self.live_server_url + '/conversions/create/')
        response = self.browser.find_elements_by_tag_name('h1')
        self.assertIn('BatchCave',response[0].text)
        options = self.browser.find_elements_by_tag_name('option')
        self.assertIn('ER_EAI_2nd',options[2].text)

    def test_user_enters_conversion_info(self):
        self.browser.get(self.live_server_url + '/conversions/create/')
        select = Select(self.browser.find_element_by_tag_name("select"))
        select.select_by_visible_text("ER_EAI_2nd")
        #User selects a process
        nameBox = self.browser.find_element_by_css_selector("input#id_Name")
        nameBox.send_keys('Firstiest conversion')

        #User is able to upload a file through dialog box
        uploadBox = self.browser.find_element_by_id("id_Upload")
        uploadBox.send_keys("/home/mcmillwh/TEST.mrc")

        submitButton = self.browser.find_element_by_tag_name("form")
        submitButton.submit()

        #File is processed and user is taken to index view
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('h2').text, "Completed Conversions"
        ))

        #new conversion is listed
        self.wait_for(lambda: self.assertIn(
            "Firstiest conversion", self.browser.find_element_by_css_selector('tbody').text
        ))

        #link to uploaded file is also there
        number = self.browser.find_element_by_link_text("Firstiest conversion").id

        #User can only submit a complete form
