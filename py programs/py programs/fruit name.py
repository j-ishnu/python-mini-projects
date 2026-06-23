fruit_list=["Apple", "Mango", "Banana", "Orange", "Grapes", "Pineapple", "Papaya", "Strawberry", "Watermelon"]
fruit_name=input('Enter the fruit name you want to buy:')
fruit_name=fruit_name.lower()
for fruit in fruit_list:
	if fruit.lower()==fruit_name:
		print(f'"Yes, {fruit} is availiable."')
		break
else:
	print(f'"Sorry, that fruit is not availiable."')
			
