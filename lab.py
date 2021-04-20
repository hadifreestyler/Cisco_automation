

weight = input("Please Enter your weight: ")
unit = input("please Enter the unit Kg(K) or Lbs(L): ")

if unit.lower() == "l":
	converted = weight / 0.45
if unit.lower() == "k":
	print("this is kg")