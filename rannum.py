import random
numlist = random.sample(range(100), 100)
for num in numlist:
    if num % 5 == 0:
        print(num)
