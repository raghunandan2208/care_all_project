from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
    is_younger = models.BooleanField(default=False)
    is_elder = models.BooleanField(default=False)
    bio = models.CharField(max_length=250, blank=True)


class Younger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    earnings = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Elder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    need_help = models.BooleanField(default=False)
    funds = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def add_fund(self, amount):
        self.funds += amount


class YoungerRequest(models.Model):
    request_by = models.ForeignKey(Younger, on_delete=models.CASCADE, related_name='request_by')
    request_to = models.ForeignKey(Elder, on_delete=models.CASCADE, related_name='request_to')
    date_requested = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.request_by.user.username}- to -{self.request_to.user.username}"


class ElderApproval(models.Model):
    approved_by = models.ForeignKey(Elder, on_delete=models.CASCADE, related_name='approved_by', null=True)
    approved_to = models.ForeignKey(Younger, on_delete=models.CASCADE, related_name='approved_to')
    date_approved = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.approved_to.user.username}"


class Profile(models.Model):
    sex = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_younger_profile = models.BooleanField(default=False)
    is_elder_profile = models.BooleanField(default=False)
    display_name = models.CharField(max_length=20, db_index=True)
    first_name = models.CharField(max_length=50, default='First name')
    last_name = models.CharField(max_length=50, default='Last name')
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, choices = sex)
    location = models.CharField(max_length=50, default=0)
    mobile = models.IntegerField(default=0)
    email = models.EmailField(default=0)
    address = models.TextField(max_length=500,default=0)
    about_me = models.TextField(max_length=500,default=0)
    image = models.ImageField(upload_to='profile/', default='profile/default-profile.jpg')
    is_filled = models.BooleanField(blank=True, null=True, verbose_name="I accept that the above given information is True")

    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse('profile', kwargs={'user':self.user})


class Transactions(models.Model):
    care_seeker = models.ForeignKey(Elder, on_delete=models.CASCADE)
    care_giver = models.ForeignKey(Younger, on_delete=models.CASCADE)
    date_approved = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(auto_now=False,blank=True,null=True)
    duration = models.IntegerField(default=0, blank=True, null=False)
    amount_to_pay = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f'{self.care_seeker.user.username, self.care_giver.user.username, self.date_approved}'


class Completed(models.Model):
    care_to = models.ForeignKey(Elder, on_delete=models.CASCADE)
    care_by = models.ForeignKey(Younger, on_delete=models.CASCADE)
    date_started = models.DateTimeField(auto_now=False, blank=True, null=True)
    scheduled_end_date = models.DateTimeField(auto_now=False, blank=True, null=True)
    date_ended = models.DateTimeField(auto_now=False, blank=True, null=True)
    duration = models.IntegerField(default=0, blank=True, null=False)
    amount_paid = models.IntegerField(default=0, blank=True)
