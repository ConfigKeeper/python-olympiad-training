# Complete the solution so that it reverses the string passed into it.
#
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

def solution(string):
    arr = list(string)
    a = ''.join(arr[::-1])
    return a

solution('hello')


solution = lambda s: ''.join(list(s)[::-1])


def solution2(string):
    return string[::-1]