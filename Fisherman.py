
import random

pound = float(input("How many pounds of fish did you catch? "))

kilogram = pound * 0.45359237

money = kilogram * 2

print("Weight in kilograms:", kilogram)
print("Your payment is:", money, "dollars")

if money > 100:
    prizes = ["Hat", "Hook", "Bucket"]
    prize = random.choice(prizes)
    print("Congratulations! You won a:", prize)
else:
    print("Sorry, no prize this time!")
