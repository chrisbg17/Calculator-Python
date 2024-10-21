def calculate():
	operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

	number_1 = int( input('Enter your first number: '))
	number_2 = int( input('Enter your second number: '))

	if operation == '+': 
		print('{} + {} = '.format(number_1, number_2))
		print(number_1+number_2)

	elif operation == '-':
		print('{} - {} = '.format(number_1, number_2))
		print(number_1-number_2)

	elif operation == '/':
		print('{} / {} = '.format(number_1, number_2))
		print(number_1/number_2)

	elif operation == '*':
		print('{} * {} = '.format(number_1, number_2))
		print(number_1*number_2)

	else: 
		print('you have not entered a valid operation, please run the program again')

	# Add again() function to calculate() function
	again()

def again():
	calc_again = input(''' 
Do you want to calculate again?
Please type Y for YES or N No.
''')
	if calc_again == 'Y':
		calculate()
	elif calc_again == 'N':
		print('See you later.')
	else:
		again()

calculate()