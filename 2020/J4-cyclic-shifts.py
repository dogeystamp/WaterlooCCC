str1 = input()
str2 = input()
def shift(toShift):
    return toShift[len(toShift)-1] + toShift[:len(toShift)-1]
for i in range(len(str2)):
    if str2 in str1:
        print("yes")
        exit()
    str2 = shift(str2)
print("no")