from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))
                                   
class PoolForm(forms.Form):
    name = forms.CharField(label='ФИО',
        min_length=2, max_length=60)
    gender = forms.ChoiceField(label='Пол',
        choices=[('1', 'Мужской'), ('2', 'Женский')],
        widget=forms.RadioSelect, initial=1)
    grade = forms.ChoiceField(label='Оценка',
        choices=[('1', 'Ужасно'), ('2', 'Плохо'),
        ('3', 'Нормально'), ('4', 'Хорошо'), ('5', 'Отлично')] , initial=3)
    recom = forms.BooleanField(label='Порекомендуете ли Вы этот сайт своим друзьям?',
        required=False)
    advice = forms.CharField(label='Советы и предложения',
        widget=forms.Textarea(attrs={'rows':3,'cols':30}))
