from django.shortcuts import render, redirect
from .models import ReserveTable
from .forms import reserveTableForm

from django.contrib import messages


# Create your views here.
def reservation(request):
	reservations = ReserveTable.objects.all()
	resForm = reserveTableForm()

	if request.method == 'POST':
		resForm = reserveTableForm(request.POST, request.FILES)
		if resForm.is_valid():
			new_form = resForm.save(commit=False)
			new_form.save()
			messages.info(request, 'Reservation Placed')
			return redirect('reservation:reservation-list')
		else:
			messages.info(request, 'Form is not valid.')
			return redirect('reservation:reservation-list')


	context={
		'reservations': reservations,
		'resForm' : resForm,
	}
	return render(request ,'reservation1.html', context)
