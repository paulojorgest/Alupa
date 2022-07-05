from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_django
from base_site.models import Products
# Create your views here.

def homepage(request):
    product_list = Products.objects.all()
    return render(request, template_name= 'base_site/index.html',context={'product_list':product_list,})

def resgister(request):
    if request.method == 'GET':
        return render(request, template_name= 'base_site/register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('senha')

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('já existe usuario com este user name')
        user= User.objects.create_user(username = username, email= email, password=password)
        user.save()
        return HttpResponse('usuario cadastrado com sucesso!')

def login(request):
    next_page = request.POST.get('next', '/produtos')
    if request.method == "GET":
        return render(request, template_name= 'base_site/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('senha')
        user = authenticate(username=username, password=password)
        if user:
            login_django(request, user)
            return redirect('/', kwargs={'user':user})
        else:
            return HttpResponse("email ou senha informados estão incorretos")

def logout(request):
    logout_django(request)
    return redirect('/')

def product(request):
    url = request.path
    return render(request, template_name='base_site/produtos.html', context={'url_site':url})

def detail(request, slug):
    product = Products.objects.get(slug=slug)
    return render(request, template_name='base_site/detalhe.html', context= {'product':product,
                                                                             })

def pedido(request):
    return HttpResponse('Este é seu pedido')
