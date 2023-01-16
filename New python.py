weight = input("Weight: ")
unit = input("Convert to (K)ilograms or (L)bs: ")
if not weight.isnumeric():
    print("Error please type in a number.")

Kilograms = float(float(weight) // 2.204)
Pounds = float(float(weight) * 2.204) 

if not unit.isnumeric():
    print("Error please put in a number")
if unit == "K" or unit == "k":
        print("Your weight in kilos is: " + str(Kilograms))

if unit == "L" or unit == "l":
        print("Your weight in (L)bs is: " + str(Pounds))

if unit != "k" or unit != "K" or unit !="l" or unit != "L":
    print("put in L for lbs and K for kilos")