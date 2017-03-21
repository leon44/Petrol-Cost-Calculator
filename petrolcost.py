# -*- coding: utf-8 -*-
print("Welcome to Leon's journey cost calculator!")
def costcalculatorUK():
	print("UK mode")
	miles = int(input("Total miles:"))
	mpg = int(raw_input("MPG of the car:") or "45")
	price = float(raw_input("Petrol price per liter: £") or "1.20")
	passengers = int(raw_input("How many passengers are travelling?:") or "1")
	pricePence = int(price*100)
	mpl = mpg / 4.54609
	litresUsed = miles / mpl
	petrolCost = litresUsed * pricePence
	petrolCostpound = float("{0:.2f}".format(petrolCost / 100))
	perpassengerCost = float("{0:2f}".format(petrolCostpound / passengers))
	print "The journey will cost a total of £",petrolCostpound
	print "This is £",perpassengerCost," each"
	print("Thanks and goodnight!")

def costcalculatorNL():
	print("Euro mode")
	km = float(raw_input("Total kilometers:"))
	kpl = float(raw_input("Kilometres per litre:") or "20")
	price = float(raw_input("Petrol price per liter: €") or "1.50")
	passengers = int(raw_input("How many passengers are travelling?:") or "1")
	priceCents = int(price*100)
	litresUsed = km / kpl
	petrolCost = litresUsed * priceCents
	petrolCostEuro = float("{0:.2f}".format(petrolCost / 100))
	perpassengerCost = float("{0:2f}".format(petrolCostEuro / passengers))
	print "The journey will cost a total of €",petrolCostEuro
	print "This is €",perpassengerCost," each"
	print("Thanks and goodnight!")

mode = raw_input("Hit return for UK mode or enter e for Euro mode: ")

if mode == "e":
	costcalculatorNL()
else:
	costcalculatorUK()