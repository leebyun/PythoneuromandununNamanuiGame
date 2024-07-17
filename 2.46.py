import random

li = [10, 20, 30, 40, 50]
print(li)
print(random.choice(li))
print(random.sample(li, 2))
random.shuffle(li)
print(li)