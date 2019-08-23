from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('activities/', views.ActivityListView.as_view(), name='activities'),
    path('activities/<int:pk>', views.ActivityDetailView.as_view(), name='activity-detail'),
]

urlpatterns += [
    path('activities/create/', views.ActivityCreate.as_view(), name='activity_create'),
    path('activities/<int:pk>/update/', views.ActivityUpdate.as_view(), name='activity_update'),
    path('activities/<int:pk>/delete/', views.ActivityDelete.as_view(), name='activity_delete'),
]
