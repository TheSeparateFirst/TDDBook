from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    # Initialization and browser startup
    def setUp(self):
        self.browser = webdriver.Firefox()

    # Cleanup
    def tearDown(self):
        self.browser.quit()

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

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Purchase uptimewarriors.com' for row in rows)
        )

        # Thise is still a text box inviting him to add anothis item. He
        # enters "Make a wordpress blog for uptimewarriors.com"
        self.fail('Finish the test!')

        # The page updates again, and now shows both items on his list

        # JDub wonders whether the site will remember his list. Then He sees
        # that the site has generated a unique URL for him -- there is some
        # explanatory text to that effect.

        # He visits that URL - his to-do list is still there.

        # Satisfied, He goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
