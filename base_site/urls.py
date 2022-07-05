from django.urls import path
from . import views

app_name = 'base_site'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('login/', views.login, name= 'login'),
    path('cadastro/', views.resgister, name='register'),
    path('produtos/<slug:slug>', views.detail, name='detail' ),
    path('logout/', views.logout, name='logout'),
    path('pedido/', views.pedido, name='pedido'),

]