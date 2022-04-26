name = input("What's your name?")
age = int(input("Enter your age:"))
name = name.lower()
firstLetter = name[0].upper()

if age > 0  and  age < 12:
    print("You're in a child")
    if name == 'josh':
        print("This is Josh!")
    else:
        print("This is "+ name)
elif age == 13:
    print("Welcome to your teenage years")
    if name == 'josh':
        print("This is Josh!")
    else:
        print("This is "+ name)
elif age > 13 and age <=18:
    print("You're a teenager!")
    if name == 'josh':
        print("This is Josh!")
    else:
        print("This is "+ name)
elif age > 18 and age < 60:
    print("You're an adult")
    if name == 'josh':
        print("This is Josh!")
    else:
        print("This is "+ name)
else:
    print("You're ancient")
    if name == 'josh':
        print("This is Josh!")
    else:
        print("This is "+ name)

print(f"{name.capitalize()} is {str(age)} years old")
print(f"The first letter of your name is {firstLetter}")