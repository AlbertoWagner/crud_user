from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import CreateView, RedirectView
from user.forms import SignUpForm
from user.models import User
from django.contrib.auth import login as auth_login


class BasicCreateUserView(CreateView):
    template_name = 'user/signup.html'
    form_class = SignUpForm
    model = User

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('user:home')
        else:
            return render(request, 'user/signup.html', {'form': form})


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'user/home.html', {'user': request.user})


class BasicDeleteUser(RedirectView):

    def get(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        return HttpResponseRedirect(reverse('user:signup'))



