# from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm


class SignupView(CreateView):
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("tweets:home")  # リダイレクト先url貼付、success_url使用時遅延評価でurl逆引き

    def from_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_deta["username"]
        password = form.cleaned_deta["password1"]   # passwordだとエラー、formのフィールドにpasswordというフィールドがない
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return response

# エラー箇所あと一個？
