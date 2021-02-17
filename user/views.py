from django.shortcuts import render

from user.models import User
# Create your views here.

def index(request):
    user_list = User.objects.all()
    res_data = {'user_list' : user_list, 'email': request.session.get('user')}
    return render(request, 'index.html', res_data)