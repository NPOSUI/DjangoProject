from django.db import models


class Manager(models.Model):
    # 名称
    name = models.CharField(max_length=200)
    # 密码
    password = models.CharField(max_length=200)
    # 权限等级
    grade = models.CharField(max_length=5)

