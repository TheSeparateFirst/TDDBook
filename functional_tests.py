from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    # Initialization and browser startup
    def setUp(self):
        self.browser = webdriver.Chrome()

    # Cleanup
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # JDub has heard about this new to-do app, and is now losing his goddamn mind
        # He opens up chrome and checks it out.
        self.browser.get('http://localhost:8000')

        # He sees the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do", header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # He types "Purchase uptimewarriors.com" into a text box
        inputbox.send_keys('Purchase uptimewarriors.com')

        # When He hits enter, the page updates, and now the page lists
# "1: Purchase uptimewarriors.com" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Purchase uptimewarriors.com')

        # There is still a text box inviting him to add another item. He
        # enters "Make a wordpress blog for uptimewarriors.com"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Make a wordpress blog for uptimewarriors.com')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on his list
        self.check_for_row_in_list_table('1: Purchase uptimewarriors.com')
        self.check_for_row_in_list_table('2: Make a wordpress blog for uptimewarriors.com')


        # JDub wonders whether the site will remember his list. Then He sees
        # that the site has generated a unique URL for him -- there is some
        # explanatory text to that effect.

        # He visits that URL - his to-do list is still there.

        # Satisfied, He goes back to sleep
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
