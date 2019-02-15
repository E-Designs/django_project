from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#dummy data fake posts.
posts = [
    {
       'author': 'ErnestLH',
       'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]
#end fake posts
def home(reqest):
    context = {
        'posts': posts
    }
    return render(reqest, 'blog/home.html', context)

def about(request):  
    return render(request, 'blog/about.html', {'title': 'About'})