from django.contrib.auth.models import User
from django import forms
from . models import Recycle,Product

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'Enter password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'Enter username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}))


    class Meta:
        model = User
        fields = ['username','email','password']

class RecycleForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}))
    Description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}))
    Image = forms.FileField()
    Contact = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'contact'}))
    Address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}))
    Expected_price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}))


    class Meta:
        model = Recycle
        fields = ['Type','Description','Expected_price','Image','Name','Contact','Address','City']

class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}))
    price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'price'}))
    image = forms.FileField()


    class Meta:
        model = Product
        fields = ['name','description','price','image']






