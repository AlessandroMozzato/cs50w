if (window.localStorage.hasOwnProperty("cart") == false) {
    var cart = new Object();
} else {
    cart = JSON.parse(window.localStorage.getItem("cart"));
}

elements = Object.keys(cart).length;
total=0.

toppings = new Object();

toppings['pizza'] = ['Toppings', 'Pepperoni', 'Sausage', 'Mushrooms', 'Onions', 'Ham', 
                    'Canadian Bacon', 'Pineapple', 'Eggplant', 'Tomato & Basil', 
                    'Green Peppers','Hamburger', 'Spinach', 'Artichoke', 'Buffalo Chicken', 
                    'Barbecue Chicken','Anchovies', 'Black Olives', 'Fresh Garlic', 'Zucchini'];
toppings['sub'] = ['Extra Cheese'];
toppings['subs'] = ['Mushrooms', 'Green Peppers', 'Onions', 'Extra Cheese'];

function addToCart(class_name, mtype, name, price, num_toppings, size) {
    elements += 1;
	cart[elements] = new Object();

    const li = document.createElement('li');
    cart[elements]['class_name'] = class_name;
    cart[elements]['mtype'] = mtype;
    cart[elements]['name'] = name;
    cart[elements]['size'] = size;
    cart[elements]['price'] = parseFloat(price);
    cart[elements]['n_toppings'] = parseInt(num_toppings);
    cart[elements]['toppings'] = [];
    cart[elements]['curr_top'] = 0;

    li.innerHTML =  class_name+' '+name+' ('+size+') '+price;
    document.querySelector('#cartitems').append(li);

    calcTotal();
    
    if (parseInt(num_toppings) > 0) {
		addToppings(class_name, mtype, elements);
	}
    window.localStorage.setItem("cart", JSON.stringify(cart));
}

function addToppings(class_name, mtype, el) {
    var txt = document.querySelector('#toppingsdiv').innerHTML;
    var toadd = '<div id="close" onclick="closeTopps();">Close X</div><ul id="toppings"></ul>'
    document.querySelector('#toppingsdiv').innerHTML = toadd + txt;
	for (var i = toppings[mtype].length - 1; i >= 0; i--) {
		const li = document.createElement('li');
		const aa = document.createElement('a');
    	aa.innerHTML = toppings[mtype][i];
    	aa.href = "#";

    	aa.onclick = function() {
            var top = this.innerHTML;

            if (cart[el]['mtype'] == 'subs' || cart[el]['mtype'] == 'sub') {
                var twoPlacedFloat = + parseFloat(cart[el]['price']);
                cart[el]['price'] = twoPlacedFloat + 0.50;
            }

            cart[el]['curr_top'] += 1;
            cart[el]['toppings'].push(top)

            var text = cart[el]['class_name']+' '+cart[el]['name']+' ('+cart[el]['size']+') '+ 
                        cart[el]['price'] + ", " + cart[el]['toppings'].join(', ');
            document.querySelector('#cartitems').lastElementChild.innerHTML = text;
            calcTotal();

            if (cart[el]['n_toppings'] == cart[el]['curr_top']) {
                document.querySelector('#toppingsdiv').innerHTML = '';
            }
            window.localStorage.setItem("cart", JSON.stringify(cart));
        }
    	li.appendChild(aa);
    	document.querySelector('#toppings').append(li);
	}
}

function closeTopps() {
    document.querySelector('#toppingsdiv').innerHTML = '';
}

function calcTotal() {
    total = 0.
    for (var el in cart) {
        if (cart.hasOwnProperty(el)) {
            var twoPlacedFloat = + parseFloat(cart[el]['price']);
            total = total + twoPlacedFloat;
        }
    }

    text = "The current total is: "+total.toFixed(2).toString();
    document.querySelector('#total').innerHTML = text;
}

function showCart() {
    total = 0.;
    for (var el in cart) {
        if (cart.hasOwnProperty(el)) {
            const li = document.createElement('li');
            li.innerHTML =  cart[el]['class_name']+' '+cart[el]['name']+' ('+cart[el]['size']+') '+ 
                                cart[el]['price'].toString() + ", " + cart[el]['toppings'].join(', ');
            document.querySelector('#cartitems').append(li);

            var twoPlacedFloat = + parseFloat(cart[el]['price']);
            total = total + twoPlacedFloat;
        }
    }
    text = "The current total is: "+total.toFixed(2).toString();
    document.querySelector('#total').innerHTML = text;
}

function fillCart(  ) {
    total = 0.;
    for (var el in cart) {
        if (cart.hasOwnProperty(el)) {
            const li = document.createElement('li');
            li.innerHTML =  cart[el]['class_name']+' '+cart[el]['name']+' ('+cart[el]['size']+') '+ 
                                cart[el]['price'].toString() + ", " + cart[el]['toppings'].join(', ');
            document.querySelector('#subcartitems').append(li);

            var twoPlacedFloat = + parseFloat(cart[el]['price']);
            total = total + twoPlacedFloat;
        }
    }
    text = "The current total is: "+total.toFixed(2).toString();
    document.querySelector('#subtotal').innerHTML = text;
}

// #italy #riesling #vino #wine #🍷 #glouglou #winestagram #winetasting #winelife #winelover #winetime #winery #winelovers #winecountry #instawine #wineoclock #winesaturday #wineday