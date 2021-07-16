from django.urls import path
from .views import *

urlpatterns = [
    path('', ListsView.as_view(), name='dashboard'),
    path('backlog/', BacklogView.as_view(), name='backlog'),
]