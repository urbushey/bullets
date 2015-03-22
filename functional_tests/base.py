from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import sys


class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_list_table_for_row(self, value):
        table = self.browser.find_element_by_id('id_bullets_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(value, [row.text for row in rows])

    def get_bullets_table(self):
        table = self.browser.find_element_by_id('id_bullets_table')
        rows = table.find_elements_by_tag_name('tr')
        return rows

    def get_bullet_input_box(self):
        return self.browser.find_element_by_id('id_text')
