"""my_firstDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#以django.urls中的include來實作，會省去一些路徑上的麻煩(相對/絕對)
#類似flask blueprint，可以管制多組api，差別只是它是一個app一組apis
#多個apps，建立上Django有其優勢
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')) #利用這個可以利用urls對不同用app分層級
]
