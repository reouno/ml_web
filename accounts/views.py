from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View

from accounts.forms import LoginForm
from users.models import CustomUser


class AccountLogin(View):
    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = CustomUser.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'login.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form})

account_login = AccountLogin.as_view()