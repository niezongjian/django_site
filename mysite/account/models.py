from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#注册时员工信息数据库
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    employee_num = models.CharField(max_length=20, null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)


class UserInfo(models.Model):
    user = models.OneToOneField(User, unique=True)
    department = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    group = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    aboutme = models.TextField(blank=True)

    def __str__(self):
        return  "user:{}".format(self.user.username)
