from django import forms
from django.forms import ModelForm

from Ninjin.models import Post, Answer

class OgiriThemeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_category', 'theme_title')

class OgiriThemeImageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_category', 'image')

class ImagePostForm(ModelForm):
    class Meta:

        model = Post
        fields = ['post_category', 'image']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('text',)
