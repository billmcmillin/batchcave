from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

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


class NewConversionTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

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
        processBox = self.browser.find_element_by_tag_name("select")
        processBox.send_keys('Firstiest conversion')

        #User is able to upload a file through dialog box
        uploadBox = self.browser.find_element_by_id("id_Upload")
        uploadBox.send_keys("~/TEST.mrc")

        submitButton = self.browser.find_element_by_tag_name("form")
        submitButton.submit()

        #File is processed and user is taken to a status view

        #When user clicks download link, file downloads through user's browser

        #User can view conversion details or return to main menu

        #self.fail('Finish the test!')

#User exits


