# 1) Taylor_Series
#
# import math
# def sin(x, n):
#     sine = 0
#     for i in range(n):
#         sign = math.pow(-1, i)
#         pi = math.pi
#         a = x * (pi / 180)
#         sine = sine + (sign * (a ** (2.0 * i + 1)) / math.factorial(2 * i + 1))
#     return sine
#
#
# x = float(input("enter the degree: "))
# n = int(input("enter the number of terms: "))
# print(sin(x, n))
#
# 2) GCD
# x = int(input("Enter a Number:"))
# y = int(input("Enter another Number"))
# for i in range(1, 100):
#     if i <= y:
#         if x % i == 0 and y % i == 0:
#             gcd = i
#             print(gcd)
#
# 3) Armstrong
# for i in range(1, 10000):
#     n = len(str(i))
#     result = 0
#     Num = i
#
#     while Num > 0:
#         digit = Num % 10
#         result = result + digit ** n
#         Num = Num // 10
#
#     if i == result:
#         print(i)
# answers
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 153
# 370
# 371
# 407
# 1634
# 8208
# 9474
#
# 4)newton raphson
#
# def func(x):
#     return x * x * x - x * x + 2
#
#
# # Derivative of x^3 - x^2 + 2
# def derivFunc(x):
#     return 3 * x * x - 2 * x
#
#
# # Function to find the root
# def newtonRaphson(x):
#     h = func(x) / derivFunc(x)
#     while abs(h) >= 0.0001:
#         h = func(x) / derivFunc(x)
#
#         # x(i+1) = x(i) - f(x) / f'(x)
#         x = x - h
#
#     print("The value of the root is : ", x)
#
#
# x0 = -20  # Initial values assumed
# newtonRaphson(x0)
#
# 5) Ceasar
# from string import ascii_letters
#
#
# def encrypt(string, key):
#     alpha = ascii_letters
#     result = ""
#
#     for chr in string:
#         if chr not in alpha:
#             result += chr
#         else:
#             new_key = (alpha.index(chr) + key) % len(alpha)
#             result += alpha[new_key]
#     return result
#
#
# print(encrypt("salam ruz bekheyr", 3))
# answer
# vdodp uxC ehnkhBu
#
#
# 6)exercise 34
# sum = 0
# min = 1000000
# max = -10000000
# for val in range(0, 20):
#     val = float(input("Enter twenty numbers: "))
#     sum += val
#     if val < min:
#         min = val
#     if val > max:
#         max = val
#
# avg = sum / 20
#
# print("Sum is : ", sum)
# print("Average is : ", avg)
# print("Minimum is :", min)
# print("Maximum is:", max)
