# Exercise 3.21
""" (Calculate Change using fewest number of coins.) Write a script that inputs a purchase price of a dollar or less and find the change for a dollar"""

#read user input
total = int (input('Please enter the price of your item in cents: '))

#find change
change = 100- total 

#print starting change statement
print ('Your change is: ')
while change != 0:

	#if change is greater than 25, calculate the number of quarters that can be given
	if change >= 25:
		quar = change // 25
		change -= quar * 25
		print (quar, 'Quarters')

	#If change is greater than 10 and less than 25, calculate number of dimes that can be given
	if change >= 10:
		dime = change // 10
		change -= dime * 10
		print (dime, 'Dimes')

	#If change is greater than 5 and less than 10, calculate the number of nickels that can be given
	if change >= 5:
		nick = change // 5
		change -= nick * 5
		print(nick, 'Nickels')

	#If change is greater than one and less than five, remaining change is given in pennies
	if change >= 1:
		penn = change 
		change -= penn
		print (penn, 'Pennies')