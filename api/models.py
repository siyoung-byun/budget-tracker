from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy
from django.conf import settings

# subclass of AbstractUser
class User(AbstractUser):

    username = models.CharField(blank=True, null=True, max_length=255)
    email = models.EmailField(ugettext_lazy('email address'), unique=True, max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
        )
    title = models.CharField(max_length=5)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
