from django.urls import path
from .views import *

urlpatterns = [
    path('<int:list_id>/', TasksView.as_view(), name='tasks'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('task-done/<int:pk>', TaskDone.as_view(), name='task-done'),
    path('task-actual/<int:list_id>/', ActualTasks.as_view(), name='task-actual'),
    path('task-add-to-list/<int:pk>/', AddTaskToList.as_view(), name='task-add-to-list'),
]
