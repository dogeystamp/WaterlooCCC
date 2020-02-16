#Written by DogeyStamp during the 2020 CCC.
#15/15 points
#Simple code, we read the 3 lines of input, the number of Small, Medium and Large treats.
#We then get the score using the formula in the problem: 1*S+2*M+3*L.
#An if statement sees if it is larger or equal to 10 and prints yes or no accordingly.
s = int(input())
m = int(input())
l = int(input())
if (s + m*2 + l*3) >= 10:
    print("happy")
else:
    print("sad")