from django.shortcuts import render


def home(request):
    return render(request, 'labMat/home.html', {'title': 'Home Page'})
