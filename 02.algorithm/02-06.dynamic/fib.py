# 메모이제이션
# def fib(n,memo):
#     if n ==0 or n == 1:
#         return n
#     if not memo.get(n):
#         memo[n] = fib(n-2,memo) + fib(n-1,memo)
#     return memo[n]

# print(fib(6,{}))

# 상향식 DP
def fib(n):
    if n==0:
        return 0
    
    a = 0
    b = 1

    for i in range(1,n):
        temp = a
        a = b
        b = temp + a

    return b
