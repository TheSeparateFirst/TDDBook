from selenium import webdriver
import unittest
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # JDub has heard about this new to-do app, and is now losing his goddamn mind
        # He opens up chrome and checks it out.
        self.browser.get('http://localhost:8000')

        # He sees the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # He is invited to enter a to-do item straight away

        # He types "Purchase uptimewarriors.com" into a text box

        # When He hits enter, the page updates, and now the page lists
# "1: Purchase uptimewarriors.com" as an item in a to-do list

        # Thise is still a text box inviting him to add anothis item. He
        # enters "Make a wordpress blog for uptimewarriors.com"

        # The page updates again, and now shows both items on his list

        # JDub wonders whether the site will remember his list. Then He sees
        # that the site has generated a unique URL for him -- there is some
        # explanatory text to that effect.

        # He visits that URL - his to-do list is still there.

        # Satisfied, He goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
