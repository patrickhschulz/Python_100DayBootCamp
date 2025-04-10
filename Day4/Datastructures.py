# states = ["Deleware", "Pennsilvania", "New Jersey", "Georgia"]
#
# print(states)
# print(states[0])
# print(states[1])
# print(states[-1])
# states[1] = "Pencilvania"
# print(states)
# states.append("Patriconia")
# print(states)
# #.extend adds a list to a list
# states.extend[]
import random

friends = ["John", "Arnie", "Jeff", "Cesar", "Justin"]
print(friends[random.randint(0, 4)])

#Also
print(random.choice(friends))

##################################
print(len(friends))
num_of_states = len(friends)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = (fruits, vegetables)
print(fruits[-1])
print(dirty_dozen[1][1])