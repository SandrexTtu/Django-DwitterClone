from django.urls import path
from .views import TweetListView,TweetCreateView,TweetUpdateView,TweetDeleteView
urlpatterns = [

    path('',TweetListView.as_view(),name = 'home'),
    path('create/',TweetCreateView.as_view(),name = 'Tweetcreate'),
    path('tweet/<int:pk>/update',TweetUpdateView.as_view(),name = 'Tweetupdate'),
    path('tweet/<int:pk>/delete',TweetDeleteView.as_view(),name = 'Tweetdelete'),
    

]