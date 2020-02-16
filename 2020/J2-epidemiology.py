#Written by DogeyStamp during the 2020 CCC.
#15/15 points
#This one is a bit confusing.
#p is the limit of people infected until we raise the alarm.
#n is the initial number of infected.
#r is the rate of transmission.
#An important thing is that one person can only infect r people ONCE.
#First we have a number of infected people, inf.
#newInf is the number of people that have been infected on that day, and can infect others.
#day is the current day.
#A while loop updates newInf by multiplying it by r
#It also adds newInf to the total infected number, inf.
#When inf (the total) goes over p (the limit), print the day number.
p = int(input())
n = int(input())
r = int(input())
inf = n
newInf = n
day = 0
while inf <= p:
    newInf = r*newInf
    inf += newInf
    day += 1
print(day)