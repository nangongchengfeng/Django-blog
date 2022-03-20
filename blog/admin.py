from django.contrib import admin

from django.contrib import admin
from django.utils import timezone

from .models import Post, Category, Tag

admin.site.site_header = "Blog博客-Joker"
admin.site.index_title = "Blog博客-Joker"
class PostAdmin(admin.ModelAdmin):
    # 文章展示列表
    list_display = ['title','excerpt','views' ,'created_time', 'modified_time', 'category', 'author']
    # 还有一个 fields 属性，则用来控制表单展现的字段
    fields = ['title', 'body', 'category', 'tags']
    search_fields = ['title', 'body']
    list_filter = ('created_time',)
    ordering = ['created_time']
    # 创建时间，作者
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        #obj.modified_time = timezone.now()
        super().save_model(request, obj, form, change)


# 把新增的 Postadmin 也注册进来
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
