from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Item, Year, Plan
# from django.views.generic import ListView


@login_required
def home(request):
    context = {
        'items': Item.objects.all(),
        'years': Year.objects.last(),
        'plans': Plan.objects.all()
    }
    return render(request, 'labMat/home.html', context)

