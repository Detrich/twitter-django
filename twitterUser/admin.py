from django.contrib import admin
from twitterUser.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(TwitterUser, UserAdmin)

