// cart = {};

function addToCart(item) {
	// cart.append(item.name)
    const li = document.createElement('li');
    li.innerHTML =  item;
    document.querySelector('#cartitems').append(li);
}