from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Register(UserCreationForm):
    class Meta :
        model= User
        fields=['username','email','password1','password2']
        widgets={
            'username':forms.TextInput(attrs={
                'placeholder':'username'
            }),
            'email':forms.EmailInput(attrs={
                'placeholder':'Email'
            }),
            'password1':forms.PasswordInput(attrs={
                'placeholder':'password'
            }),
            'password2':forms.PasswordInput(attrs={
                'placeholder':'Confirm passsword'
            })
        }


# class Signup(UserCreationForm):
#     class Meta:
#         model=User;
#         fields=[
#             'username',
#             'email',
#             'password1',
#             'password2',
            
#         ]
#         widgets={
#             'username':forms.TextInput(attrs={
                
#                 'placeholder':"Username",
             
#                 'name':"username",

#             }),
#             'email':forms.TextInput(attrs={
                
#                 'placeholder':"email",
                
#                 'name':"email",

#             }),
#             'password1':forms.TextInput(attrs={
                
#                 'placeholder':"password",
                
#                 'name':"password1",
                

#             }),
#             'password2':forms.TextInput(attrs={
#                 'placeholder':"COnfirm Password",
                
#                 'name':"password2",

#             })
#         }



class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=[
            'category'
        ]
        widgets={
            'category':forms.TextInput(attrs={'class':'form-control'}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['name','author','image','pages','price','rent','rent_period','price_rent','status','category']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'rent':forms.NumberInput(attrs={'class':'form-control', 'id':'rent'}),
            'rent_period':forms.NumberInput(attrs={'class':'form-control' , 'id':'rent_period'}),
            'price_rent':forms.NumberInput(attrs={'class':'form-control','id':'price_rent','disabled':'true'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }