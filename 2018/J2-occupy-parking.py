#Written by DogeyStamp as practice.
#15/15 points
#Read number of cars, then the cars on day 1 and 2.
#We then compare using a for loop over each space.
#If there a car both days, then ass 1 to the number of occurences, occs.
space = int(input())
d1 = input()
d2 = input()
occs = 0
for i in range(space):
    if d1[i]==d2[i] and d1[i]=='C':
        occs+=1
print(occs)