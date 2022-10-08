from django.db import models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Comments(models.Model):
    comment = models.TextField()


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="blog_category",
                                 related_query_name="")
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    price = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
