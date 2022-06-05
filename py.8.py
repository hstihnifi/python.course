# """""""""""""""""""""""""""""""""""""""""""""""""Tuples,Dictionary,and Sets Exc:""""""""""""""""

# 1)
# lists are mutable but tuples are immutable

# 2)
# in tuples items can't be modified (can't be removed or added ,and replaced within tuples)

# 3)
# tuples are immutable

# 4)
# ordered

# 5)
a = (1, 2, 3, 4, 5, 6, 7, 8)
print(a)
s = _, _, *s, _, _ = a
print(s)

# 6)
a = (1, 2, 3, 4, 5, 6, 7, 8)
s = a[3:7]
print(s)

# 7)
tpl = (7, 10, -3, 18, 6, 10)
i = list(tpl)
i[0] = 'x'
i[5] = 'y'
tpl = tuple(i)
print(tpl)

# 8)
def product(*cp):
    Product = 1
    for i in cp:
        Product *= i
    return Product

# 9)
def zero_sum(i, index, result):
    i = (3, 2, -5)
    result = 0
    for index in i:
        result += index
        if result == 0:

            return True
        else:
            return False

# 10)
# because it associates a key with an item

# 11)
# dict = {"d": }
# print(dict)

# 12)
# d['fred'] = 44

# 13) & 14)
# A valid key should be present in dictionary or the interpreter generates a
# KeyError exception

# 15)
# mutable

# 16)
# a)
# {3: 0, 5: 1, 10: 1, 8: 2, 15: 4}
# b)
# 3, 5, 10, 8, 15
# c)
# 3, 5, 10, 8, 15
# d)
# 0, 1, 1, 2, 4

# 17)
# ordered(in later versions)

# 18)
from tkinter import Tk, Button

count = 0


def update():
    global count, b
    count += 1
    b.configure(text="Click count= " + str(count))
    print("updating")


root = Tk()
b = Button(root)
b.configure(background="yellow", text="Click count = 0", command=update)
b.pack()
root.mainloop()


# 20)
# In order to use the curly braces for a set, the set must contain at least one element

# 21)
A = set()
print(type(A))

# 22)
# mutable

# 23)
# a)
# {2, 19, 20, 7, 10}
# b) True
# c) False
# d) {10,7}
# e) {2, 4, 5, 6, 7, 9, 10, 19, 20}
# f) True
# g) True
# h) False
# i) True
# j) False
# k) 5
# l) {2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# m) {0, 5, 8, 17, 18}
# n) {0, 5}

# """"""""""""""""""""""""""""""""""""""""""" Handling Exceptions Exc:"""""""""""""""""""""""""""""""

# 11)
try:
    lst = [0, 0, 0, 0]
    with open('data.txt', 'r') as f:
        count = 0
        for line in f.read_lines():
            lst[count] = int(line)
            count += 1
except FileNotFoundError:
    print("the 'data.txt' file doesn't exist")
except OSError:
    print("can't read the 'data.txt' ")

# 12)
# a) i.Begin,22,End  b)ValueError exception
try:
    print("Begin")
    x = int(input())
except ValueError as x:
    print(x)
else:
    print("End")

# b) i:Begin , 22 , End
# ii:Begin, ZZ , wrong!, End

# c) i:Begin,22  ii:ValueError, written type of error is wrong it should be ValueError
print("Begin")
try:
    x = int(input())
    print(x)
except IndexError:
    print("Wrong!")
except ValueError as x:
    print("Given Value is incorrect")
    print("End")

# d) i:Begin , 22 , End
# ii:Begin , ZZ , Wrong! , End

# e)i:Begin
# 22
# Wow
# End
# ii
# Begin
# ZZ
# Wrong!
# End

# f)i:Begin
# 22
# Done
# End
# ii:
# Begin
# ZZ
# Wrong!
# Done
# End

# g)i:Begin
# 22
# Wow
# Done
# End
# ii:Begin
# ZZ
# Wrong!
# Done
# End

# 13)
# ValueError is subset of Exception,so it won't run except ValueError

# 14)
# FileNotFoundError is subclass of OSError, it get raised depending on the system error code

# """""""""""""""""""""""""""""""""""""""""""""""""""" Custom Types Exc:""""""""""""""""""""""

# 1)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(point: {},{})".format(self.x, self.y)

    def distance(self, other):
        return (self.x - other.x) + (self.y - other.y)


r1 = Point(3, 0)
r2 = Point(5, 0)
print(Point.distance(r1, r2))

# 3)it lets the class initialize the object's attributes and serves no other purpose.

# 5)
class Rational:

    def __init__(self, num, den):
        self.__numerator = num
        if den != 0:
            self.__denominator = den
        else:
            raise ValueError("The Rational Number is Illegal")

    def get_numerator(self):
        return self.__numerator

    def get_denominator(self):
        return self.__denominator

    def set_numerator(self, n):
        self.__numerator = n

    def set_denominator(self, d):

        if d != 0:
            self.__denominator = d
        else:
            raise ValueError("Zero denominator")

    def __mul__(self, other):
        return Rational(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    def __add__(self, other):
        pass

    def __str__(self):
        return str(self.get_numerator()) + "/" + str(self.get_denominator())


def main():
    fract1 = Rational(1, 2)
    fract2 = Rational(2, 3)
    print("fract1 =", fract1)
    print("fract2 =", fract2)
    fract1.set_numerator(3)
    fract1.set_denominator(4)
    fract2.set_numerator(1)
    fract2.set_denominator(10)
    print("fract1 =", fract1)
    print("fract2 =", fract2)
    fract3 = Rational(1, 2)
    fract4 = Rational(3, 5)
    print(fract3, "*", fract4, "=", fract3 * fract4)
    frac5 = Rational(4, 1)


main()

# 7)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(point: {},{})".format(self.x, self.y)

    def distance(self, other):
        return (self.x - other.x) + (self.y - other.y)


r1 = Point(3, 0)
p = Point(2, 4)
print(Point.distance(r1, p))

# 9)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius


c = Circle(2)
print("Area of circle:", round(c.area(), 2))
print("Perimeter of circle:", round(c.circumference(), 2))

# 11)

# a)
# 40
# 0
# 41
# 1
# 50
# 21

# b) 0

# c) 50
