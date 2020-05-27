from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    website = models.URLField(blank=True)
    tagline = models.TextField(default='Tagline here')
    perks = models.TextField(blank=True)
    skills = models.TextField()
    status = models.CharField(max_length=50, default='Applied')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resume_company', blank=True)
    date_applied = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name + ' for user: ' +  self.user.username

    def get_absolute_url(self):
        return reverse('i_blog_userinfo')


class Extra(models.Model):
    heading = models.CharField(max_length=100)
    para = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.heading
