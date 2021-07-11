from django.urls import path
from .views import *

urlpatterns = [
    path('', ListsView.as_view(), name='dashboard'),
    path('list-delete/<int:pk>/', ListDeleteView.as_view(), name='list-delete'),
    path('backlog/', BacklogView.as_view(), name='backlog'),
]