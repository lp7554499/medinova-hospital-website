from django.shortcuts import render
from ourblogs.models import Blog

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})
