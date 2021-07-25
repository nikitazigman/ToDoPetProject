from datetime import date, timedelta

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
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        last_list = queryset.filter(user=self.request.user).first()

        if last_list:
            last_task_list_date = last_list.date
        else:
            last_task_list_date = self.request.user.date_joined.date()

        skipped_days: timedelta = date.today() - last_task_list_date

        for day in range(1, skipped_days.days + 1):
            time_delta = timedelta(days=day)
            task_list = List(
                date=last_task_list_date + time_delta,
                status=False,
                user=self.request.user
            )
            task_list.save()

        queryset = queryset.filter(user=self.request.user)
        data = {'lists': []}

        for row in queryset:
            data['lists'].append(
                {
                    'id': row.id,
                    'date': row.date,
                    'done': row.tasks.filter(status=True).count(),
                    'len': row.tasks.count(),
                }
            )

        queryset = data['lists']

        return queryset


class BacklogView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'dashboard/backlog.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(BacklogView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user, status=False)
        return queryset
