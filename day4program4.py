import math
def checkArmstrongNumber(num):
    num=str(num)
    n=len(num)
    total=0
    for i in num:
        total +=int(i)**n
    if int(num)==total:
        return 1
    else:
        return 0
inpNum=input("Enter a Number:")
if checkArmstrongNumber(inpNum):
       print("yes")
else:
       print("No")
        
