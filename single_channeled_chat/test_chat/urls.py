from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up', views.sign_up, name="sign_up"),
    path('chat_room/', views.room, name='room'),
    path('ajax/message/', views.get_data_from_js, name='ajax_message'),
]