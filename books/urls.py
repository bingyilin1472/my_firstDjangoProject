from django.urls import path, re_path
# 這邊引入方法必須相對位置，因為它並非主程式，若用絕對路徑會以主程式所在位置來啟動
from . import views

# 正規表達式很強大，因為他是以格式來判定你符合哪一個api
# /35.55與555A，就可以對應到不同的API
# 若不符合該re則完全不會有動作
# re數字能比較豐富，相對int converter

# class-base要注意，他是以as_view方法當作進入點，是要.as_view()，呼叫的方式，不能省()

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('myview/', views.MyView.as_view(), name='myview'),
    re_path('^show_book_id/(?P<book_id>[a-zA-Z0-9]{4})/$', views.show_book_id, name='show_book_id'),
    path('show_book_uuid/<uuid:book_uuid>/', views.show_book_uuid, name='show_book_uuid'),
    re_path('^show_book_price/(?P<price>\d+\.\d+)/$', views.show_book_price, name='show_book_price'),
    path('show_path/<path:path_name>/', views.show_path, name='show_path'),
    path('helloslug/<str:name>/', views.helloslug, name='hello_slug'),
    path('hello_google/', views.hello_google, name='hello_google'),
    re_path('^price_warning/(?P<price>\d+\.\d+)/$', views.price_warning, name='price_warning'),
    path('info/', views.MyRedirectView.as_view(), name='MyRedirectView'),
    path('show_book_info/', views.show_book_info, name='book_info')
]
