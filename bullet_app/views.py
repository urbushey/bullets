from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'home.html', {
                  # Return '' if bullet_text does not exist.
                  'new_bullet_text': request.POST.get('bullet_text', '')
                  })
