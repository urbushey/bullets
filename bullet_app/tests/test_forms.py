from django.test import TestCase
from bullet_app.forms import EMPTY_BULLET_ERROR, BulletForm


class BulletFormTest(TestCase):

    def test_form_renders_bullet_text_input(self):
        form = BulletForm()
        self.assertIn('placeholder="+ This week I..."', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_validation_for_blank_items(self):
        form = BulletForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['text'],
            [EMPTY_BULLET_ERROR]
        )
