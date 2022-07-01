from django.shortcuts import render
from django.views.generic import View

def show_base(request):
    context = {
        
    }
    return render(request, '/templates/', context)