from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse 

def home1(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request,'blog/home1.html', context)

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})

# Create your views here.
