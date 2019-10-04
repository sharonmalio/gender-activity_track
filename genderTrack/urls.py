from django.urls import path
# from django.contrib.auth import views
from django.urls import include
from . import views

# from myapp import views as myapp_views


urlpatterns = [
    path('', views.index, name='index'),
    path('activities/', views.ActivityListView.as_view(), name='activities'),
    path('select_outcome/calculate/', views.ActivityCalculateView.as_view(), name='activity_calculate'),
    path('activities/<int:pk>', views.ActivityDetailView.as_view(), name='activity_detail'),
]

urlpatterns += [
    path('activities/create/', views.ActivityCreate.as_view(), name='activity_create'),
    path('activities/<int:pk>/update/', views.ActivityUpdate.as_view(), name='activity_update'),
    path('activities/<int:pk>/delete/', views.ActivityDelete.as_view(), name='activity_delete'),
]


