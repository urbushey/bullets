from django.shortcuts import redirect, render
from bullet_app.models import Bullet
# Create your views here.


def home_page(request):
    if request.method == 'POST':
        Bullet.objects.create(text=request.POST['bullet_text'])
        return redirect('/')

    bullets = Bullet.objects.all()
    return render(request,
                  'home.html',
                  {'bullets': bullets})
