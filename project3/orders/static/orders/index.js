// cart = {};

cart = {};
total = 0;

toppings = ['Toppings', 'Pepperoni', 'Sausage', 'Mushrooms', 
'Onions', 'Ham', 'Canadian Bacon', 'Pineapple', 'Eggplant', 
'Tomato & Basil', 'Green Peppers','Hamburger', 'Spinach', 
'Artichoke', 'Buffalo Chicken', 'Barbecue Chicken','Anchovies', 
'Black Olives', 'Fresh Garlic', 'Zucchini'];

function addToCart(class_name, name, price, num_toppings, size) {
	// cart.append(item.name)

    const li = document.createElement('li');
    li.innerHTML =  class_name+' '+name+' ('+size+') '+price;
    document.querySelector('#cartitems').append(li);
    var twoPlacedFloat = + parseFloat(price)
    total = total + twoPlacedFloat;
    text = "The current total is: "+total.toFixed(2).toString()
    document.querySelector('#total').innerHTML = text;

    var tops = parseInt(num_toppings);

	while (tops > 0) {
		addToppings(class_name);
		tops -= 1;
	}
}

function addToppings(class_name) {
	for (var i = toppings.length - 1; i >= 0; i--) {
		const li = document.createElement('li');
		const aa = document.createElement('a');

    	aa.innerHTML = toppings[i];
    	aa.href = "#";
    	// aa.onclick = addTop(toppings[i]);
    	li.appendChild(aa);
    	document.querySelector('#toppings').append(li);
	}
}

function addTop(val) {
	var lii = document.querySelector('#cartitems').lastElementChild;
	lii.innerHTML = val;

	 var ul = document.getElementById("toppings");

     while (ul.firstChild)
         ul.removeChild(ul.firstChild);
}