from itertools import product
from django.shortcuts import render, redirect
from .models import Meals, Order, OrderItem
from .models import optionOne, optionTwo
from .functions import orderTrxIdGen
from .decorators import unauthenticated_user

from .forms import optionOneForm, optionTwoForm

# Create your views here.


def meal_list(request):
    meals = Meals.objects.all()
    context = {
        'meals': meals,
    }
    return render(request, 'meal_list.html', context)


@unauthenticated_user
def checkout(request):
    try:
        if request.user.is_authenticated:
            customer = request.user.customer
            order = Order.objects.filter(
                customer=customer, submited=False).first()
            items = order.orderitem_set.all()
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}
    except:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {
        'items': items,
        'order': order,

    }
    return render(request, 'checkout1.html', context)


@unauthenticated_user
def createOrder(request, slug):
    reqCustomer = request.user.customer
    foodItem = Meals.objects.get(slug=slug)
    #####checking dublicate order item
    try:
        customer = request.user.customer
        customerOrder = Order.objects.get(customer=customer, submited=False)
        order = OrderItem.objects.get(order=customerOrder, product=foodItem)
        print("+++++++++++++++++++++++ duplicate finded")
        print(order)
        return redirect('meal:checkout')
    except:
        pass
    #####checking dublicate order item ended

    # selecting the top element which sumited is True or False
    customerOrder = Order.objects.filter(customer=reqCustomer).last()
    try:
        # if it is true we have to create new order(cart)
        if customerOrder.submited == True:
            reqCustomerOrder = Order.objects.create(
                customer=reqCustomer,
                complete=False,
                submited=False,
                transaction_id=orderTrxIdGen(),
            )

            reqCustomerOrderItem = OrderItem.objects.create(
                product=foodItem,
                order=reqCustomerOrder,
            )
            if foodItem.option == 1:
                reqCustomerOrderItemOption = optionOne.objects.create(
                    orderItem=reqCustomerOrderItem,
                    spicy="regular",
                )
            if foodItem.option == 2:
                reqCustomerOrderItemOption = optionTwo.objects.create(
                    orderItem=reqCustomerOrderItem,
                    spicy="regular",
                )
            return redirect('meal:update_choice', reqCustomerOrderItem.id)
        else:  # it means the order is not submited
            reqCustomerOrderItem = OrderItem.objects.create(
                product=foodItem,
                order=customerOrder,
            )
            if foodItem.option == 1:
                reqCustomerOrderItemOption = optionOne.objects.create(
                    orderItem=reqCustomerOrderItem,
                    spicy="regular",
                )
            if foodItem.option == 2:
                reqCustomerOrderItemOption = optionTwo.objects.create(
                    orderItem=reqCustomerOrderItem,
                    spicy="regular",
                )
            return redirect('meal:update_choice', reqCustomerOrderItem.id)
    except:  # there exitsts no order//firstorder
        reqCustomerOrder = Order.objects.create(
            customer=reqCustomer,
            complete=False,
            submited=False,
            transaction_id=orderTrxIdGen(),
        )

        reqCustomerOrderItem = OrderItem.objects.create(
            product=foodItem,
            order=reqCustomerOrder,
        )
        if foodItem.option == 1:
                reqCustomerOrderItemOption = optionOne.objects.create(
                    orderItem=reqCustomerOrderItem,
                    spicy="regular",
                )
        if foodItem.option == 2:
                reqCustomerOrderItemOption = optionTwo.objects.create(
                    orderItem=reqCustomerOrderItem,
                    spicy="regular",
                )
        return redirect('meal:update_choice', reqCustomerOrderItem.id)


def updateChoices(request, pk): #for option One(Try) & Two(Except) 
    #meal info start
    reqCustomer = request.user.customer

    #meal info end
    try:#adding cart for first time
        order_Item = OrderItem.objects.get(id=pk)
        detailObject = optionOne.objects.get(orderItem=order_Item)

        form = optionOneForm(instance=detailObject)

        if request.method == 'POST':
            form = optionOneForm(request.POST, instance=detailObject)
            if form.is_valid():
                form.save()
                return redirect('meal:checkout')

        content = {
            'form': form,
            'meal':order_Item,
            }
        return render(request, 'option_update_form.html', content)
        
    except:#adding same cart for second time
        order_Item = OrderItem.objects.get(id=pk)
        detailObject = optionTwo.objects.get(orderItem=order_Item)

        form = optionTwoForm(instance=detailObject)

        if request.method == 'POST':
            form = optionTwoForm(request.POST, instance=detailObject)
            if form.is_valid():
                form.save()
                return redirect('meal:checkout')

        content = {
            'form': form,
            'meal':order_Item,
            }
        return render(request, 'option_update_form.html', content)




def increaseOrderQty(request, slug):
    customer = request.user.customer
    customerOrder = Order.objects.get(customer=customer, submited=False)
    order = OrderItem.objects.get(order=customerOrder, product=slug)
    order.quantity += 1
    order.save()
    return redirect('meal:checkout')


def decreaseOrderQty(request, slug):
    customer = request.user.customer
    customerOrder = Order.objects.get(customer=customer, submited=False)
    order = OrderItem.objects.get(order=customerOrder, product=slug)
    if order.quantity == 1:
        order.delete()
        return redirect('meal:checkout')
    else:
        order.quantity -= 1
        order.save()
        return redirect('meal:checkout')


def submitOrder(request):
    customer = request.user.customer
    customerOrder = Order.objects.get(customer=customer, submited=False)
    customerOrder.submited = True
    customerOrder.save()
    return redirect('meal:meal_list')


def deleteOrderItem(request, slug):
    customer = request.user.customer
    customerOrder = Order.objects.get(customer=customer, submited=False)
    order = OrderItem.objects.get(order=customerOrder, product=slug)
    order.delete()
    return redirect('meal:checkout')
