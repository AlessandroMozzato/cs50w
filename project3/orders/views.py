from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.views import generic

import json
from django.core.serializers.json import DjangoJSONEncoder
import os

from .models import Menu, Order
import logging

import stripe

stripe_keys = {
  'secret_key': os.environ['SECRET_KEY'],
  'publishable_key': os.environ['PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

# Create your views here.
def index(request):    
	logger = logging.getLogger('applog')
	menu = list(Menu.objects.all())

	context = {
		"class_names" : ['Regular Pizza', 'Sicilian Pizza', 'Subs', 'Pasta', 'Salads', 'Dinner Platters'],
		"items" : list(menu),
		
	}
	return render(request, "orders/index.html", context)

def confirm_order(request):
	total = request.POST['cart']

	context = {
		"key" : stripe_keys['publishable_key'],
		"total" : total
	}

	return render(request, "orders/submit.html", context)

def submit_order(request):
	cart = request.POST['subcart']
	print(cart)
	cart = json.loads(cart)
	items = []
	total = 0
	for j in cart.keys():
		total += float(cart[j]['price'])
		topps = ''
		if cart[j]['n_toppings'] > 0:
			topps = ' - '+', '.join(cart[j]['toppings'])

		item = cart[j]['class_name'] + ' - ' + cart[j]['name'] + ' - ' + str(cart[j]['price']) + topps
		items.append(item)
	items = '; '.join(items)
	items_in_menu = max([int(k) for k in cart.keys()])

	f = Order(user=request.user.username, items_in_menu=items_in_menu, total=total, items=items)
	f.save()

	customer = stripe.Customer.create(
		email= request.user.username,
		source=request.POST['stripeToken']
	)

	charge = stripe.Charge.create(
		customer=customer.id,
		amount=total,
		currency='eur',
		description="Charge for {}".format(request.user.username),
	)

	return HttpResponseRedirect(reverse("index"))

class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'orders/signup.html'