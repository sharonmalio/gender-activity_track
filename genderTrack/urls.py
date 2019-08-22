from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('activities/', views.ActivityListView.as_view(), name='activities'),
    path('activity/<int:pk>', views.ActivityDetailView.as_view(), name='activity-detail'),
]
