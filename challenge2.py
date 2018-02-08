from random import randint

listlength = range(1000)

counter = {}
for x in range(1,21):
	counter[x]=0

randomlist = []

for x in listlength:
	randomlist.append(randint(1,20))

for k in randomlist:
		counter[randomlist[k]]+=1

for i in counter:
	print (counter[i])

input()
