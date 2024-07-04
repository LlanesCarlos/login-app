from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from .forms import (
    CustomUserCreationForm,
    UserUpdateForm,
)
from django.contrib.auth import get_user_model
from django.views.generic import (
    DetailView,
    UpdateView,
    DeleteView,
) 
from django.urls import reverse
from django.contrib.auth.views import (
    PasswordChangeView, PasswordChangeDoneView
)
from django.contrib.auth.mixins import UserPassesTestMixin

User = get_user_model()

class UserCreateAndLoginView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        raw_pw = form.cleaned_data.get("password1")
        user = authenticate(email=email, password=raw_pw)
        login(self.request, user)
        return response

class OnlyYouMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

class UserDetail(OnlyYouMixin, DetailView):
    model = User
    template_name = 'user_detail.html'
    
class UserUpdate(OnlyYouMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user_edit.html'

    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk': self.kwargs['pk']})
    
class PasswordChange(PasswordChangeView):
    template_name = 'password_change.html'


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'user_detail.html'
    
class UserDelete(OnlyYouMixin, DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('login')
    
