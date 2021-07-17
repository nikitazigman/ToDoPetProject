from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm

class TasksView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(task_list=self.kwargs.get('list_id'))
        task = context['tasks'].first()
        context['task_list_name'] = task.task_list.date
        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'task_list', 'deadline', 'difficulty']
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    # fields = ['title', 'description', 'task_list', 'deadline', 'difficulty', 'status']
    success_url = reverse_lazy('dashboard')
    form_class = TaskForm


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('dashboard')
