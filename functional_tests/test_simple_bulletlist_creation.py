from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_bullet_and_retrieve_later(self):
        # It is Friday, time for bullets.
        # Milton wants to use our app instead of email. He goes to the homepage
        self.browser.get(self.server_url)

        # Milton first visits the site and sees no bullets.
        self.assertIn('Friday Bullets', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Bullets', header_text)

        # Milton wants to add the first bullet
        inputbox = self.get_bullet_input_box()
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         '+ This week I...'
                         )

        # Milton wants to give Uri credit.
        inputbox.send_keys('Uri saved the day.')

        # Milton hits enter, and now the new bullet appears in the table.
        inputbox.send_keys(Keys.ENTER)
        milton_bullets_url = self.browser.current_url
        self.assertRegex(milton_bullets_url,
                         '/bullets/.+')

        # Milton wants to give Bereket some credit too by entering a second
        # item.
        inputbox = self.get_bullet_input_box()
        inputbox.send_keys('Bereket committed some sick code too.')
        inputbox.send_keys(Keys.ENTER)

        self.check_list_table_for_row('Uri saved the day.')
        self.check_list_table_for_row('Bereket committed some sick code too.')

        # Bereket wants to enter bullets also
        ## New web browser session
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Bereket visits home page. Does not see anyone else's bullets
        ## This is because I am following along with the TDD python book
        ## Normally we want him to see other people's bullets
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Uri saved the day', page_text)
        self.assertNotIn('Bereket committed some sick code', page_text)

        # Bereket enters his own bullet
        inputbox = self.get_bullet_input_box()
        inputbox.send_keys('Had a bad day')
        inputbox.send_keys(Keys.ENTER)

        # Bereket gets his own URL
        bereket_bullets_url = self.browser.current_url
        self.assertRegex(bereket_bullets_url,
                         '/bullets/.+')
        self.assertNotEqual(bereket_bullets_url, milton_bullets_url)

        # Again, make sure Bereket doesn't see Milton's bullets
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Uri saved the day', page_text)
        self.assertIn('Had a bad day', page_text)

        # Milton comes back and wants to enter a bullet that is negative
        ## New web browser session
        # TODO commenting out
        #self.browser.quit()
        #self.browser = webdriver.Firefox()
        #self.browser.get(self.server_url)
        #bullet_dropdown = \
        #    self.browser.find_element_by_id('id_new_bullet_dropdown')
        #for option in bullet_dropdown.find_elements_by_tag_name('option'):
        #    if option.text == "-":
        #        option.click()
        #        break
