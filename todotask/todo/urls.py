from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('add/',views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
 