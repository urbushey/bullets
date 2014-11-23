from django.shortcuts import redirect, render
from bullet_app.models import Bullet, BulletGroup
# Create your views here.


def home_page(request):
    return render(request,
                  'home.html'
                  )


def view_bullets(request, bullet_group_id):
    bg = BulletGroup.objects.get(id=bullet_group_id)
    return render(request,
                  'bullets.html',
                  {'bullet_group': bg})


def new_bullet_group(request):
    bg = BulletGroup.objects.create()
    Bullet.objects.create(text=request.POST['bullet_text'],
                          sign=request.POST['bullet_sign'],
                          bullet_group=bg)
    return redirect('/bullets/%d/' % (bg.id,))


def add_bullet(request, bullet_group_id):
    bg = BulletGroup.objects.get(id=bullet_group_id)
    Bullet.objects.create(text=request.POST['bullet_text'],
                          sign=request.POST['bullet_sign'],
                          bullet_group=bg)
    return redirect('/bullets/%d/' % (bg.id,))
