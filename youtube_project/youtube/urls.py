from django.urls import path
from . import views

urlpatterns = [
    path('youtube/', views.CommentList.as_view()),
    path('reply/', views.ReplyList.as_view()), 
    path('youtube/<int:pk>/', views.CommentDetails.as_view()),
    path('reply/<int:pk>/', views.ReplyDetails.as_view())
]