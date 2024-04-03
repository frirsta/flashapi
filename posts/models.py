from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Author"
    )
    caption = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='flash/', blank=False, null=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_posted']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f'{self.id} {self.caption}'
