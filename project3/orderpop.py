from orders.models import Menu

f = Order(user='ale', items_in_menu=2, total=10.20, items='asd')
f.save()