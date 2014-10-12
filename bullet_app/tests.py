from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from bullet_app.views import home_page
from bullet_app.models import Bullet

# Create your tests here.


class HomePageTest(TestCase):

    def test_root_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        #TODO this test is getting long
        request = HttpRequest()
        request.method = 'POST'
        request.POST['bullet_text'] = 'A new bullet'

        response = home_page(request)

        # Test that it actually saves to DB
        #self.assertEqual(Bullet.objects.count(), 1)
        new_bullet = Bullet.objects.first()
        self.assertEqual(new_bullet.text, 'A new bullet')

    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['bullet_text'] = 'A new bullet'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_saving_and_retrieving_bullets(self):
        first_bullet = Bullet()
        first_bullet.text = 'The first (ever) bullet. Bang!'
        first_bullet.save()

        second_bullet = Bullet()
        second_bullet.text = 'Second bullet'
        second_bullet.save()

        saved_bullets = Bullet.objects.all()
        self.assertEqual(saved_bullets.count(), 2)

        first_saved_bullet = saved_bullets[0]
        second_saved_bullet = saved_bullets[1]
        self.assertEqual(first_saved_bullet.text,
                         'The first (ever) bullet. Bang!')
        self.assertEqual(second_saved_bullet.text,
                         'Second bullet')

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Bullet.objects.count(), 0)

    def test_home_page_displays_all_bullets(self):
        Bullet.objects.create(text='bullet 1')
        Bullet.objects.create(text='bullet 2')

        request = HttpRequest()
        response = home_page(request)
        self.assertIn('bullet 1', response.content.decode())
        self.assertIn('bullet 2', response.content.decode())
