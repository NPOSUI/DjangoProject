from django.shortcuts import render
from django.http import HttpResponse


def listener(request):
    return HttpResponse("测试成功！！！")