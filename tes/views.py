from django.http import HttpResponse


def listener(request):
    return HttpResponse("测试成功！！！")
