from django.db import models
from common.models import User
from product.models import Product


# 浏览记录
class CusClickLog(models.Model):

    # 顾客
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    # 产品
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    # 点击数量
    count = models.IntegerField(default=1)


# 购买记录
class CusBusyLog(models.Model):

    # 顾客
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    # 产品
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    # 数量
    amount = models.IntegerField(default=1)
