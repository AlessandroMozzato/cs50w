from django.db import models

# Create your models here.
class Menu(models.Model):
	class_name = models.CharField(max_length=30)
	name = models.CharField(max_length=30)
	num_toppings = models.CharField(max_length=30)
	size = models.BooleanField(default=True)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	price_big = models.DecimalField(max_digits=5, decimal_places=2, null=True)


"""
Menu(class_name='Regular Pizza', name='Cheese', num_toppings=0, size=True, price=12.20, price_big=17.45)
Menu(class_name='Regular Pizza', name='1 topping', num_toppings=1, size=True, price=13.20, price_big=19.45)
Menu(class_name='Regular Pizza', name='2 toppings', num_toppings=2, size=True, price=14.70, price_big=23.45)
Menu(class_name='Regular Pizza', name='3 toppings', num_toppings=3, size=True, price=15.70, price_big=17.45)
Menu(class_name='Regular Pizza', name='Special', num_toppings=30, size=True, price=17.25, price_big=25.45)
		
Menu(class_name='Sicilian Pizza', name='Cheese', num_toppings=0, size=True, price=23.45, price_big=37.70)
Menu(class_name='Sicilian Pizza', name='1 topping', num_toppings=1, size=True, price=25.45, price_big=39.70)
Menu(class_name='Sicilian Pizza', name='2 toppings', num_toppings=2, size=True, price=27.45, price_big=41.70)
Menu(class_name='Sicilian Pizza', name='3 toppings', num_toppings=3, size=True, price=28.45, price_big=43.70)
Menu(class_name='Sicilian Pizza', name='Special', num_toppings=30, size=True, price=29.45, price_big=44.70)

Menu(class_name='Subs', name='Cheese', num_toppings=0, size=True, price=6.50, price_big=7.95)
Menu(class_name='Subs', name='Italian', num_toppings=0, size=True, price=6.50, price_big=7.95)
Menu(class_name='Subs', name='Ham + Cheese', num_toppings=0, size=True, price=6.50, price_big=7.95)
Menu(class_name='Subs', name='Meatball', num_toppings=0, size=True, price=6.50, price_big=7.95)
Menu(class_name='Subs', name='Tuna', num_toppings=0, size=True, price=6.50, price_big=7.95)
Menu(class_name='Subs', name='Turkey', num_toppings=0, size=True, price=7.50, price_big=8.50)
Menu(class_name='Subs', name='Chicken Parmigiana', num_toppings=0, size=True, price=7.50, price_big=8.50)
Menu(class_name='Subs', name='Eggplant Parmigiana', num_toppings=0, size=True, price=6.50, price_big=7.95)
Menu(class_name='Subs', name='Steak', num_toppings=0, size=True, price=6.50, price_big=7.95)
Menu(class_name='Subs', name='Steak + Cheese', num_toppings=0, size=True, price=6.95, price_big=8.50)
Menu(class_name='Subs', name='Sausage, Peppers & Onions', num_toppings=0, size=True, price=8.50)
Menu(class_name='Subs', name='Hamburger', num_toppings=0, size=True, price=4.60, price_big=6.95)
Menu(class_name='Subs', name='Cheeseburger', num_toppings=0, size=True, price=5.10, price_big=7.45)
Menu(class_name='Subs', name='Fried Chicken', num_toppings=0, size=True, price=6.95, price_big=8.50)
Menu(class_name='Subs', name='Veggie', num_toppings=0, size=True, price=6.95, price_big=8.50)

Menu(class_name='Pasta', name='Baked Ziti w/Mozzarella', num_toppings=0, size=False, price=6.50)
Menu(class_name='Pasta', name='Baked Ziti w/Meatballs', num_toppings=0, size=False, price=8.75)
Menu(class_name='Pasta', name='Baked Ziti w/Chicken', num_toppings=0, size=False, price=9.75)

Menu(class_name='Salads', name='Garden Salad', num_toppings=0, size=False, price=6.25)
Menu(class_name='Salads', name='Greek Salad', num_toppings=0, size=False, price=8.25)
Menu(class_name='Salads', name='Antipasto', num_toppings=0, size=False, price=8.25)
Menu(class_name='Salads', name='Salad w/Tuna', num_toppings=0, size=False, price=8.25)

Menu(class_name='Dinner Platters', name='Garden Salad', num_toppings=0, size=True, price=35.00, price_big=60.00)
Menu(class_name='Dinner Platters', name='Greek Salad', num_toppings=0, size=True, price=45.00, price_big=70.00)
Menu(class_name='Dinner Platters', name='Antipasto', num_toppings=0, size=True, price=45.00, price_big=70.00)
Menu(class_name='Dinner Platters', name='Baked Ziti', num_toppings=0, size=True, price=35.00, price_big=60.00)
Menu(class_name='Dinner Platters', name='Meatball Parm', num_toppings=0, size=True, price=45.00, price_big=70.00)
Menu(class_name='Dinner Platters', name='Chicken Parm', num_toppings=0, size=True, price=45.00, price_big=80.00)
"""