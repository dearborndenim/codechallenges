from random import randint
from pprint import pprint

counter={}
for x in range(1000):
    number = randint(1,20)
    if number not in counter:
        counter[number] = 1
        continue

    if number in counter:
        counter[number] += 1

pprint(counter)
