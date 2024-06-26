from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(
        null=True, blank=True, upload_to='flash/', default='flash/default_avatar')
    website = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return self.user.username


def create_profile(sender, instance, created, **kwargs):
    """
    Create a profile for the user when a new user is created.
    """
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=get_user_model())
