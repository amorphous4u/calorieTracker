from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SelectFoodForm, AddFoodForm, CreateUserForm, ProfileForm
from .models import Profile, PostFood
from datetime import datetime, date, timedelta
from django.utils import timezone
from .filters import FoodFilter

# Create your views here.


@login_required(login_url='login')
def HomePageView(request):
    calories = Profile.objects.filter(person_of=request.user).last()
    calorie_goal = calories.calorie_goal

    if date.today() > calories.date:
        profile = Profile.objects.create(person_of=request.user)
        profile.save()

    calories = Profile.objects.filter(person_of=request.user).last()
    all_food_today = PostFood.objects.filter(profile=calories)

    calorie_goal_status = calorie_goal - calories.total_calorie
    over_calorie = 0
    if calorie_goal_status < 0:
        over_calorie = abs(calorie_goal_status)

    context = {
        'total_calorie': calories.total_calorie,
        'calorie_goal': calorie_goal,
        'calorie_goal_status': calorie_goal_status,
        'over_calorie': over_calorie,
        'food_selected_today': all_food_today
    }

    return render(request, 'home.html', context)


##signup page
def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'register.html', context)
