from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from bullet_app.models import Bullet, BulletGroup
# Create your views here.


def home_page(request):
    return render(request,
                  'home.html'
                  )


def view_bullets(request, bullet_group_id):
    bg_ = BulletGroup.objects.get(id=bullet_group_id)
    error = None

    if request.method == 'POST':
        try:
            bullet = Bullet(text=request.POST['bullet_text'],
                            sign=request.POST['bullet_sign'],
                            bullet_group=bg_)
            bullet.full_clean()
            bullet.save()
            return redirect('/bullets/%d/' % (bg_.id,))
        except ValidationError:
            error = "You can't have an empty bullet"

    return render(request,
                  'bullets.html',
                  {'bullet_group': bg_,
                   'error': error})


def new_bullet_group(request):
    bg = BulletGroup.objects.create()
    bullet = Bullet.objects.create(text=request.POST['bullet_text'],
                                   sign=request.POST['bullet_sign'],
                                   bullet_group=bg)
    try:
        bullet.full_clean()
    except ValidationError:
        error = "You can't have an empty bullet"
        return render(request, 'home.html', {"error": error})
    return redirect('/bullets/%d/' % (bg.id,))
