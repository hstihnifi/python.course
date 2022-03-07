import math

print("Q:1 first page")
i = int(input())
j = int(input())
k = int(input())
if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print("i=", i, " j=", j, " k=", k)
# answers
# a) i= 5  j= 5  k= 7
# b) i= 3  j= 5  k= 5
# c) i= 7  j= 3  k= 7
# d) i= 5  j= 3  k= 3
# e) i= 5  j= 3  k= 5
# f) i= 7  j= 7  k= 3


print("Q:2")
print("write a number and i\'ll guess : ")
val = int(input())
if val < 10:
    if val != 5:
        print("bet ", end='you\'re number is under 10 : ')
    else:
         val += 1
else:
    if val == 17:
        val += 10
    else:
        print("let me guess, ", end='you chose a number bigger than 10 : ')
print(val)
# answers
# a) bet you're number is under 10 : 3
# b) let me guess, you chose a number bigger than 10 : 21
# c) 6
# d) 27
# e) bet you're number is under 10 : -5


print("Q:1 next page")
income = int(input("how much is your salary? "))
tax_rate = 0

if income <= 1000:
    tax_rate = 0

elif (income > 1000) and (income <= 2500):
    tax_rate = 10

elif (income > 2500) and (income <= 4000):
    tax_rate = 15

elif (income > 4000) and (income <= 6000):
    tax_rate = 20

elif income > 8000:
    tax_rate = 30

print("tax: ", tax_rate)
print("income: ", income)
print("finally you get: ", income - (tax_rate / 100) * income)


("Q:2")
a = int(input())
b = int(input())
c = int(input())

if (a > b) and (a > c):
    if math.pow(a, 2) == math.pow(b, 2) + math.pow(c, 2):
        print("Right")
    else:
        print("Not right")
if (b > a) and (b > c):
    if math.pow(b, 2) == math.pow(a, 2) + math.pow(c, 2):
        print("Right")
    else:
        print("Not right")
if (c > a) and (c > b):
    if math.pow(c, 2) == math.pow(a, 2) + math.pow(b, 2):
        print("Right")
    else:
        print("Not right")



("Q:3")
duplicate = 0
first_number = int(input('first number: '))
second_number = int(input('second number: '))
if first_number == second_number:
    duplicate = duplicate + 1

third_number = int(input('third number: '))
if first_number == third_number or \
        second_number == third_number:
    duplicate = duplicate + 1

fourth_number = int(input('fourth number: '))
if first_number == fourth_number or \
        second_number == fourth_number or \
        third_number == fourth_number:
    duplicate = duplicate + 1

fifth_number = int(input('fifth number: '))
if first_number == fifth_number or \
        second_number == fifth_number or \
        third_number == fifth_number or \
        fourth_number == fifth_number:
    duplicate = duplicate + 1

if duplicate != 0:
    print("Duplicates")
else:
    print("All Unique")
