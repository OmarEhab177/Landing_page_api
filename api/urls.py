from django.urls import path
from .views import MessageListView, MessageDetailView 
urlpatterns = [
    path('message/', MessageListView.as_view(), name='message'),
    path('message/<str:pk>/', MessageDetailView.as_view(), name='message-detail')




    # path('message-list/', views.messageList, name='message_list'),
    # path('message-detail/<int:pk>/', views.messageDetail, name='message_detail'),
    # path('message-create/', views.messageCreate, name='create'),
    # path('message-update/<int:pk>/', views.messageUpdate, name='message_update'),
    # path('message-delete/<int:pk>/', views.messageDelete, name='message_delete'),

]
