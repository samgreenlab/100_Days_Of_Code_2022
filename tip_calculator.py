#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

split_percentage = input("What percentage are you paying, 10, 12, 15?: ")
total_bill = 150
number_of_people = input("How many people are there?: ")
num_people = int(number_of_people)
person_should_pay = (total_bill / num_people) * 1.12
rounded_number = format(person_should_pay, ".2f")

print(f"Each person should pay {rounded_number} tip from {num_people} people")