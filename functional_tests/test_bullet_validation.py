import unittest
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_bullets(self):

        # Milton goes to the home page and accidentally tries to submit
        # an empty bullet.
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_bullet').send_keys('\n')


        # The home page refreshes, and there is an error message saying that
        # bullets cannot be blank.
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty bullet")

        #Milton tries again with some text.
        self.browser.find_element_by_id('id_new_bullet').send_keys('Today was good\n')
        self.check_list_table_for_row('Today was good')

        # perversely, he now decides to submit a second blank list item
        self.browser.find_element_by_id('id_new_bullet').send_keys('\n')
        self.check_list_table_for_row('Today was good')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty bullet")

        # He corrects it by adding  a second bullet that is not blank
        self.check_list_table_for_row('Today was good')
        self.check_list_table_for_row('Today was good')

        # Milton can enter the bullet and press enter and it is saved
        # Milton can come back to the site and see his bullets
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

