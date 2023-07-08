import random

print("welcome to bill decider-who will pay the bill")
x= input("Please give names: ")
names=x.split(",")
print(names)
print(random.choice(names))

