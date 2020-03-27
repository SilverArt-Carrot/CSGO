from django.urls import path
from . import views

app_name = 'weapon'
urlpatterns = [
    path('', views.index, name='index'),
    path('content/', views.content, name='content'),
    path('testpost/', views.testpost, name='testpost'),
    path('weapons/<int:cate_id>/', views.weapons, name='weapons'),
    path('okk/', views.okk, name='okk'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('okk2/', views.okk2, name='okk2'),
    path('okk3/', views.okk3, name='okk3'),
    path('get_verify_code/', views.get_verify_code, name='get_verify_code'),
]
