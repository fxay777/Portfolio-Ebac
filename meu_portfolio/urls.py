from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('projetos/', views.projetos, name='projetos'),
    path('contato/', views.contato, name='contato'),
]
