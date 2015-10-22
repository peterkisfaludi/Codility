# https://codility.com/demo/results/trainingS7YZYS-FYG/

def solution(A):
    # write your code in Python 2.7
    A=[abs(x) for x in A]
    return len(set(A))