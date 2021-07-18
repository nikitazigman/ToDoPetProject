from django.urls import path
from .views import *

urlpatterns = [
    path('<int:list_id>/', TasksView.as_view(), name='tasks'),
    path('task-create/<int:list_id>/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]