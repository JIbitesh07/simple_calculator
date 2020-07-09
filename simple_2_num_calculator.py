#functions used for calculations
def addition(c,d):
    return c+d
def substraction(c,d):
    return c-d
def multiplication(c,d):
    return c*d
def division(c,d):
    return c//d
def mod(c,d):
    return c%d
def exponent(c,d):
    return c**d
#taking two user inputs for calculation
c=float(input("enter a number"))
d=float(input("enter a number"))
#giving options to user to choose one of the operation
print("1.addition,2.substraction,3.multiplation,4.division,5.mod,6.exponent")
x=str(input("choose a operation number from above"))

#calculating the result according to the inputs and operations entered by the users
if(x=="1"):
    print(addition(c,d))
elif(x=="2"):
    print(substraction(c,d))
elif(x=="3"):
    print(multiplication(c,d))
elif(x=="4"):
    print(division(c,d))
elif(x=="5"):
    print(mod(c,d))
elif(x=="6"):
    print(exponent(c,d))
else:
    print("operation not found")
   
