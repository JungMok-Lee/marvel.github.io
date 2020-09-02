from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    return render(request, 'home.html')

def news(request):
    news = Blog.objects
    return render(request, 'movie/news.html', {'news': news})

def news_detail(request, news_id):
    news_detail = get_object_or_404(Blog, pk=news_id)
    return render(request, 'movie/news_detail.html', {'news':news_detail})

def introduce(request):
    return render(request, 'introduce/introduce.html')

def maker(request):
    return render(request, 'introduce/maker.html')

def aboutmarvel(request):
    return render(request, 'introduce/aboutmarvel.html')

def motivation(request):
    return render(request, 'introduce/motivation.html')

def process(request):
    return render(request, 'introduce/process.html')


def movie(request):
    return render(request, 'movie/movie.html')

def trailer(request):
    return render(request, 'movie/trailer.html')

def audience(request):
    return render(request, 'movie/audience.html')

def plan(request):
    return render(request, 'movie/plan.html')

def character(request):
    return render(request, 'character/character.html')

def captain(request):
    return render(request, 'character/captain.html')

def ironman(request):
    return render(request, 'character/ironman.html')

def blackwidow(request):
    return render(request, 'character/blackwidow.html')

def wintersoldier(request):
    return render(request, 'character/wintersoldier.html')