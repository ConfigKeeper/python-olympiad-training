# Your Job
# Find the sum of all multiples of n below m

# Keep in Mind
# n and m are natural numbers (positive integers)
# m is excluded from the multiples
# sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
# sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
# sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
# sumMul(4, -7)  ==> "INVALID"


# MY-----------------------------------------------------------
def sum_mul(n, m):

    if n<=0 or m<=0:
        return "INVALID"
    elif n >= m:
        return 0
    sum = 0
    i = 2
    _n = n
    while _n < m:
        sum += _n
        _n = n * i
        i += 1

        print(sum)
    return sum
print(sum_mul(4, 123))
#NOT MY-----------------------------------------------------------

def sum_mul2(n, m):
    if m>0 and n>0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'
    
def sum_mul3(n, m):
    return sum(x for x in range(n, m, n)) if m > 0 and n > 0 else 'INVALID'

sum_mul4 = lambda n, m: sum(range(n, m, n)) if n > 0 and m > 0 else "INVALID"

sum_mul5 = lambda _,__:sum(range(0,__,_)) if _>0 and __>0 else 'INVALID'