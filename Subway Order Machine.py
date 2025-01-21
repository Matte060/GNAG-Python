'''
GNAG Week 3:
Subway Order Machine Activity Example
'''

#Welcoming someone to Subway
print("Welcome to Subway, the world famous sandwich shop! Can I take your order?: ")

#Taking their order
size = input("What size sandwich would you like?: ")
meat = input("What kind of meat would you like on your sandwich?: ")
toppings = input("What toppings do you want on your sandwich?: ")
drink = input("What kind of drink would you like?: ")

#Recapping their order
print("Thanks for ordering you got: A", size, meat, "sandwich topped with:", toppings)
print("You got a", drink, "to drink")
