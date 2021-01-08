import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from common.models import User


# 注册处理
def customer_register(request):

    # return JsonResponse({'ret': 0})

    # 检测是否是option请求
    if request.method == "OPTIONS":
        print("检测到OPTIONS")
        return HttpResponse("ok")
    else:
        # 从post请求中获取代码
        data = request.POST.lists()

        name = request.POST.get("name")
        password = request.POST.get("password")
        email = request.POST.get("email")
        tel = request.POST.get("tel")
        address = request.POST.get("address")

        # data1 = data.keys()
        for d in data:
            d1 = d

        d2 = d1[0]
        d3 = d2
        print(d3)
        print(type(d3))

        # print(type(data))
        # print(name)
        if not name:
            # print("name为空")
            return JsonResponse({'ret': 0}, status=403)
        else:
            customer = User.objects.create(user_name=name,
                                           password=password,
                                           is_super=1,
                                           email=email,
                                           tel=tel,
                                           address=address)

            return JsonResponse({'ret': 0, 'id': customer.id})
