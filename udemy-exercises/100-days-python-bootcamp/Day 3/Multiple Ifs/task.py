print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        if age >= 45 and age <= 55:
            bill = 0
        else:
            bill += 12
            print("adult tickets are $12.")

    photo_cost = input("Do you want to have a photo taken? Type Y for Yes and n for No.")
    if photo_cost == "Y":
        bill += 3
    print(f"your total cost is: ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
