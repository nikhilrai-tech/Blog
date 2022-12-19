from django.contrib import admin
from.models import Post

@admin.register(Post)
class postmodelAdmin(admin.ModelAdmin):
    list_display=["id","titel","desc"]
