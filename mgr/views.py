from django.shortcuts import render
from django.http import HttpResponse

from mgr.models import Manager


def resdata(request):
    qs = Manager.objects.values()

    retStr = ''
    for ma in qs:
        print(type(ma), ma)
        for name, value in ma.items():
            retStr += f'{name} : {value} | '
            retStr += '<br>'
    return HttpResponse(retStr)
