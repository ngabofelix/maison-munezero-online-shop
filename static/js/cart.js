// get add to cart button
var addToCartBtn = document.getElementsByClassName('add-to-cart')

// loop in that btns and each btn add event listener 'click' 
// and then grab the value data-attribute we set for each button
//then execute callback function which will send data to backend in Ajax call
for(i = 0 ; i < addToCartBtn.length ; i++){
	addToCartBtn[i].addEventListener('click', function(){
		var product_id = this.dataset.product
		var action = this.dataset.action

		if(user == 'AnonymousUser'){
			console.log('not logged in: ',user)
			window.location.href = "user/login"
		}else{
			addToCartHandler(product_id, action)
		}
	})
}

// declaration of callback func which send data
function addToCartHandler(product_id, action){
	// set url path
	var url = 'add-to-cart';

	// construct fetch call
	fetch(url, {
		method: 'POST',
		headers: {
			'ContentType' : 'application/json',
			'X-CSRFToken': csrftoken,
		},
		body : JSON.stringify({'product_id':product_id, 'action':action})
	})
	// return promise
	.then((response)=>{
		return response.json()
	})
	.then((data) => {
		console.log('data:', data)
		location.reload()
	})
}

