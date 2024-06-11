from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()  # グローバル変数として扱う、ここで先に変数代入


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")
