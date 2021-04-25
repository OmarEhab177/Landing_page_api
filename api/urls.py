from django.urls import path
from . import views 
urlpatterns = [
    path('message-list/', views.messageList, name='message_list'),
    path('message-detail/<int:pk>/', views.messageDetail, name='message_detail'),
    path('message-create/', views.messageCreate, name='create'),
    path('message-update/<int:pk>/', views.messageUpdate, name='message_update'),
    path('message-delete/<int:pk>/', views.messageDelete, name='message_delete'),

]
