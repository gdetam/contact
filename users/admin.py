from django.contrib import admin

from .models import CustomUser, UsersLikes

admin.site.register(CustomUser)
admin.site.register(UsersLikes)
