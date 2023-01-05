weight = input("Wieght: ")
unit = input("(K)ilograms or (L)bs: ")
Kilograms = float(float(weight) * 2.204)
Pounds = float(float(weight) // 2.204) 
if unit == "K" or unit == "k":
    print("Your weight in kilos is: " + str(Kilograms))

if unit == "L" or unit == "l":
    print("Your weight in pounds is: " + str(Pounds))
