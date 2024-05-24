from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=50,null=True)
    ph_no=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    profile_pic = models.ImageField(default="defaultPP.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"