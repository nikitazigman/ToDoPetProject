from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.urls import reverse_lazy

from .forms import ToDoUserCreationForm, ToDoLoginForm
from django_email_verification import send_email


class CustomLoginView(LoginView):
    template_name = 'authorization/login.html'
    fields = '__all__'
    redirect_authenticated_user = False
    form_class = ToDoLoginForm


class RegisterPage(FormView):
    template_name = 'authorization/register.html'
    form_class = ToDoUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()

        if user is not None:
            login(self.request, user)

        return_val = super(RegisterPage, self).form_valid(form)

        user.is_active = False
        send_email(user)

        return return_val

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('login')

        return super(RegisterPage, self).get(*args, **kwargs)
