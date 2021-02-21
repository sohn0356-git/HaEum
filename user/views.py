from django.shortcuts import render, redirect, reverse

from user.models import User
from post.models import Photo
# Create your views here.

def index(request):
    user_list = User.objects.all()
    user = User.objects.filter(email=request.session.get('user'))
    photo_lists = Photo.objects.all()
    photo_list = []
    if len(photo_lists)>5:
        for p in photo_lists:
            photo_list.append(p)
            if len(photo_list)>=5:
                    break
    elif len(photo_lists)>0:
        for p in photo_lists:
            photo_list.append(p)

    res_data = {
        'user_list' : user_list,
        'photo_list' : photo_list     
        }
    if user:
        res_data['user'] = user[0]
    return render(request, 'index.html', res_data)

def login(request):
    error_msg = {}
    if request.method=="POST":
        user_id = request.POST.get('email')
        user_pw = request.POST.get('password')
        if user_id and user_pw:
            user = User.objects.filter(email=user_id)
            if user:
                if user[0].password == user_pw:
                    request.session['user'] = user_id
                    return redirect(reverse('user:index'))
                else:
                    error_msg['error'] = "아이디나 비밀번호가 잘못되었습니다."
            else:
                error_msg['error'] = "아이디나 비밀번호가 잘못되었습니다."
    return render(request, 'login.html', error_msg)

def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect(reverse('user:index'))

def mypage(request):
    user = User.objects.filter(email=request.session.get('user'))
    res_data = {"user" : user}
    if request.method=="POST":
        pass
    return render(request, 'mypage.html', res_data)