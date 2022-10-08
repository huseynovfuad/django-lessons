from django.contrib import admin
from .models import Blog, Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):

    class Meta:
        model = Category

    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)


admin.site.register(Category, CategoryAdmin)


class BlogAdmin(admin.ModelAdmin):

    class Meta:
        model = Blog

    list_display = ("category", "title", "created_at", "updated_at")
    search_fields = ("title", )
    list_filter = ("category", )


admin.site.register(Blog, BlogAdmin)