from .models import News_post
from django.forms import ModelForm, TextInput, Textarea


class News_postForm(ModelForm):
	class Meta:
		model = News_post
		fields = ['title', 'short_description', 'text', 'replay1', 'replay2', 'replay3']
		widgets = {
			'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Назваеие фильма'}),
			'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Жанр'}),
			'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание фильма'}),
			'replay1': Textarea(attrs={'class': 'form-control', 'placeholder': 'Популярный отзыв'}),
			'replay2': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отрицательный отзыв'}),
			'raiting': TextInput(attrs={'class': 'form-control', 'placeholder': 'Рейтинг'})
		}
