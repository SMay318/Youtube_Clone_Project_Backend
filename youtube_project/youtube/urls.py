from django.urls import path
from . import views

urlpatterns = [
    path('youtube/', views.CommentList.as_view()),
    path('youtube/<int:pk>/', views.CommentDetails.as_view())
]