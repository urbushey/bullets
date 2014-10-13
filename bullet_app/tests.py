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


class BulletsViewTest(TestCase):

    def test_uses_bullets_template(self):
        response = self.client.get('/bullets/the-only-bullets-in-the-world/')
        self.assertTemplateUsed(response, 'bullets.html')

    def test_displays_all_bullets(self):
        Bullet.objects.create(text='bullet 1')
        Bullet.objects.create(text='bullet 2')

        response = self.client.get('/bullets/the-only-bullets-in-the-world/')
        self.assertContains(response, 'bullet 1')
        self.assertContains(response, 'bullet 2')

class NewBulletsTest(TestCase):

    def test_saving_a_POST_request(self):
        self.client.post(
            '/bullets/new',
            data={'bullet_text': 'A new bullet'}
            )
        self.assertEqual(Bullet.objects.count(), 1)
        new_bullet = Bullet.objects.first()
        self.assertEqual(new_bullet.text, 'A new bullet')

    def test_redirects_after_POST(self):
        response = self.client.post(
            '/bullets/new',
            data={'bullet_text': 'A new bullet'}
            )

        self.assertRedirects(response,
                             '/bullets/the-only-bullets-in-the-world/')
