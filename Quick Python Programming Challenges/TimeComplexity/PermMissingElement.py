'''
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
'''

def solution(A):

    # Implement your solution here
    A.sort()

    for i in range(len(A)):

        # Check if first element is missing
        if A[0] != 1:
            return 1

        #Check if last element is missing
        if A[len(A)] != len(A):
            return len(A)

        #Otherwise check all other elements
        if A[i+1] - A[i] == 2:
            return A[i+1]-1

    pass

print(solution([1,4,5,6,2]))
