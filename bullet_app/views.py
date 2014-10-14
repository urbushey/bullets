from django.shortcuts import redirect, render
from bullet_app.models import Bullet, BulletGroup
# Create your views here.


def home_page(request):
    return render(request,
                  'home.html'
                  )


def view_bullets(request):
    bullets = Bullet.objects.all()
    return render(request,
                  'bullets.html',
                  {'bullets': bullets})


def new_bullet(request):
    bg = BulletGroup.objects.create()
    Bullet.objects.create(text=request.POST['bullet_text'],
                          bullet_group=bg)
    return redirect('/bullets/the-only-bullets-in-the-world/')
