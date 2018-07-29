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

for p in products:
	print(p[0], 's price is', p[1])

# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

with open('prodcuts.csv','w', encoding = 'utf-8') as f: 
	#the encoding part is for the program to recognize as many languages as possible
	#therefore it can read chinese if you have chinese as the title, if you only have english then dont really need it
	f.write('product name, price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')