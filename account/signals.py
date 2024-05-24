from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import Customer
from meal.models import Order
from meal.functions import orderTrxIdGen

def customer_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='customer')
		instance.groups.add(group)
        
		Customer.objects.create(
			user=instance,
			name=instance.username,
			)

		Order.objects.create(
            customer=instance.customer,
            complete=False,
            submited=False,
            transaction_id=orderTrxIdGen(),
        )
    	
		

post_save.connect(customer_profile, sender=User)
