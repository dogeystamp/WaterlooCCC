#Written by DogeyStamp as practice.
#15/15 points
#Really simple, we take in the numbers into a list, we then use an if/else to ignore or answer.
nums = [int(input()) for i in range(4)] 
if((nums[0] == 8 or nums[0] == 9) and (nums[3] == 8 or nums[3]==9) and (nums[1] == nums[2])):
    print("ignore")
else:
    print("answer")