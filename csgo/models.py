from django.db import models


# Create your models here.

class CSgoUser(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=20, verbose_name='密码')

    def __str__(self):
        return self.username


class Gun(models.Model):
    name = models.CharField(max_length=50)
    cate = models.CharField(max_length=20)

    def __str__(self):
        return self.name
