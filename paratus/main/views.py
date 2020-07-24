from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from . import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.htm')

def basics(request):
    return render(request, 'basics.htm')

def taxes(request):
    return render(request, 'taxes.htm')

def credit(request):
    return render(request, 'creditscore.htm')

def retirement(request):
    return render(request, 'retirement.htm')

def student(request):
    return render(request, 'student.htm')

def investment(request):
    return render(request, 'investment.htm')

def stocks(request):
    return render(request, 'stocks.htm')

def property(request):
    return render(request, 'property.htm')

def bonds(request):
    return render(request, 'bonds.htm')

class SignupView(FormView):
    form_class = forms.SignUpForm
    template_name = 'signup.htm'
    success_url = reverse_lazy('main:home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(self.request.POST["password"])
        user.save()
        login(self.request, user)
        if user is not None:
            return HttpResponseRedirect(self.success_url)

        return super().form_valid(form)

class LoginView(FormView):
    form_class = forms.LoginForm
    success_url = reverse_lazy('main:home')
    template_name = 'login.htm'

    def form_valid(self, form):
        credentials = form.cleaned_data
        print(credentials)
        email = credentials['email']
        password1 = credentials['password']
        user = authenticate(username=email,
                            password=password1)
        print(user)
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            messages.add_message(self.request, messages.INFO, 'Wrong credentials\
                                please try again')
            return HttpResponseRedirect(reverse_lazy('main:login'))

def logout_user(request):
    logout(request)
    messages.info(request, "logged out")
    return redirect('main:home')

def forum(request):
    print(request)
    if request.method == 'POST' and 'post' in request.POST:
        pform = forms.PostForm(request.POST)
        if pform.is_valid():
            post = pform.save(commit=False)
            post.paratus_user = request.user
            post.save()
    elif request.method == 'POST' and 'comment' in request.POST:
        cform = forms.CommentForm(request.POST)
        print(request.POST)
        print(request.body)
        if cform.is_valid():
            comment = cform.save(commit=False)
            comment.paratus_user = request.user
            comment.paratus_post = request.POST['data']
            comment.save()
    pform = forms.PostForm()
    cform = forms.CommentForm()
    context = {
               "pform": pform,
               "cform": cform,
               "posts": ParatusPost.objects.all,
               }
    return render(request, 'forum.htm', context)


    # if request.method == 'POST':
    #     if 'post' in request.POST:
    #         pform = forms.PostForm(request.POST)
    #         if pform.is_valid():
    #             post = pform.save(commit=False)
    #             post.paratus_user = request.user
    #             post.save()
    #     elif 'comment' in request.POST:
    #         cform = forms.CommentForm(request.POST)
    #         if cform.is_valid():
    #             comment = cform.save(commit=False)
    #             # comment.paratus_user = request.user
    #             # comment.paratus_post = request.post.get("id")
    #             # comment.save()
    # pform = forms.PostForm()
    # cform = forms.CommentForm()
    # context = {
    #             "pform": pform,
    #             "cform": cform,
    #             "posts": ParatusPost.objects.all,
    #             }





    # post = form.cleaned_data
    # post.save()


    # return render(request, 'forum.htm', context)
