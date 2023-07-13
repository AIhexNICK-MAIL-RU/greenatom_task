from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm

def index(request):
    films = Film.objects.order_by('-id')
    return render(request, "main/index.html", {'title': 'Главная страница сайта', 'films': films})
    # return HttpResponse("<h4>Hello</h4>")


def about(request):
    return render(request, "main/about.html")

def create(request):
    error = ''
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была неверной'

    form = FilmForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, "main/create.html")