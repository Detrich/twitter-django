from django.urls import path
from authentication.views import loginuser,logoutuser,signupuser,landing

urlpatterns = [
    path('welcome/', landing , name='landing'),
    path('login/', loginuser),
    path('logout/', logoutuser),
    path('signup/', signupuser)
]
