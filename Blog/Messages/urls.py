from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Principal, name='Principal'),
    path('inbox/<str:username>/', InboxView.as_view(), name='inbox'),
    path('Bandeja/',MessageListView.as_view(), name='messages_list' ),
    path('EnviarMensaje/',BuscarUsuarios, name='EnviarMensaje' ),
    path('BuscarUsuarios/',BuscarUsuarios, name='BuscarUsuarios' ),
    
    
]