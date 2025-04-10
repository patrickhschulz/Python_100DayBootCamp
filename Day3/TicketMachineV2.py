# TicketMachine :D
print("Welcome to the rollercoaster!")

adult_price = 12
youth_price = 7
child_price = 5
midlife_crisis = 0
# rider_height = 0
age = 0

rider_height = int(input("What is your height in CM? "))
if rider_height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age >= 45 and age <= 55:
        print(f"Enjoy your midlife crisis ${midlife_crisis} ticket")
        bill = midlife_crisis
    elif age > 18:
        print(f"Ticket price is ${adult_price}.")
        bill = adult_price
    elif age < 12:
        print(f"Ticket price is ${child_price}")
        bill = child_price
    else:
        print(f"Ticket price is ${youth_price}")
        bill = youth_price

    wants_photo = input("Do you want to have a photo taken? Type Y for Yes and N for No.").lower()
    if wants_photo == "y":
        #add cost of photo to bill
        bill += 3
    print(f"Your final bill will be {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
