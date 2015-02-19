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
