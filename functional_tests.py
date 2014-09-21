from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_bullet_and_retrieve_later(self):
        # Milton visits the site and sees no bullets
        assert 'Friday Bullets' in self.browser.title

        # Milton wants to add the first bullet
        # Milton clicks a plus button to begin typing a bullet
        # Milton can choose whether this bullet is + or -
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

if __name__ == '__main__':
    unittest.main(warnings='ignore')
