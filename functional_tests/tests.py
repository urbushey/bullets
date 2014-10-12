from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_list_table_for_row(self, value):
        table = self.browser.find_element_by_id('id_bullets_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(value, [row.text for row in rows])

    def test_can_start_bullet_and_retrieve_later(self):
        # It is Friday, time for bullets.
        # Milton wants to use our app instead of email. He goes to the homepage
        self.browser.get(self.live_server_url)

        # Milton first visits the site and sees no bullets.
        self.assertIn('Friday Bullets', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Bullets', header_text)

        # Milton wants to add the first bullet
        inputbox = self.browser.find_element_by_id('id_new_bullet')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         '+ This week I...'
                         )

        # Milton wants to give Uri credit.
        inputbox.send_keys('Uri saved the day.')

        # Milton hits enter, and now the new bullet appears in the table.
        inputbox.send_keys(Keys.ENTER)

        # Milton wants to give Bereket some credit too by entering a second
        # item.
        inputbox = self.browser.find_element_by_id('id_new_bullet')
        inputbox.send_keys('Bereket committed some sick code too.')
        inputbox.send_keys(Keys.ENTER)

        self.check_list_table_for_row('+ Uri saved the day.')
        self.check_list_table_for_row('+ Bereket committed some sick code too.')

        # Milton can choose whether this bullet is + or -
        # Milton can enter the bullet and press enter and it is saved
        # Milton can come back to the site and see his bullets
        self.fail("Finish writing the test!")

    # Bereket can come to the site and see Milton's bullet
    # Bereket can post his own bullet
    # Bereket can see Milton's bullet and his own bullet on the site
    # Bereket can collapse his bullet or Milton's bullet
    # Bereket can post a comment on Milton's bullet
    # Milton can see the comment posted on his bullet by Bereket
    # Bereket can see the bullets sorted by date
    # Bereket can see the bullets sorted by user
    # Bereket can see the bullets sorted by (team?)
    # Milton can embed rich text in his bullet
    # Milton can embed links in his bullet
    # Milton can embed a picture in his bullet
    # Bereket can email a link to Milton's bullet
    # Milton can sign into the site using his LDAP password (OY)