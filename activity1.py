name = input("Enter your name: ")
program = input("Enter your program: ")
section_block = input("Enter your section/block: ")
email = input("Enter your email address: ")
age = int(input("Enter your age: "))
height_cm = float(input("Enter your height in cm: "))
weight_kg = float(input("Enter your weight in kg: "))

hobbies = []
for i in range(3):
    hobby = input(f"Enter hobby {i + 1}: ")
    hobbies.append(hobby)

is_allowed_to_drink = age >= 18

height_inches = height_cm * 0.393701

weight_lbs = weight_kg * 2.20462

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)

print("\nUser Information:")
print(f"a. Name: {name}")
print(f"b. Program: {program}")
print(f"c. Block: {section_block}")
print(f"d. Email: {email}")
print(f"e. Age: {age}")
print(f"f. Is allowed to drink: {is_allowed_to_drink}")
print(f"g. Height (Inches): {height_inches:.2f}")
print(f"h. Weight (lbs): {weight_lbs:.2f}")
print(f"i. BMI: {bmi:.2f}")

print("\nHobbies:")
for i, hobby in enumerate(hobbies, start=1):
    print(f"{i}. Hobby {i}: {hobby}")
