print("Welcome to the tip calculator")
total = float(input("What was the total bill? $"))
tip_percentage = input("how much tip would you like to leave? 10, 12, or 15?\n")
percentage = int(tip_percentage) / 100
party_size = input("How big was the lunch party?\n")
share = (int(total) * int(percentage) + int(total)) / int(party_size)
print(share)