from product.models import Product
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

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
    # 最后登录时间
    last_login = models.DateTimeField(auto_now_add=True)


class Order(models.Model):

    # 订单名
    order_name = models.CharField(max_length=20)
    # 用户
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    # 产品，多对多
    product = models.ManyToManyField(Product, through='OrderProduct')
    # 订单创建时间
    date = models.DateTimeField(default=None)


# 订单与产品的中间表
class OrderProduct(models.Model):

    # 订单
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    # 产品
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    # 数量
    amount = models.IntegerField(default=1)


# 购物车
class ShopCar(models.Model):

    # 购物车名
    name = models.CharField(max_length=100)
    # 顾客
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    # 产品
    product = models.ManyToManyField(Product, through="ShopCarProduct")
    # 购物车过期时间
    date = models.DateTimeField(default=None)


# 购物车与产品的中间表
class ShopCarProduct(models.Model):

    # 购物车
    shopcar = models.ForeignKey(ShopCar, on_delete=models.PROTECT)
    # 产品
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    # 数量
    amount = models.IntegerField(default=1)


# 公告
class NoticeBoard(models.Model):

    # 公告名称
    name = models.CharField(max_length=100)
    # 内容
    content = models.CharField(max_length=500)
    # 公告过期时间
    # date = models.TimeField()
