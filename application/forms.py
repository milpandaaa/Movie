from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class Selling_form(forms.ModelForm):
    class Meta:
        model = Selling
        fields = ['id_cassette', 'id_seller', 'id_profile', 'price']
        widgets = {
            'id_cassette': forms.TextInput(attrs={'class': 'form-control'}),
            'id_seller': forms.TextInput(attrs={'class': 'form-control'}),
            'id_profile': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SignUpForm(UserCreationForm):
    photo = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'photo', 'password1', 'password2')


class Сassette_form(forms.ModelForm):

    class Meta:
        model = Сassette
        fields = ['name', 'year', 'theme', 'price', 'duration', 'film_studio', 'producer', 'poster']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'theme': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'film_studio': forms.TextInput(attrs={'class': 'form-control'}),
            'producer': forms.TextInput(attrs={'class': 'form-control'}),
            'poster': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Seller_form(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['address']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Admission_form(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ['id_cassette', 'id_seller']
        widgets = {
            'id_cassette': forms.TextInput(attrs={'class': 'form-control'}),
            'id_seller': forms.TextInput(attrs={'class': 'form-control'}),
        }


