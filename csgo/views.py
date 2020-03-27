from django.shortcuts import render
from .models import CSgoUser, Gun
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .Captcha import Captcha
from django.conf import settings
import random
import re
import os


# Create your views here.
def index(request):
    username = request.session.get('user', 'Traveler')
    return render(request, 'csgo/index.html', {'username': username,
                                               'content': '欢迎光临Carrot的CSGO武器展示网站，谢谢！'})


def rifle(request):
    username = request.session.get('user', 'Traveler')
    rifle_list = Gun.objects.filter(cate='步枪')
    return render(request, 'csgo/rifle.html', {'rifle_list': rifle_list, 'username': username})


def machine_gun(request):
    username = request.session.get('user', 'Traveler')
    machine_gun_list = Gun.objects.filter(cate='机枪')
    return render(request, 'csgo/machine_gun.html', {'machine_gun_list': machine_gun_list, 'username': username})


def pistol(request):
    username = request.session.get('user', 'Traveler')
    pistol_list = Gun.objects.filter(cate='手枪')
    return render(request, 'csgo/pistol.html', {'pistol_list': pistol_list, 'username': username})


def shotgun(request):
    username = request.session.get('user', 'Traveler')
    shotgun_list = Gun.objects.filter(cate='霰弹枪')
    return render(request, 'csgo/shotgun.html', {'shotgun_list': shotgun_list, 'username': username})


def submachine_gun(request):
    username = request.session.get('user', 'Traveler')
    submachine_gun_list = Gun.objects.filter(cate='微型冲锋枪')
    return render(request, 'csgo/submachine_gun.html',
                  {'submachine_gun_list': submachine_gun_list, 'username': username})


def knife(request):
    username = request.session.get('user', 'Traveler')
    knife_list = Gun.objects.filter(cate='刀')
    return render(request, 'csgo/knife.html', {'knife_list': knife_list, 'username': username})


def register(request):
    username = request.session.get('user', 'Traveler')
    flag = request.session.get('flag', True)
    if not flag:
        del request.session['flag']
        return render(request, 'csgo/register.html', {'flag': '验证码错误，请重新输入', 'username': username})
    else:
        return render(request, 'csgo/register.html', {'username': username})


def add_gun(request):
    username = request.session.get('user', 'Traveler')
    if username == 'Traveler':
        return render(request, 'csgo/index.html', {'content': '你还未登录',
                                                   'username': username})
    else:
        return render(request, 'csgo/add_gun.html', {'username': username})


def no_register(request):
    username = request.session.get('user', 'Traveler')
    return render(request, 'csgo/index.html', {'content': '你还没有登录哦',
                                               'username': username})


def login(request):
    username = request.session.get('user', 'Traveler')
    flag = request.session.get('flag', True)
    if not flag:
        del request.session['flag']
        return render(request, 'csgo/login.html', {'flag': '验证码错误，请重新输入', 'username': username})
    else:
        return render(request, 'csgo/login.html', {'username': username})


def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('csgo:index'))


def okk_for_add_gun(request):
    username = request.session.get('user', 'Traveler')
    if request.method == 'POST':
        img = request.FILES.get('img')
        if img:
            filename = request.POST['name'] + r'.png'
            filepath = os.path.join(settings.MEDIA_ROOT, filename)
            with open(filepath, 'wb')as fp:
                for info in img.chunks():
                    fp.write(info)
            post_gun = Gun()
            post_gun.name = request.POST['name']
            post_gun.cate = request.POST['cate']
            post_gun.save()
            return render(request, 'csgo/index.html', {'content': '添加成功',
                                                       'username': username})
        else:
            return render(request, 'csgo/index.html', {'content': "添加失败，图片添加错误",
                                                       'username': username})


USERNAME_PATTERN = re.compile(r'\w{4,20}')


def okk_for_register(request):
    username = request.session.get('user', 'Traveler')
    get_code = request.POST['verify_code'].upper()
    code = request.session.get('verify_code').upper()
    username_r = request.POST['username']
    password = request.POST['password']
    if get_code == code:
        if not USERNAME_PATTERN.fullmatch(username):
            return render(request, 'csgo/index.html', {'content': '用户名由字母、数字和下划线构成且长度为4-20个字符',
                                                       'username': username})
        if len(password) < 4 or len(password) > 20:
            return render(request, 'csgo/index.html', {'content': '无效的密码，密码长度必须在4~20之间',
                                                       'username': username})
        new_user = CSgoUser()
        new_user.username = username_r
        new_user.password = password
        new_user.save()
        return render(request, 'csgo/index.html', {'content': '注册成功',
                                                   'username': username})
    else:
        request.session['flag'] = False
        return HttpResponseRedirect(reverse('csgo:register'))


def okk_for_login(request):
    username = request.session.get('user', 'Traveler')
    get_username = request.POST['username']
    get_password = request.POST['password']
    get_code = request.POST['verify_code'].upper()
    code = request.session.get('verify_code').upper()
    if get_code == code:
        try:
            user = CSgoUser.objects.get(username=get_username)
        except CSgoUser.DoesNotExist as e:
            return render(request, 'csgo/index.html', {'content': '登录失败，用户名错误',
                                                       'username': username})
        else:
            if get_password == user.password:
                request.session['user'] = get_username
                return HttpResponseRedirect(reverse('csgo:index'))
            else:
                return render(request, 'csgo/index.html', {'content': '登录失败，密码错误',
                                                           'username': username})
    else:
        request.session['flag'] = False
        return HttpResponseRedirect(reverse('csgo:login'))


ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_verify_code(request):
    selected_chars = random.choices(ALL_CHARS, k=4)
    selected_chars = ''.join(selected_chars)
    request.session['verify_code'] = selected_chars
    image = Captcha.instance(width=200, height=60).generate(selected_chars)
    return HttpResponse(image, content_type='image/png')
