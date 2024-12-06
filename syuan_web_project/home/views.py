from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("歡迎來到部落格首頁！")


def about(request):
    return HttpResponse("這是部落格的關於頁面！")
