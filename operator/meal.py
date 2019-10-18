import math
# import sys

# input = sys.stdin.readline()
def solve(meal_cost, tip_percent, tax_percent):
	if meal_cost < 0 or tip_percent < 0 or tax_percent < 0:
		print('Invalid entry: try again')
		return False

	totalMealCost = int(round(meal_cost + ((tip_percent/100)*meal_cost) + ((tax_percent/100)*meal_cost)))
	print('totalMealCost is: ',totalMealCost)
	
bill = True
while bill:
	mealcost = float(input('Enter:'))
	tippercent = int(input('Enter:'))
	taxpercent = int(input('Enter:'))
	totalcost = solve(mealcost, tippercent, taxpercent)
	complete= False
	if not complete:
		again = input('do u have another bill: (y/n)')
		if again.lower() == 'y':
			print('Provide')
		elif again.lower() == 'n':
			bill = False
		else:
			print('Not a valid input')
			bill = False
