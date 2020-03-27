from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=20, verbose_name='密码')

    def __str__(self):
        return self.username


class Category(models.Model):
    cate = models.CharField(max_length=50)

    def __str__(self):
        return self.cate


class Weapon(models.Model):
    which_cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    gun = models.CharField(max_length=50)

    def __str__(self):
        return self.gun


