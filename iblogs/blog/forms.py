from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class OrderForm(ModelForm):

	class Meta:
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name','body')

		widgets ={
			'name':forms.TextInput(attrs={'class':'form-control'}),
			'body': forms.Textarea(attrs={'class':'form-control'}),
		}


class PostsModelForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = "__all__"
		exclude = ['likes', 'dislikes']


class CategoryModelForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = "__all__"



