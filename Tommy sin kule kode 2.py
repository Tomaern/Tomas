Weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K" :
    Converted = Weight / 0.45
    print("Weight in Lbs: " + str(Converted))
else:
    Converted = Weight * 0.45
    print("Weight in Kg: " + str(Converted))