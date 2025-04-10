#random module :D
import random
#import my_module

#print(random.randint(1, 100))
#print(my_module.my_favorite_number)

# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)

random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

random_float = random.uniform(1, 100)
print(random_float)

random_cointoss = random.randint(1, 100)
if random_cointoss > 50:
    print("Heads")
else:
    print("Tails")