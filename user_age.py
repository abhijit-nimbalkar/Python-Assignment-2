
# File: user_age.py
# user input example

age_good = False
age = 0.0
while not age_good:
    try:
        age = float(input("Enter your age: "))
    except:
        print("Bad age format")
        age = -1.0
    if not 0.0 < age <= 125.0:
        print("Enter value in (0.0,125.0]")
    else:
        age_good = True
print("Age is", age)
