from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm
from dashboard.models import List


class TasksView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(task_list=self.kwargs.get('list_id'))
        context['list'] = List.objects.filter(id=self.kwargs.get('list_id')).first()
        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    success_url = reverse_lazy('dashboard')
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.task_list = List.objects.filter(id=self.kwargs.get('list_id')).first()
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy('dashboard')
    form_class = TaskForm


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('dashboard')
