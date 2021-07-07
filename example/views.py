from django.shortcuts import render
from .models import Company
from .models import farRockaway

# Create your views here.

def post_html(request):
    google = Company(name="Dennis Kwarteng")
    return render(request, 'example/post_html.html', {'google':google})

def FarRock(request):
    rock = farRockaway.objects.all()
    return render(request, 'example/FarRock.html', {'rock':rock})
