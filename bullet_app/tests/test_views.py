from django.core.urlresolvers import resolve
from django.utils.html import escape
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from bullet_app.views import home_page
from bullet_app.models import Bullet, BulletGroup

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

    def test_can_select_bullet_sign_and_save(self):
        response = self.client.post(
            '/bullets/new',
            data={'bullet_text': 'A negative bullet',
                  'bullet_sign': '-'
                 }
            )
        # follow the redirect
        self.assertContains(self.client.get(response.url),
                            '- A negative bullet')


class BulletsViewTest(TestCase):

    def test_uses_bullets_template(self):
        bg = BulletGroup.objects.create()
        response = self.client.get('/bullets/%d/' % (bg.id,))
        self.assertTemplateUsed(response, 'bullets.html')

    def test_displays_only_bullets_in_bullet_group(self):
        correct_bg = BulletGroup.objects.create()
        Bullet.objects.create(text='bullet 1', bullet_group=correct_bg)
        Bullet.objects.create(text='bullet 2', bullet_group=correct_bg)
        other_bg = BulletGroup.objects.create()
        Bullet.objects.create(text='other bullet 1', bullet_group=other_bg)
        Bullet.objects.create(text='other bullet 2', bullet_group=other_bg)

        response = self.client.get('/bullets/%d/' % (correct_bg.id,))

        self.assertContains(response, 'bullet 1')
        self.assertContains(response, 'bullet 2')
        self.assertNotContains(response, 'other bullet 1')
        self.assertNotContains(response, 'other bullet 2')

    def test_displays_bullet_sign(self):
        bg = BulletGroup.objects.create()
        Bullet.objects.create(text='positive bullet',
                              bullet_group=bg,
                              sign='+')
        Bullet.objects.create(text='negative bullet',
                              bullet_group=bg,
                              sign='-')

        response = self.client.get('/bullets/%d/' % (bg.id,))
        self.assertContains(response, '+ positive bullet')
        self.assertContains(response, '- negative bullet')

class NewBulletGroupTest(TestCase):

    def test_saving_a_POST_request(self):
        self.client.post(
            '/bullets/new',
            data={'bullet_text': 'A new bullet',
                  'bullet_sign': '+'}
            )
        self.assertEqual(Bullet.objects.count(), 1)
        new_bullet = Bullet.objects.first()
        self.assertEqual(new_bullet.text, 'A new bullet')

    def test_redirects_after_POST(self):
        response = self.client.post(
            '/bullets/new',
            data={'bullet_text': 'A new bullet',
                  'bullet_sign': '+'}
            )
        bullet_group = BulletGroup.objects.first()
        self.assertRedirects(response,
                             '/bullets/%d/' % (bullet_group.id))

    def test_can_save_a_POST_request_to_existing_bullet_group(self):
        other_bullet_group = BulletGroup.objects.create()
        correct_bullet_group = BulletGroup.objects.create()

        self.client.post(
            '/bullets/%d/add_bullet' % (correct_bullet_group.id,),
            data={'bullet_text': 'A new bullet for an existing bullet_group',
                  'bullet_sign': '+'}
            )

        self.assertEqual(Bullet.objects.count(), 1)
        new_bullet = Bullet.objects.first()
        self.assertEqual(new_bullet.text,
                         'A new bullet for an existing bullet_group')
        self.assertEqual(new_bullet.bullet_group, correct_bullet_group)
        self.assertNotEqual(new_bullet.bullet_group, other_bullet_group)

    def test_redirects_after_POST_to_existing_bullet_group(self):
        other_bullet_group = BulletGroup.objects.create()
        correct_bullet_group = BulletGroup.objects.create()

        response = self.client.post(
            '/bullets/%d/add_bullet' % (correct_bullet_group.id,),
            data={'bullet_text': 'A new bullet for an existing bullet_group',
                  'bullet_sign': '+'}
            )

        self.assertRedirects(response,
                             '/bullets/%d/' % (correct_bullet_group.id,)
                             )

    def test_passes_correct_bullet_group_to_template(self):
        other_bullet_group = BulletGroup.objects.create()
        correct_bullet_group = BulletGroup.objects.create()
        response = self.client.get('/bullets/%d/' % (correct_bullet_group.id,))
        self.assertEqual(response.context['bullet_group'],
                         correct_bullet_group
                         )

    def test_validation_errors_are_sent_to_template(self):

        response = self.client.post('/bullets/new',
                                    data={'bullet_text': '',
                                          'bullet_sign': '+'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        expected_error = escape("You can't have an empty bullet")
        self.assertContains(response, expected_error)
