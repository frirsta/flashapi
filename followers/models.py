from django.db import models
from django.contrib.auth.models import User


class Followers(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower')

    class Meta:
        unique_together = ('user', 'follower')

    def __str__(self):
        return f'{self.user} follows {self.follower}'
