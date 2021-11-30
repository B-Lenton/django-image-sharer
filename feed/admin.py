from django.contrib import admin
from .models import Post

# connect Post with PostAdmin, which inherits everything from admin.ModelAdmin
class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)