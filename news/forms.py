from django import forms
from .models import pictures, comments

class PictureForm(forms.ModelForm):
    class Meta:
        model = pictures
        fields = ('title', 'image')
        labels = {'title': 'Заголовок', 'image': 'Путь к картинке'}

class CommentForm(forms.ModelForm):
    class Meta:
        model = comments
        fields = ('text',)
        labels = {'text': 'Текст комментария'}