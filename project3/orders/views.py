from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.views import generic

import json
from django.core.serializers.json import DjangoJSONEncoder

from .models import Menu, Order

import logging

toppings = ['Toppings', 'Pepperoni', 'Sausage', 'Mushrooms', 'Onions', 
'Ham', 'Canadian Bacon', 'Pineapple', 'Eggplant', 'Tomato & Basil', 'Green Peppers',
'Hamburger', 'Spinach', 'Artichoke', 'Buffalo Chicken', 'Barbecue Chicken',
'Anchovies', 'Black Olives', 'Fresh Garlic', 'Zucchini']

# Create your views here.
def index(request):    
	logger = logging.getLogger('applog')
	menu = list(Menu.objects.all())

	context = {
		"class_names" : list(set(item.class_name for item in menu)),
		"items" : list(menu),
		"toppings": toppings
	}
	return render(request, "orders/index.html", context)

def submit_order(request):
	logger = logging.getLogger('applog')
	cart = request.POST['cart']
	cart = json.loads(cart)
	
	items = []
	total = 0
	for j in cart.keys():
		total += float(cart[j]['price'])
		topps = ''
		if cart[j]['n_toppings'] > 0:
			topps = ' - '+', '.join(cart[j]['toppings'])

		item = cart[j]['class_name'] + ' - ' + cart[j]['name'] + ' - ' + cart[j]['price'] + topps
		items.append(item)
	items = '; '.join(items)
	items_in_menu = max([int(k) for k in cart.keys()])

	f = Order(user=request.user.username, items_in_menu=items_in_menu, total=total, items=items)
	f.save()

	return HttpResponseRedirect(reverse("index"))

class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'orders/signup.html'