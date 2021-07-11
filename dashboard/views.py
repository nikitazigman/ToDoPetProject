from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import List
from tasks.models import Task


class ListsView(LoginRequiredMixin, ListView):
    model = List
    context_object_name = 'lists'
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = context['lists'].filter(user=self.request.user)
        return context


class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = List
    context_object_name = 'list'
    success_url = reverse_lazy('dashboard')


class BacklogView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'dashboard/backlog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['tasks'])
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        print(context['tasks'])
        return context
