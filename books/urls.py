from django.urls import path, re_path
#這邊引入方法必須相對位置，因為它並非主程式，若用絕對路徑會以主程式所在位置來啟動
from . import views

#正規表達式很強大，因為他是以格式來判定你符合哪一個api
#/35.55與555A，就可以對應到不同的API
#若不符合該re則完全不會有動作
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('myview/', views.MyView.as_view, name='myview'),
    re_path('^id/(?P<book_id>[a-zA-Z0-9]{4})/$', views.show_book_id, name='bookid'), #以分組名稱作為變數帶入後面的大小為四的字串
    re_path('^(?P<price>\d+\.\d+)/$', views.show_book_price, name='bookprice') #以分組名稱作為變數帶入一個浮點數，作為價格
]