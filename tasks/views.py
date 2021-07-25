from django.views.generic.list import ListView
from django.utils import timezone
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

        if 'list_id' in self.request.GET:
            form.instance.task_list = List.objects.filter(id=self.request.GET.get('list_id')).first()

        return super(TaskCreate, self).form_valid(form)

    def get_success_url(self):

        if 'next' in self.request.GET:
            return self.request.GET.get('next')

        return super(TaskCreate, self).get_success_url()


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy('dashboard')
    form_class = TaskForm

    def post(self, request, *args, **kwargs):

        if 'next' in self.request.POST:
            self.success_url = reverse_lazy('tasks', kwargs={'task-list': self.request.POST.get('next')})

        return super(TaskUpdate, self).form_valid(request, *args, **kwargs)


class TaskDone(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy('dashboard')
    fields = ['status']

    def post(self, request, *args, **kwargs):

        if 'next' in self.request.POST:
            self.success_url = reverse_lazy('tasks', kwargs={'list_id': self.request.POST.get('next')})

        return super(TaskDone, self).post(request, *args, **kwargs)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('dashboard')
    next_page = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_page'] = self.request.GET.get('next', None)
        return context

    def get_success_url(self):
        if 'next' in self.request.GET:
            return self.request.GET.get('next')

        return super(TaskDelete, self).get_success_url()


class ActualTasks(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    paginate_by = 10
    template_name = "tasks/active_task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_id'] = self.kwargs.get('list_id')
        return context

    def get_queryset(self):
        queryset = super(ActualTasks, self).get_queryset()
        queryset = queryset.filter(
            user=self.request.user,
            status=False,
            deadline__gte=timezone.now().date()
        ).exclude(task_list__id=self.kwargs.get('list_id'))

        return queryset


class AddTaskToList(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy('dashboard')
    fields = ['task_list']

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        print(request.POST['task_list'])
        request.POST['task_list'] = List.objects.filter(id=request.POST['task_list']).first()
        return super(AddTaskToList, self).post(request, **kwargs)

    def get_success_url(self):

        if 'next' in self.request.GET:
            return self.request.GET.get('next')

        return super(AddTaskToList, self).get_success_url()