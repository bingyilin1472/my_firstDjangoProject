from django.shortcuts import render
from django.http import HttpResponse
from django.views import View  # 採用class-base view要繼承View物件


# Create your views here.

# 定義API函數
def hello(request):
    return HttpResponse('<h1>Hello, func view</h1>')


class MyView(View):
    def get(self, request):
        return HttpResponse('<h1>class-base view</h1>')


def show_book_id(request, book_id):
    s = '<h3>你的圖書編號: {0}</h3>'.format(book_id)
    return HttpResponse(s)


def show_book_price(request, price):
    s = '<h3>你的圖書價格: {0}</h3>'.format(price)
    return HttpResponse(s)
