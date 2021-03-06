from .base import FunctionalTest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select
from unittest import skip
from selenium.webdriver.common.keys import Keys

class Invalid_Input_Test(FunctionalTest):
    def test_cannot_add_incomplete_conversion(self):
        #user enters an incomplete item
        self.browser.get(self.live_server_url + '/conversions/create/')
        select = Select(self.browser.find_element_by_tag_name("select"))
        select.select_by_visible_text("ER_EAI_2nd")
        #User selects a process
        processBox = self.browser.find_element_by_tag_name("select")
        processBox.send_keys('Firstiest conversion')

        #User is able to upload a file through dialog box
        uploadBox = self.browser.find_element_by_id("id_Upload")
        uploadBox.send_keys("~/TEST.mrc")

        submitButton = self.browser.find_element_by_tag_name("form")
        submitButton.submit()


        #user submits and is redirected to error page
        #self.wait_for(lambda: self.assertEqual(
            #self.browser.find_element_by_css_selector('#error_msg').text, "There is an error with the submission."))

        #When user clicks download link, file downloads through user's browser

        #User can view conversion details or return to main menu

        #self.fail('Finish the test!')

#User exits


