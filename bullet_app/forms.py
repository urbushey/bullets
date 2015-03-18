from django import forms

from bullet_app.models import Bullet

EMPTY_BULLET_ERROR = "You can't have an empty bullet item"

class BulletForm(forms.models.ModelForm):

    class Meta:
        model = Bullet
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': '+ Enter a to-do item',
                'class': 'form-control input-lg',
            }),
        }
        error_messages = {
            'text': {'required': EMPTY_BULLET_ERROR}
        }
