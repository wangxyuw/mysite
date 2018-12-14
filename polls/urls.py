from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index')
]

# @app.route('/')
# def index():
#     pass

# 先引入视图函数
# path()函数定义的路由最终都会在项目启动时加载
# path(路由检测，)
