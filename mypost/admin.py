from django.contrib import admin

# Register your models here.
from django.contrib import admin
from mypost.models import Post
from mypost.models import Category

admin.site.register(Post)
admin.site.register(Category)