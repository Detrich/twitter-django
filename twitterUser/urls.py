from django.urls import path
from twitterUser.views import follow,unfollow

urlpatterns = [
    path('follow/<str:username>/<str:username2>', follow),
    path('unfollow/<str:username>/<str:username2>', unfollow)
]
