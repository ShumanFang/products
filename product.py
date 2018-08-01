import os #import operating system

products = []
if os.path.isfile('products.csv') #check if there is already a file
	print('yeah, found file')
	#read file
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if 'product, price' in line:
				continue #this will skip the following content in the loop and move on to the next loop
			name, price = line.strip().split(',')
			prodcuts.append9([name,price])
	print(products)

else:
	print('cant find file')


#read file
# products = []
# with open('products.csv', 'r', encoding='utf-8') as f:
# 	for line in f:
# 		if 'product, price' in line:
# 			continue #this will skip the following content in the loop and move on to the next loop
# 		name, price = line.strip().split(',')
# 		prodcuts.append9([name,price])
# print(products)



#enter info
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


#create file
with open('prodcuts.csv','w', encoding = 'utf-8') as f: 
	#the encoding part is for the program to recognize as many languages as possible
	#therefore it can read chinese if you have chinese as the title, if you only have english then dont really need it
	f.write('product name, price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')