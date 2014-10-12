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
        request = HttpRequest()
        request.method = 'POST'
        request.POST['bullet_text'] = 'A new bullet'

        response = home_page(request)

        self.assertIn('+ A new bullet', response.content.decode())
        expected_html = render_to_string('home.html',
                                         {'new_bullet_text': 'A new bullet'}
                                         )
        self.assertEqual(response.content.decode(), expected_html)

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
