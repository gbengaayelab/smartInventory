from django.http import HttpResponse
from django.shortcuts import render
from .models import Department, Email, Inventories


def index(request):
    inventories = Inventories.objects.all()
    return render(request, 'index.html',
                  {'inventories': inventories})

