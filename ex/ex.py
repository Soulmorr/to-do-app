import random

lower = int(input("input a lower bound:"))
upper = int(input("input a upper bound:"))

result = random.randrange(lower, upper+1)
print(result)
