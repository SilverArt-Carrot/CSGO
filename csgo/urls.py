from django.urls import path
from . import views

app_name = 'csgo'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_gun/', views.add_gun, name='add_gun'),
    path('knife/', views.knife, name='knife'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('machine_gun/', views.machine_gun, name='machine_gun'),
    path('pistol/', views.pistol, name='pistol'),
    path('register/', views.register, name='register'),
    path('rifle/', views.rifle, name='rifle'),
    path('shotgun/', views.shotgun, name='shotgun'),
    path('submachine_gun/', views.submachine_gun, name='submachine_gun'),
    path('no_register/', views.no_register, name='no_register'),
    path('okk_for_add_gun/', views.okk_for_add_gun, name='okk_for_add_gun'),
    path('okk_for_register/', views.okk_for_register, name='okk_for_register'),
    path('okk_for_login/', views.okk_for_login, name='okk_for_login'),
    path('get_verify_code/', views.get_verify_code, name='get_verify_code'),
]
