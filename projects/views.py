from django.shortcuts import render
from .models import Project

# Create your views here.
from django.http import HttpResponse


def index(request):
    queryset = Project.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "projects/index.html", context)
