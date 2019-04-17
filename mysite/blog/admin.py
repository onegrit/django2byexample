from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """定制Model管理页面"""
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)} # 使用title自动填充slug字段
    raw_id_fields = ('author',)
    date_hierarchy = 'publish' # there are navigation links to navigate through a date hierarchy
    ordering = ('status', 'publish')
