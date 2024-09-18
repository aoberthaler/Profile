'''
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''
def solution(A):
    # Implement your solution here
    maximum = max(A)
    minimum = min(A)
    if maximum <= 0:
        return 1
    elif minimum > 1:
        return 1

    #Else loop to find a solution
    else:
        cache = 0
        for element in sorted(set(A)):
            if element <= cache:
                pass
            else:
                if element == cache + 1:
                    cache = element
                else:
                    return cache + 1
        return cache + 1

    pass

print(solution[-3,-1])