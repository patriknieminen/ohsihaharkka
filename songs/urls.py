from django.urls import path

from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('view/<int:pk>', views.song_view, name='song_view'),
    path('new', views.song_create, name='song_new'),
    path('edit/<int:pk>', views.song_update, name='song_edit'),
    path('delete/<int:pk>', views.song_delete, name='song_delete'),
]