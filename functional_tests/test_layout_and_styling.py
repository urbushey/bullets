from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # Bereket goes to the homepage
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # she notices the input box is neatly centered
        inputbox = self.browser.find_element_by_id('id_new_bullet')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=25)  # I am not following the book exactly but I want
                       # this test to pass even with the +/- dropdown

        # she sees the same thing when she submits input
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_bullet')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=25)  # I am not following the book exactly but I want
                       # this test to pass even with the +/- dropdown


class ItemValidationTest(FunctionalTest):

    @skip
    def test_cannot_add_empty_list_items(self):

        # Milton goes to the home page and accidentally tries to submit
        # an empty bullet.

        # The home page refreshes, and there is an error message saying that
        # bullets cannot be blank.

        #Milton tries again with some text.

        self.fail('write me')

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

