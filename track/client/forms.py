from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django import forms
from . models import Post

class user_reg(UserCreationForm):
    password1=forms.CharField(label="password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(label="password again",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=["username","first_name","last_name","email"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"})

        }
        
class user_log(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
class update_post(forms.ModelForm):
    class Meta:
        model=Post
        fields=["titel","desc"]
        labels={
            "titel":"Title","desc":"Description"
        }
        widgets={
            "titel":forms.TextInput(attrs={"class":"form-control mb-5"}),
            "desc":forms.Textarea(attrs={"class":"form-control "}),
            
        }