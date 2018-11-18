from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'labMat/home.html', {'title': 'Home Page'})
