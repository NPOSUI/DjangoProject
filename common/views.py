import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from common.models import User
import rest_framework
import rest_framework_simplejwt

# 注册处理
def customer_register(request):

    # 检测是否是option请求
    if request.method == "OPTIONS":
        print("检测到OPTIONS")
        return HttpResponse("ok")
    else:
        # 从post请求中获取数据
        # 从QueryDict中取出数据，这个方法有点沙雕，需要改进
        print(request)
        data = request.POST.lists()
        print(data)
        for d in data:
            d1 = d
        data = d1[0]
        data = json.loads(data)

        name = data['name']
        password = data['password']
        email = data['email']
        tel = data['tel']
        address = data['address']

        return JsonResponse({'ret': 0})

        # try:
        #     customer = User.objects.create(user_name=name,
        #                                    password=password,
        #                                    is_super=1,
        #                                    email=email,
        #                                    tel=tel,
        #                                    address=address)
        # except ValueError:
        #     print("插入数据失败！！！")
        #     return JsonResponse({'ret': 1}, status=500)
        # else:
        #     return JsonResponse({'ret': 0, 'id': customer.id})


# 登录处理
def customer_login(request):
    pass