from django.shortcuts import render

from user.models import User
from post.models import Photo
# Create your views here.

def index(request):
    user_list = User.objects.all()
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
        'photo_list' : photo_list,
        'email': request.session.get('user')        
        }
    return render(request, 'index.html', res_data)