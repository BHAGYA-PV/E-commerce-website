from django import forms
from .models import *



class category(forms.ModelForm):
    class Meta:
        model=categories
        fields=("name","image")
        widgets={
            "image":forms.FileInput(attrs={'accept': '*'})
            
            }



class FileModelForm(forms.ModelForm):
    class Meta:
        model=product
        fields=("name","price","image","categories")
        widgets={
            "image":forms.FileInput(attrs={'accept': '*'})
            
            }


class RegsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    adress = forms.CharField(max_length=200)
    city = forms.CharField(max_length=50)
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        
class LogsForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput())