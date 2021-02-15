from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', { 'email': request.session.get('user') })