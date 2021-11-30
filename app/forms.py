"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class Anketa(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=50)
    gender = forms.ChoiceField(label='Ваш пол',
                               choices=[('1','мужской'),('2','женский')],
                               widget=forms.RadioSelect, initial=1)
    city = forms.CharField(label='Ваш город', min_length=3, max_length=50)
    firstmeet = forms.CharField(label='Как Вы узнали о нашем магазине?',
                              widget=forms.Textarea(attrs={'row':10, 'cols':31}))
    waiting = forms.ChoiceField(label='Ваши ожидания оправдались?', choices=[('1', 'Да'),('2', 'Нет')], widget=forms.RadioSelect, initial=1)
    raiting = forms.ChoiceField(label='Как Вы оцениваете удобство сайта?', choices=(('1', 'Плохо'), ('2', 'Хуже среднего'), ('3', 'Нормально'), ('4', 'Хорошо'), ('5', 'Отлично')), initial=1)
    recomend = forms.ChoiceField(label='Насколько легко Вам было оформить заказ?', choices=(('1', 'Сложно'), ('2', 'Легко'), ('3', 'Очень легко')), initial=1)
    message = forms.CharField(label='Что бы Вы порекомендовали изменить, учитывая ваш опыт взаимодействия с нашим сайтом?', widget=forms.Textarea(attrs={'rows':8, 'cols':31}))
    email = forms.EmailField(label='Ваш email', min_length=7)
    notice = forms.BooleanField(label='Хотите получать рассылку новостей магазина на ваш e-mail?', required=False)
    
class CommentForm (forms.ModelForm):

    class Meta:

        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm (forms.ModelForm):
    
    class Meta:

        model = Blog   #используемая модель
        fields = ('title', 'description', 'content', 'image',)  #заполнения поля
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка",} 