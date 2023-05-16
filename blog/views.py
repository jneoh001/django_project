from django.shortcuts import render

posts = [
    {
        'author' : 'Javier',
        'title': 'Blog Post 1',
        'content': 'First post !! ',
        'date_posted': 'August 2 2022'
    },
    {
        'author' : 'George',
        'title': 'Blog Post 2',
        'content': ' Having fun now!! ',
        'date_posted': 'August 3 2022'
    },
]

def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})