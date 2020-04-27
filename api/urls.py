from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_form, name='login'),
    path('logout/', views.logout_form, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('api/', views.retrieve_data, name='retrieve_data'),
    path('visualization/', views.visualization, name='visualization')

]