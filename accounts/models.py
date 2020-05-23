from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    address = models.CharField(max_length=255, blank=False)
    address_2 = models.CharField(max_length=150, blank=True)
    contact = models.PositiveIntegerField(blank=False)
    user =models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "UserProfile" + str(self.id)