from .base import FunctionalTest


class BulletParsingTest(FunctionalTest):

    def test_sign_parsing(self):
        # Uri goes to the homepage.
        self.browser.get(self.server_url)
        # Uri wants to use a '+' at the beginning of his message to
        # set the bullets positivity to 1.
        self.browser.find_element_by_id('id_new_bullet').send_keys('+ This is good')
        self.check_list_table_for_row('+ Uri saved the day.')
        self.
        # Uri wants to add a new bullet. He wants this one to be negative.
        # Uri wants to add a bullet that has 3 positives.
        # Uri wants to add a bullet that has 3 negatives.
        # Uri wants to add a bullet that has 1 positive and one negative.
        # Uri wants to add a bullet that has 4 positives and 3 negatives.
        # Uri wants to add a bullet that has 5 positive and 5 negatives.
        # Uri can't add a bullet with more than 5 positives or 5 -.
