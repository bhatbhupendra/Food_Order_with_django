from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decorators import unauthenticated_user, authenticated_user
from .forms import createMealForm

from reservation.forms import ReserveTable
from meal.models import Order, OrderItem
# Create your views here.

@authenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('account:login')
        else:
            messages.error(request,"Password is not strong")


    content = {'form':form}
    return render(request, 'signup.html', content)

@authenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password =request.POST.get('password')
        print(username)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    content = {}
    return render(request, 'signin.html', content)


def logoutUser(request):
    logout(request)
    return redirect('account:login')


def adminSection(request):
    form = createMealForm()
    if request.method == 'POST':
        form = createMealForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Meal Added.')
            return redirect('account:admin-section')
        else:
            messages.error(request,"Can't Add new Meal to list.")

    content = {
        'form': form,
    }
    return render(request, 'admin-section.html', content)

def orderSection(request):
    reservationList = ReserveTable.objects.all()
    orderList = Order.objects.filter(submited=True)
    orderListFilled = Order.objects.filter(submited=True,complete=True)
    content = {
        'reservations': reservationList,
        'orders' : orderList,
        'ordersF' : orderListFilled,
    }
    return render(request, 'order-section.html', content)

def orderInfo(request,pk):
    orderDetailItem = OrderItem.objects.filter(order=pk)
    content = {
        'items': orderDetailItem,
    }
    return render(request, 'order-detail.html', content)

# def userPage(request):
#     userInfo = request.user.profile
 
#     context = {
#         'userInfo' : userInfo,
#     }
#     return render(request, 'user-page.html', context)
