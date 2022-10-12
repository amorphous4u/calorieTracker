"""calorie_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import HomePageView, LoginPage, LogoutPage, select_food, add_food, RegisterPage, ProfilePage, update_food, delete_food


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView, name='home'),
    path('login/', LoginPage, name='login'),
    path('logout/', LogoutPage, name='logout'),
    path('select_food/', select_food, name='select_food'),
    path('add_food/', add_food, name='add_food'),
    path('update_food/<str:pk>/'), update_food, name='update_food'),
# path('/', include('calories.urls')),
]
