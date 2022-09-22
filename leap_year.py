# pizza order and delivery

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

price = 0

small_pizza = 15
medium_pizza = 20
large_pizza = 25

pepperoni_small = 2
pepperoni_medium_large = 3

cheese = 1


if size == "L":
    price += large_pizza
elif size == "M":
    price += medium_pizza
elif size == "S":
    price += small_pizza

if add_pepperoni == "Y" and size == "S":
    price += pepperoni_small
elif add_pepperoni == "Y" and size == "L":
    price += pepperoni_medium_large
elif add_pepperoni == "Y" and size == "M":
    price += pepperoni_medium_large

if extra_cheese == "Y":
    price += cheese

print(f"Your final bill is: {price}")