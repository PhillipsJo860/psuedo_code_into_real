# Joshua and Tucker
# Psuedo code group project
# 9/24/2024

# Project A
# Input
name = input("Please enter your name here: ")
print(f"Welcome {name}, please enter your three quiz scores below.")
quiz1 = int(input("Enter score one: "))
quiz2 = int(input("Enter score two: "))
quiz3 = int(input("Enter score three: "))
# Process
added = quiz1 + quiz2 + quiz3
average = added / 3
# Ouput
print(f"You entered the three scores as follows: {quiz1} {quiz2} {quiz3}. The average between the three scores is = {int(average)}")
# Project B
# Input
name = input("Please enter your name here: ")
print(f"Welcome {name}, today we will be calculating your vehicles gas milage.")
miles_drove = int(input("Please enter the distance drove in miles: "))
gas_used = int(input("Please enter the amount of gas used in gallons: "))
# Process
mi_per_gal = miles_drove / gas_used
# Output
print(f"You drove {miles_drove} and used {gas_used} gallons of gas. THis means that your gas milage is {float(mi_per_gal)}.")