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
        self.assertIn('Batchcave', self.browser.title)
        self.fail('Finish the test!')

        #User is presented with a list of processes to choose from


#User selects a process

#User is taken to the process window

#User is able to upload a file through dialog box

#File is processed and downloads through user's browser

#User is prompted to perform the same process again or return to main menu


#User exits


if __name__ == '__main__':
    unittest.main(warnings='ignore')
