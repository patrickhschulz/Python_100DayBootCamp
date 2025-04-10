print("Welcome to the Python Pizza Delivery App!")
crust_size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

#todo: work out how much they need to pay based on their size and toppings

small_crust = 15
medium_crust = 20
large_crust = 25
small_pepperoni = 2
medium_pepperoni = 3
large_pepperoni = 3

if extra_cheese == "y":
    cheezy = 1
else:
    cheezy = 0

if pepperoni == "y" and crust_size == "m" or crust_size == "l":
    pepperoni_cost = medium_pepperoni
elif pepperoni == "y" and crust_size == "s":
    pepperoni_cost = small_pepperoni
else:
    pepperoni_cost = 0

if crust_size == "l":
    pizza_cost = large_crust + pepperoni_cost + cheezy
elif crust_size == "m":
    pizza_cost = medium_crust + pepperoni_cost + cheezy
elif crust_size == "s":
    pizza_cost = small_crust + pepperoni_cost + cheezy

print("Your pizza will be $" + str(pizza_cost))



