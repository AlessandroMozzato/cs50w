from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

import json
from django.core.serializers.json import DjangoJSONEncoder

from .models import Menu


toppings = ['Toppings', 'Pepperoni', 'Sausage', 'Mushrooms', 'Onions', 
'Ham', 'Canadian Bacon', 'Pineapple', 'Eggplant', 'Tomato & Basil', 'Green Peppers',
'Hamburger', 'Spinach', 'Artichoke', 'Buffalo Chicken', 'Barbecue Chicken',
'Anchovies', 'Black Olives', 'Fresh Garlic', 'Zucchini']

# Create your views here.
def index(request):
	menu = list(Menu.objects.all())

	context = {
		"items" : list(menu),
		"items_json" : json.dumps(menu, cls=DjangoJSONEncoder),
		"toppings": toppings
	}
	return render(request, "orders/index.html", context)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'orders/signup.html'