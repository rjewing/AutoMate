from FuelCalculator import FuelCost


def main():
	myfuelcost = FuelCost()
	state = raw_input("Enter state: ")
	distance = int(raw_input("Enter distance traveled per year: "))
	mpg = int(raw_input("Enter miles per gallon: "))
	print myfuelcost.calculateFuelCost(state, distance, mpg)

if __name__ == '__main__':
	main()
