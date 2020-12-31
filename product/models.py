from django.db import models
import datetime


class Comment(models.Model):

    # id
    id = models.IntegerField(primary_key=True,)
    # 评论类型
    co_type = models.CharField(max_length=10)
    # 内容
    content = models.CharField(max_length=200)
    # 时间
    date = models.DateTimeField(default=datetime.datetime.now())


class Product(models.Model):

    # 商品名称
    name = models.CharField(max_length=50)
    # 商品类型
    type = models.CharField(max_length=50)
    # 价格
    price = models.IntegerField(default=10)
    # 销量
    sales_vol = models.IntegerField(default=100)
    # 单位
    unit = models.CharField(max_length=10)
    # 发货地址
    address = models.CharField(max_length=100)
    # 库存
    repertory = models.IntegerField(default=100)
    # 描述
    des = models.CharField(max_length=500)
    # 评论id
    com_id = models.ForeignKey(Comment, on_delete=models.PROTECT)
    # 图片
    # pic = models.ImageField()


