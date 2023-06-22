from django.contrib import admin
from django.utils.html import format_html

from posts.models import User, Comment, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_link', 'created_at')
    list_filter = ('created_at',)

    def author_link(self, obj):
        link = "/admin/posts/user/{}/change/".format(obj.author.id)
        return format_html('<a href="{}">{}</a>', link, obj.author.username)

    author_link.short_description = 'Автор'


admin.site.register(Post, PostAdmin)
admin.site.register(User)
admin.site.register(Comment)


