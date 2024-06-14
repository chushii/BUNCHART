from django.contrib import admin
from .models import articles, pictures, comments

admin.site.register(articles)
admin.site.register(pictures)
admin.site.register(comments)