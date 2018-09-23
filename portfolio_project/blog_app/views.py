from django.shortcuts import render, get_object_or_404
from .models import Blog
#from . import all_blogs
# Create your views here.
def all_blogs(request):
	blogs = Blog.objects
	return render(request, 'blog_app/all_blogs.html', {'blogs': blogs} )

def detail(request, blog_id):
	detail = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog_app/detail.html', {'blog': detail })