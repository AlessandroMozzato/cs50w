var cart = new Object();
elements = 0;
total = 0;

toppings = ['Toppings', 'Pepperoni', 'Sausage', 'Mushrooms', 'Onions', 'Ham', 'Canadian Bacon', 'Pineapple', 
'Eggplant', 'Tomato & Basil', 'Green Peppers','Hamburger', 'Spinach', 'Artichoke', 'Buffalo Chicken', 
'Barbecue Chicken','Anchovies', 'Black Olives', 'Fresh Garlic', 'Zucchini'];

function addToCart(class_name, name, price, num_toppings, size) {
    elements += 1;
	cart[elements] = new Object();

    const li = document.createElement('li');
    cart[elements]['class_name'] = class_name;
    cart[elements]['name'] = name;
    cart[elements]['size'] = size;
    cart[elements]['price'] = price;
    cart[elements]['n_toppings'] = parseInt(num_toppings);
    cart[elements]['toppings'] = [];
    cart[elements]['curr_top'] = 0;

    li.innerHTML =  class_name+' '+name+' ('+size+') '+price;
    document.querySelector('#cartitems').append(li);
    var twoPlacedFloat = + parseFloat(price);
    total = total + twoPlacedFloat;
    text = "The current total is: "+total.toFixed(2).toString();
	
    document.querySelector('#total').innerHTML = text;
    
    if (parseInt(num_toppings) > 0) {
		addToppings(class_name, elements);
	}
}

function addToppings(class_name, el) {
	for (var i = toppings.length - 1; i >= 0; i--) {
		const li = document.createElement('li');
		const aa = document.createElement('a');
    	aa.innerHTML = toppings[i];
    	aa.href = "#";

    	aa.onclick = function() {
            var top = this.innerHTML;
            var text = document.querySelector('#cartitems').lastElementChild.innerHTML;
            document.querySelector('#cartitems').lastElementChild.innerHTML = text + ", " + top;
            cart[el]['curr_top'] += 1;
            cart[el]['toppings'].push(top)

            if (cart[el]['n_toppings'] == cart[elements]['curr_top']) {
                var ul = document.getElementById("toppings");
                while(ul.firstChild){
                    ul.removeChild(ul.firstChild);
                }
            }
        }

    	li.appendChild(aa);
    	document.querySelector('#toppings').append(li);
	}
}