from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import News_post
from .forms import News_postForm

# Create your views here.

def home(request):
	news = News_post.objects.all()
	return render(request, 'films/films.html', {'news': news})

def create_film(request):
	error = ""
	if request.method == 'POST':
		form = News_postForm(request.POST) # Сюда сохранится информация от пользователя.
		if form.is_valid():
			form.save()
			return redirect('news_home')
		else:
			error = "Данные были заполнены некорректно"
	form = News_postForm()
	return render(request, 'films/add_new_post.html', {'form': form, 'error': error})