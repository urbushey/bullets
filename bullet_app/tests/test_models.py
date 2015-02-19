from django.test import TestCase
from django.core.exceptions import ValidationError
from bullet_app.models import Bullet, BulletGroup

# Create your tests here.


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

    def test_cannot_save_empty_bullets(self):
        bullet_group_ = BulletGroup.objects.create()
        bullet = Bullet(bullet_group=bullet_group_,
                        text='')
        with self.assertRaises(ValidationError):
            bullet.save()
            bullet.full_clean()

    def test_get_absolute_url(self):
        bg_ = BulletGroup.objects.create()
        self.assertEqual(bg_.get_absolute_url(), '/bullets/%d/' % (bg_.id,))
