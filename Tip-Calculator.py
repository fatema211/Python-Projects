#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = input("What was the total bill? $\n")
bill_float = float(bill)
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
tip_calculation = bill_float*(tip/100)
total_bill = bill_float+tip_calculation
people = input("How many people to split the bill?\n")
each_person_has_to_pay = total_bill/5
final_bil = "{:.2f}".format(each_person_has_to_pay)
print(f"Each person should pay {final_bil}")
