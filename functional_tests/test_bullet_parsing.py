from .base import FunctionalTest
from unittest import skip

@skip
class BulletParsingTest(FunctionalTest):

    def test_sign_parsing(self):
        # Uri goes to the homepage.
        self.browser.get(self.server_url)
        # Uri wants to use a '+' at the beginning of his message to
        # set the bullet's positivity to 1.
        self.get_bullet_input_box().send_keys(
                                        '+ This is good]\n')
        row = self.get_bullets_table()[0]
        self.assertIn('This is good', row.text)
        self.assertEqual(row.sign, '+')
        # Uri wants to add a new bullet. He wants this one to be negative.
        self.get_bullet_input_box().send_keys(
                                        '- This is bad\n')
        row = self.get_bullets_table()[1]
        self.assertIn('This is bad', row.text)
        self.assertEqual(row.sign, '-')
        # # Uri wants to add a bullet that has 3 positives.
        # self.get_bullet_input_box().send_keys(
        #                                 '+++ Triple good!\n')
        # row = self.get_bullets_table()[2]
        # self.assertIn('Triple good!', row.text)
        # self.assertEqual(row.positive_score, 3)
        # self.assertEqual(row.negative_score, 0)
        # # Uri wants to add a bullet that has 3 negatives.
        # self.get_bullet_input_box().send_keys(
        #                                 '+++ Triple bad!\n')
        # row = self.get_bullets_table()[3]
        # self.assertIn('Triple bad!', row.text)
        # self.assertEqual(row.positive_score, 0)
        # self.assertEqual(row.negative_score, 3)
        # # Uri wants to add a bullet that has 1 positive and one negative.
        # # Note that the '-' in the middle of the sentence is not
        # # incorreclty counted.
        # self.get_bullet_input_box().send_keys(
        #                                 '+/- One good - one bad!\n')
        # row = self.get_bullets_table()[4]
        # self.assertIn('One good - one bad!', row.text)
        # self.assertEqual(row.positive_score, 1)
        # self.assertEqual(row.negative_score, 1)
        # # Uri wants to add a bullet that has 4 positives and 3 negatives.
        # self.get_bullet_input_box().send_keys(
        #                                 '++++--- Four good three bad!\n')
        # row = self.get_bullets_table()[5]
        # self.assertIn('Four good three bad!', row.text)
        # self.assertEqual(row.positive_score, 4)
        # self.assertEqual(row.negative_score, 3)
        # # Uri wants to add a bullet that has 5 positive and 5 negatives.
        # self.get_bullet_input_box().send_keys(
        #                                 '+++++ ----- Five good five bad!\n')
        # row = self.get_bullets_table()[6]
        # self.assertIn('Five good five bad!', row.text)
        # self.assertEqual(row.positive_score, 5)
        # self.assertEqual(row.negative_score, 5)
        # # Uri can't add a bullet with more than 5 positives or 5 -.
        # self.get_bullet_input_box().send_keys(
        #                                 '++++++++ --------- \
        #                                 Still five good five bad!\n')
        # row = self.get_bullets_table()[7]
        # self.assertIn('Still five good five bad!', row.text)
        # self.assertEqual(row.positive_score, 5)
        # self.assertEqual(row.negative_score, 5)

