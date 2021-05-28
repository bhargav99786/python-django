
#1.	Calculate average of 5 numbers.
V1 = int(input("ENTER FIRST VALUE :"))
V2 = int(input("ENTER SECOND VALUE :"))
V3 = int(input("ENTER THIRD VALUE :"))
V4 = int(input("ENTER FOURTH VALUE :"))
V5 = int(input("ENTER FIFTH VALUE :"))
total = V1 + V2 + V3 + V4 + V5
average = total / 5
print(average)

#2.	Check whether number is even or odd.
val1 = int(input("enter any numbe :"))
if val1%2 == 0:
    print("{0} number is even".format(val1))
else:
    print("{0} number is odd".format(val1))

#3.	Take a year and check whether it is leap year or not
val1 = int(input("enter any year :"))
if (((val1 % 4 == 0) & (val1 % 100!= 0)) | (val1%400 == 0)):
    print("{0}  is leap year".format(val1))
else:
    print("{0} is not leap year".format(val1))

#4.	Take a number and check whether it is zero, positive or negative.
#11.	Take a number and check whether it is zero, positive or negative using nested IF…ELSE statement .
val1 = int(input("enter number"))
if val1 < 0 :
    print("{} is negative".format(val1))
elif val1 >0:
    print("{} is positive".format(val1))
else:
    print("{} is zero".format(val1))


#5.	Take 2 numbers and display greatest number. (Also check equal number condition)
val1= int(input("enter first number :"))
val2= int(input("enter second number :"))
if val1 > val2:
    print("{} is bigger".format(val1))
elif  val1 < val2:
    print("{} is bigger".format(val2))
else:
    print("both are equal")

#6.	Take a number and find factorial of that number.
num = int(input("enter number :"))
factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

#7.	Write a program to swap 2 numbers using third variable
val1 = int(input("enter first Number :"))
val2 = int(input("enter second Number :"))
temp = val1
val1 = val2
val2 = temp
print("{} is first number".format(val1))
print("{} is second number".format(val2))

#8.	Take 2 numbers and find smallest number.
val1= int(input("enter first number :"))
val2= int(input("enter second number :"))
if val1 > val2:
    print("{} is smallest".format(val2))
elif val1 > val2:
    print("{} is smallest".format(val1))
else:
    print("both are equal")


#9.	Take a number check if a number is less than 100 or not. If it is less than 100 then check if it is odd or even.
val1 = int(input("enter any number :"))
if val1<100:
    if val1%2 == 0:
        print("{0} number is even".format(val1))
    else:
        print("{0} number is odd".format(val1))
else:
    print("{0} is greater than 100".format(val1))

#10.	Take a number to print the square of a number if it is less than 10.
val1 = int(input("enter any number :"))
if val1<10:
    print(val1**2)  11
else:
    print("{0} is greater than 10".format(val1))

#11.	Take a number and check whether it is zero, positive or negative using nested IF…ELSE statement .
val1 = int(input("enter number"))
if val1 < 0 :
    print("{} is negative".format(val1))
elif val1 >0:
    print("{} is positive".format(val1))
else:
    print("{} is zero".format(val1))

#12.	Take 3 numbers and find greatest number using nested IF….ELSE statement.
V1 = int(input("ENTER FIRST VALUE :"))
V2 = int(input("ENTER SECOND VALUE :"))
V3 = int(input("ENTER THIRD VALUE :"))
if V1>V2:
    if V1>V3:
        print("{} is greatest".format(V1))
    else:
        print("{} is greatest".format(V3))
else:
    print("{} is greatest".format(V2))

#13.	Take 3 numbers and find smallest number using logical operator.
V1 = int(input("ENTER FIRST VALUE :"))
V2 = int(input("ENTER SECOND VALUE :"))
V3 = int(input("ENTER THIRD VALUE :"))
if V1<V2:
    if V1<V3:
        print("{} is smallest".format(V1))
    else:
        print("{} is smallest".format(V3))
else:
    print("{} is smallest".format(V2))

#14.	Write a program to swap 2 numbers without taking third variable.
val1 = int(input("enter first Number :"))
val2 = int(input("enter second Number :"))
val1 = val2 + val1
val2 = val1 - val2
val1 = val1 - val2
print("{} is first number".format(val1))
print("{} is second number".format(val2))

#15.	Take starting number and ending number from the user and print following series.
V1 = int(input("ENTER START VALUE :"))
V2 = int(input("ENTER END VALUE :"))
if V1<V2 :
    for i in range(V1,V2 + 1): 
        print(i)
else:
    print("startimng number bigger tahn ending")
