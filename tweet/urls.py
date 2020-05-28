from django.urls import path
from tweet.views import MakeTweet,maintweets,profiletweets,singletweet


urlpatterns = [
    path("" , maintweets, name='homepage'),
    path("<str:username>/<int:id>/", singletweet),
    path("<str:username>/", profiletweets, name='profile'),
    path("<str:username>/NEW", MakeTweet)
]
