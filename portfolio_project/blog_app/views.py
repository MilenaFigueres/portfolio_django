from django.shortcuts import render

# Create your views here.
def all_blogs(request):
	return render(request, 'blog_app/all_blogs.html' )