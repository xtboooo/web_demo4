from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=128, verbose_name='密码')
    gender = models.BooleanField(default=False, verbose_name='性别')
    age = models.IntegerField(default=18, verbose_name='年龄')
    mobile = models.CharField(max_length=11, null=True, verbose_name='电话')
    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户表'
