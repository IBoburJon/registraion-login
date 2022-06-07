from forms.views import loginPage
from django.contrib import admin
from django.urls import path

from forms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.regPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
]