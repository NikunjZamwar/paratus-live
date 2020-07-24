from django import forms
from .models import *

class SignUpForm(forms.ModelForm):
    # class Meta:
    #     model = ParatusUser
    #     fields = ['name', 'email', 'password']
    #     widgets = {
    #             'password': forms.PasswordInput(),
    #     }
    class Meta:
        model = ParatusUser
        fields = ('first_name','last_name', 'email', 'password',)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput())

class PostForm(forms.ModelForm):
    class Meta:
        model = ParatusPost
        fields = ('paratus_message',)
        widgets = {'paratus_message': forms.Textarea(attrs={'rows':4, 'cols':15}), }

class CommentForm(forms.ModelForm):
    class Meta:
        model = ParatusComment
        fields = ('comment',)
        widgets = {'comment': forms.Textarea(attrs={'rows':4, 'cols':15}), }
