print("Hello World")

#BMI Calculator Activity (w/the help of Cs Dojo)

name1= "Toni"
height_m1 = 2
weight_kg1 = 90

name2 = "Toni's Sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "Toni's Cousin"
height_m3 = 2.5
weight_kg3 = 160

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"

result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)

#Madlib project

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Name: ")


madlib = f"Computer programming is so {adj}! It makes me so excited all the time because I love to {verb1}!\
Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)

#Secret Number Game

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low")
        elif guess > random_number:
            print("Sorry, guess again. Too high")

    print(f"Yay, congrats. You have guessed the number {random_number} correctly")


guess(10)
