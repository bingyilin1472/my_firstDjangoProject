# shortcut有捷徑之意，redirect是他其中的module
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View  # 採用class-base view要繼承View物件


# Create your views here.

# 定義API函數
# func view，必須要有一個request參數
def hello(request):
    return HttpResponse('<h1>Hello, func view</h1>')


# 實踐跨站redirection to Google
# func取名上慣例似乎是小寫
def hello_google(request):
    # 其中要包含連線的協定、網址domain name，redirect是其中一種response物件
    return redirect('http://www.google.com')


# class-base view
class MyView(View):
    def get(self, request):
        return HttpResponse('<h1>class-base view</h1>')


# name 透過slug converter取得
def helloslug(request, name):
    s = '<h3>Hello, {0}!</h3>'.format(name)
    # return s，這樣會出錯，因為不是HttpResponse，只是單純的html
    # 'str' object has no attribute 'get'，意思是他無法對應你的get request
    return HttpResponse(s)


def show_path(request, path_name):
    s = '<h3>Path, {0} !</h3>'.format(path_name)
    return HttpResponse(s)


# use regular expression group to get matched arg
def show_book_id(request, book_id):
    s = '<h3>你的圖書編號: {0}</h3>'.format(book_id)
    return HttpResponse(s)


def show_book_uuid(request, book_uuid):
    s = '<h3>你的圖書編號: {0}</h3>'.format(book_uuid)
    return HttpResponse(s)


def show_book_price(request, price):
    s = '<h3>你的圖書價格: {0}</h3>'.format(price)
    # 他可以配合一些條件，條件符合才會進行redirection
    if float(price) >= 50.00:
        return redirect('price_warning', price=price)
    return HttpResponse(s)


def price_warning(request, price):
    s = '<h3>你圖書的價格高過: {0}</h3>'.format(price)
    return HttpResponse(s)