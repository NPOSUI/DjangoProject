from product.models import Product
from django.db import models


class User(models.Model):

    # 用户名
    user_name = models.CharField(max_length=50)
    # 密码
    password = models.CharField(max_length=50)
    # 用户类型
    is_super = models.IntegerField(default=1)
    # 邮箱
    email = models.CharField(max_length=50)
    # 电话
    tel = models.IntegerField(default=None)
    # 地址
    address = models.CharField(max_length=200)


class Order(models.Model):

    # 订单名
    order_name = models.CharField(max_length=20)
    # 用户
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    # 产品，多对多
    product = models.ManyToManyField(Product, through='OrderProduct')
    # 订单时间
    date = models.DateTimeField(default=None)


# 订单与产品的中间表
class OrderProduct(models.Model):

    # 订单
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    # 产品
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    # 数量
    amount = models.IntegerField(default=None)


class Analysis(models.Model):

    # 订单
    order = models.ForeignKey(Order, on_delete=models.PROTECT)