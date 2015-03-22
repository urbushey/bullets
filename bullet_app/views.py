from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from bullet_app.models import Bullet, BulletGroup
from bullet_app.forms import BulletForm
from bullet_app.lib.bulletparser import parse
# Create your views here.


def home_page(request):
    return render(request,
                  'home.html',
                  {'form': BulletForm()}
                  )


def view_bullets(request, bullet_group_id):
    bg_ = BulletGroup.objects.get(id=bullet_group_id)
    error = None

    if request.method == 'POST':
        try:
            # parse the text
            bullet_dict = parse(request.POST['text'])
            original_text = request.POST['text']
            text = bullet_dict["parsed_text"]
            # Parsing bullet text overrides the post contents.
            if "positive_score" in bullet_dict:
                positive_score = bullet_dict["positive_score"]
                negative_score = bullet_dict["negative_score"]
            else:
                # TODO update this to pay attention to POST content
                positive_score = 1
                negative_score = 0

            bullet = Bullet(original_text=original_text,
                            text=text,
                            positive_score=positive_score,
                            negative_score=negative_score,
                            bullet_group=bg_)
            bullet.full_clean()
            bullet.save()
            return redirect(bg_)
        except ValidationError:
            error = "You can't have an empty bullet"
    return render(request,
                  'bullets.html',
                  {'bullet_group': bg_,
                   'error': error})


def new_bullet_group(request):
    bg_ = BulletGroup.objects.create()
    bullet = Bullet.objects.create(text=request.POST['text'],
                                   bullet_group=bg_)
    try:
        bullet.full_clean()
        pass
    except ValidationError:
        error = "You can't have an empty bullet"
        return render(request, 'home.html', {"error": error})
    return redirect(bg_)
