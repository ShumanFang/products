products = []
while True:
	name = input('please enter the product name: ')
	if name == 'q': #quick
		break
	price = input('please enter product price: ')
	p = []
	p.append(name)
	p.append(price)
	#or p = [name, price]
	products.append(p)
	#or products.append([name, price])
print(products)

products[0][0]