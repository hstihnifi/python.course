# Q:1
# yes,a python list is an object that holds a collaction of objects

# Q:2
# Negative index is allowed

# Q:3
lst = [45, -3, 16, 8]
print(lst)

# answer=[45, -3, 16, 8]

# Q:4
lst = [10, -4, 11, 29]
# a)
print(lst[0])
# b)
print(lst[3])
# c) 10
# d) 29
# e) -4
# f) 29
# g) 10
# h) illegal,should be integers or slices.

# Q:5
lst = [3, 0, 1, 5, 2]
x = 2
# a) 3
# b) 5
# c) 1
# d) 5
# e) 5
# f) 2
# g) 0
# h) 3

# Q:6
i = [30, -6, 45, 69, 56, 34]
print(len(i))
# 6

# Q:7
j = []
print(len(j))
# 0

# Q:8
lst = [20, 1, -34, 40, -8, 60, 1, 3]
# a) [20, 1, -34, 40, -8, 60, 1, 3]
# b) [20, 1, -34]
# c) [-8, 60, 1, 3]
# d) [-8, 60, 1, 3]
# e) [40, -8]
# f) [20, 1, -34, 40, -8]
# g) [-8, 60, 1, 3]
# h) [20, 1, -34, 40, -8, 60, 1, 3]
# i) [20, 1, -34, 40]
# j) [1, -34, 40, -8]
# k)
i = -34
if i in lst:
    print("True")
# l)
if i not in lst:
    print("False")
# m) 8

Q:9
A = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] ==> A[0:5] ==> [2, 4, 6, 8, 10]
A = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10] ==> A[6:11] ==> [2, 4, 6, 8, 10]
A = [2, 3, 4, 5, 6, 7, 8, 10] ==> A[0:7:2] + A[7:] ==>! [2, 4, 6, 8, 10]
A = [2, 4, 6, 'a', 'b', 'c', 8, 10] ==> A[0:3] + A[6:] ==> [2, 4, 6, 8, 10]
A = [2, 4, 6, 8, 10] ==> A[0:5] ==> [2, 4, 6, 8, 10]
A = [] ==> IMPOSSIBLE !! HOWEVER => A[0:] + [2, 4, 6, 8, 10] ==> [2, 4, 6, 8, 10]
A = [10, 8, 6, 4, 2] ==> A[-1:-6:-1] ==> [2, 4, 6, 8, 10]
A = [2, 4, 6] ==> IMPOSSIBLE !! HOWEVER => A[0:4] + [8, 10] ==> [2, 4, 6, 8, 10]
A = [6, 8, 10] ==> IMPOSSIBLE !! HOWEVER => [2, 4] + A[0:4] ==> [2, 4, 6, 8, 10]
A = [2, 10] ==> IMPOSSIBLE !! HOWEVER => A[0:1] + [4, 6, 8] + A[1:2] ==> [2, 4, 6, 8, 10]
A = [4, 6, 8] ==> IMPOSSIBLE !! HOWEVER => [2] + A[0:3] + [10] ==> [2, 4, 6, 8, 10]

Q:10
a) [8, 8, 8, 8]
b) [2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7]
c) [1, 2, 3, 'a', 'b', 'c', 'd']
d) [1, 2, 1, 2, 1, 2, 4, 2]
e) [1, 2, 4, 2, 1, 2, 4, 2, 1, 2, 4, 2]

Q:11
a) [3, 5, 7, 9]
b) [50, 60, 70, 80, 90]
c) [12, 15, 18]
d) [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]
e) [(0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2)]

# Q:12
# a)
a = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(a)

# b)
b = [x / 4 for x in range(7)]
print(b)

# c)
pairs = [(x, y) for x in ['a', 'b'] for y in [0, 1, 2]]
print(pairs)

# Q:13
# if the element is in the list it is 'True' if not 'False'

# Q:14
# returnes a new list which has the same elements in reversed order

# # Q:15
def sum_pos(a):
    sum = 0
    for items in a:
        if items >= 0:
            sum += items
    return sum


def main():
    a = [6, -8, 4, -4]
    col = sum_pos(a)
    print(col)


main()

# Q:16
def count_evens(lst):
    count = 0
    element = 0
    for element in lst:
        if element % 2 == 0:
            count += 1
    return count


def main():
    lst = [7, 4, 2, 6, 0]
    add = count_evens(lst)
    print(add)


main()

# Q:17
def print_big_enough(alist, b):
    for digits in alist:
        if digits >= b:
            print(digits)
        else:
            print()


print(print_big_enough([4, 5, 7, 8], 5))

# Q:18
lst = [5, 3, 1]


def next_number(lst):
    spi = 0
    num = 0
    for i in lst:
        if i > spi:
            spi = i

    for i in range(1, spi + 1):
        if i not in lst:
            return i

    return spi + 1


print(next_number(lst))

# Q:19
alist = [1, 2, 3, 4, 5]
L = len(alist)

for i in range(int(L / 2)):
    n = alist[i]
    alist[i] = alist[L - i - 1]
    alist[L - i - 1] = n

print(alist)

# Q:20
def matrix(row, column):
    result = []
    for x in range(row):
        partial_result = []
        for x in range(column):
            partial_result.append(1)
        result.append(partial_result)

    return result


m = matrix(6, 9)
for x in m:
    print(x)

m[2][4] = 0
print("---------------------------")
for x in m:
    print(x)

# # Q:21
# 1
def first_way():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(a)


# 2
def second_way():
    a = []

    for i in range(1, 11):
        a += [i]
    print(a)


# 3
def third_way():
    a = []
    i = 1
    while i < 11:
        a.append(i)
        i += 1
    print(a)


def fourth_way():
    b = [-10, -9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    a = (b[3:13])
    print(a)


def fifth_way(n, a):
    if 11 > n > 0:
        a += [n]
        fifth_way(n + 1, a)
    return a

#1
first_way()
#2
second_way()
#3
third_way()
#4
fourth_way()
#5
print(fifth_way(1, []))
