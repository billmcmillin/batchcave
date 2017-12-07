from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_user_can_choose_from_main_menu(self):
        #User has batch records to convert, goes to batchcave homepage
        self.browser.get('http://localhost:8000')

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

    def test_user_is_presented_menu_of_processes(self):

        self.browser.get('http://localhost:8000/converions/create')

        #User is presented with a list of processes to choose from
        choice1 = self.browser.find_element_by_id('id_ER_EAI_2nd')
        self.assertEqual(
            choice1.text,
            'ER_EAI_2nd'
       )

        #User selects a process

    def test_user_can_select_process(self):
        pass
        #self.browser.get('http://localhost:8000/conversions/create')

        #User is taken to the process window

        #header_text = self.browser.find_element_by_tag_name('h2').text
        #self.assertIn('Begin New Conversion', header_text)

        #User can select a process
        #process_link = self.browser.find_element_by_tag_name('option').text
        #self.assertIn('ER_EAI_2nd', process_link)

        #User is able to upload a file through dialog box

        #File is processed and user is taken to a status view

        #When user clicks download link, file downloads through user's browser

        #User can view conversion details or return to main menu

        #self.fail('Finish the test!')

#User exits


if __name__ == '__main__':
    unittest.main(warnings='ignore')
