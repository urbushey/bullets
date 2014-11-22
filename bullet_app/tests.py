from django.core.urlresolvers import resolve
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

class NewBulletGroupTest(TestCase):

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
        bullet_group = BulletGroup.objects.first()
        self.assertRedirects(response,
                             '/bullets/%d/' % (bullet_group.id))

    def test_can_save_a_POST_request_to_existing_bullet_group(self):
        other_bullet_group = BulletGroup.objects.create()
        correct_bullet_group = BulletGroup.objects.create()

        self.client.post(
            '/bullets/%d/add_bullet' % (correct_bullet_group.id,),
            data={'bullet_text': 'A new bullet for an existing bullet_group'}
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
            data={'bullet_text': 'A new bullet for an existing bullet_group'}
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

class BulletAndBulletGroupModelsTest(TestCase):
    def test_saving_and_retrieving_bullets(self):
        bullet_group_ = BulletGroup()
        bullet_group_.save()

        first_bullet = Bullet()
        first_bullet.text = 'The first (ever) bullet. Bang!'
        first_bullet.sign = '+'
        first_bullet.bullet_group = bullet_group_
        first_bullet.save()

        second_bullet = Bullet()
        second_bullet.text = 'Second bullet'
        second_bullet.sign = '-'
        second_bullet.bullet_group = bullet_group_
        second_bullet.save()

        saved_group = BulletGroup.objects.first()
        self.assertEqual(saved_group, bullet_group_)

        saved_bullets = Bullet.objects.all()
        self.assertEqual(saved_bullets.count(), 2)

        first_saved_bullet = saved_bullets[0]
        second_saved_bullet = saved_bullets[1]
        self.assertEqual(first_saved_bullet.text,
                         'The first (ever) bullet. Bang!')
        self.assertEqual(first_saved_bullet.sign,
                         '+')
        self.assertEqual(first_saved_bullet.bullet_group, bullet_group_)
        self.assertEqual(second_saved_bullet.text,
                         'Second bullet')
        self.assertEqual(second_saved_bullet.sign,
                         '-')
        self.assertEqual(second_saved_bullet.bullet_group, bullet_group_)
