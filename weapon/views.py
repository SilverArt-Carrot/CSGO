from django.shortcuts import render
from .models import Category, Weapon, User
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .Captcha import Captcha
import random
import re


# Create your views here.
def index(request):
    username = request.session.get('user', '游客')
    return render(request, 'weapon/index.html', {'username': username, })


def content(request):
    return render(request, 'weapon/content.html', {'weapon_category_list': Category.objects.all()})


def weapons(request, cate_id):
    cate = Category.objects.get(pk=cate_id)
    weapons_list = []
    for weapon in cate.weapon_set.all():
        weapons_list.append(weapon.gun)
    return JsonResponse({'data': weapons_list})


# class ContentView(generic.DetailView):
#     model = Category
#     template_name = 'weapon/content.html'
#     context_object_name = 'ccc'


def testpost(request):
    username = request.session.get('user', '游客')
    if username == '游客':
        return HttpResponse('你还没有登录哦')
    else:
        return render(request, 'weapon/testpost.html')


def okk(request):
    print(request.POST['gun'])
    print(request.POST['which_cate'])
    post_gun = Weapon()
    try:
        cate = Category.objects.get(cate=request.POST['which_cate'])
    except Category.DoesNotExist as e:
        return HttpResponse('没有这种类型的枪啦')
    else:
        post_gun.gun = request.POST['gun']
        post_gun.which_cate = cate
        post_gun.save()
        return HttpResponse('添加成功了哦')


USERNAME_PATTERN = re.compile(r'\w{4,20}')


def okk2(request):
    get_code = request.POST['verify_code'].upper()
    code = request.session.get('verify_code').upper()
    username = request.POST['username']
    password = request.POST['password']
    if get_code == code:
        # form = UserForm(request.POST)
        # if form.is_valid():
        #     form.save()
        if not USERNAME_PATTERN.fullmatch(username):
            return HttpResponse('用户名由字母、数字和下划线构成且长度为4-20个字符')
        if len(password) <= 8 or len(password) >= 20:
            return HttpResponse('无效的密码，密码长度必须在8~20之间')
        new_user = User()
        new_user.username = username
        new_user.password = password
        new_user.save()
        return HttpResponse('注册成功了')
    else:
        request.session['flag'] = False
        return HttpResponseRedirect(reverse('weapon:register'))


def okk3(request):
    get_username = request.POST['username']
    get_password = request.POST['password']
    get_code = request.POST['verify_code'].upper()
    code = request.session.get('verify_code').upper()
    if get_code == code:
        try:
            user = User.objects.get(username=get_username)
        except User.DoesNotExist as e:
            return HttpResponse('用户名错误')
        else:
            if get_password == user.password:
                request.session['user'] = get_username
                return HttpResponseRedirect(reverse('weapon:index'))
            else:
                return HttpResponse('密码错误')
    else:
        request.session['flag'] = False
        return HttpResponseRedirect(reverse('weapon:login'))


def register(request):
    flag = request.session.get('flag', True)
    if not flag:
        del request.session['flag']
        return render(request, 'weapon/register.html', {'flag': '验证码错误，请重新输入'})
    else:
        return render(request, 'weapon/register.html')


def login(request):
    flag = request.session.get('flag', True)
    if not flag:
        del request.session['flag']
        return render(request, 'weapon/login.html', {'flag': '验证码错误，请重新输入'})
    else:
        return render(request, 'weapon/login.html')


def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('weapon:index'))


ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_verify_code(request):
    selected_chars = random.choices(ALL_CHARS, k=4)
    selected_chars = ''.join(selected_chars)
    request.session['verify_code'] = selected_chars
    image = Captcha.instance(width=200, height=60).generate(selected_chars)
    return HttpResponse(image, content_type='image/png')
