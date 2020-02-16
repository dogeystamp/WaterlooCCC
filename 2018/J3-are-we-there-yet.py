#Written by DogeyStamp as practice.
#15/15 points
#We get the cities distances from 0, and not from eachother.
#We then do a nested for loop to compare each city to eachother.
nums = input()
cities = [0]
ind = 0
for i in nums.split():
    cities.append(int(i)+int(cities[ind]))
    ind+=1
for i in range(len(cities)):
    for j in range(len(cities)):
        print(abs(cities[j]-cities[i]),end = " ")
    print("")