from django.shortcuts import redirect, render
from bullet_app.models import Bullet
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
    Bullet.objects.create(text=request.POST['bullet_text'])
    return redirect('/bullets/the-only-bullets-in-the-world/')
