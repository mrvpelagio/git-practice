from django.shortcuts import render
from django.http import HttpResponse
from  django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello. This is from the index views.py")

def task_list(request):
    ctx = {
        "Practicing": [
            "Task 1",
            "Task 2",
            "Task 3"
        ]
    }
    return render(request, "task_list.html", ctx)