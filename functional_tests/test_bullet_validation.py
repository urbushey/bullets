import unittest
from .base import FunctionalTest


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

