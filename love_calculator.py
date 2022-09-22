print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lover1 = name1.lower()
lover2 = name2.lower()

a = lover1 + lover2

t = a.count("t")
r = a.count("r")
u = a.count("u")
e = a.count("e")

l = a.count("l")
o = a.count("o")
v = a.count("v")
e = a.count("e")

digit1 = t + r + u + e
digit2 = l + o + v + e

true_love = str(digit1) + str(digit2)
score = int(true_love)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")