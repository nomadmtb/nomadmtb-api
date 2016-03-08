from django.contrib import admin
from django.contrib.auth.models import User
from .models import Post, Link, Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Link)
admin.site.register(Profile)
