def positive_sum(list):
    answer = 0
    for numbers in list: 
        if numbers > 0:
            answer += numbers
    return answer

def positive_sum(arr):
    return sum(filter(lambda x: x > 0,arr))

def positive_sum(arr):
    ''' I really hate these one line codes, but here I am...
        trying to be cool here... and writing some'''
    return sum(map(lambda x: x if x > 0 else 0, arr))

def positive_sum(arr):
    return sum( max(i, 0) for i in arr )