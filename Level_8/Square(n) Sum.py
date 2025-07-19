# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9

def square_sum1(numbers):
    sum = 0
    for x in numbers:
        sum+= x**2
    return sum

def square_sum22(numbers):
    return sum(x ** 2 for x in numbers)

square_sum = lambda n: sum(e**2 for e in n)
def summation2(num):
    return sum(range(1,num+1))





