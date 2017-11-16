from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_user_is_presented_menu_of_processes(self):
        #User has batch records to convert, goes to batchcave homepage
        self.browser.get('http://localhost:8000')

        #User is presented with basic info about the app
        self.assertIn('BatchCave', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('BatchCave', header_text)

        #User is presented with a list of processes to choose from
        menu = self.browser.find_element_by_id('id_menu_header')
        self.assertEqual(
            menu.text,
            'Select Process'
        )
        choice1 = self.browser.find_element_by_id('id_ER_EAI_2nd')
        self.assertEqual(
            choice1.text,
            'ER_EAI_2nd'
       )

        #User selects a process
    def test_user_can_select_process(self):
        self.browser.get('http://localhost:8000')
        choice1 = self.browser.find_element_by_id('id_ER_EAI_2nd')
        choice1.click()

        #User is taken to the process window

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Begin New Conversion', header_text)

#User is able to upload a file through dialog box

#File is processed and downloads through user's browser

#User is prompted to perform the same process again or return to main menu

        self.fail('Finish the test!')

#User exits


if __name__ == '__main__':
    unittest.main(warnings='ignore')
