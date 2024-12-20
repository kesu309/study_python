# 再帰関数（recursive function）: 関数内で自身の関数をcallする
# 階乗（factorial): 3! = 3　×　2 ×　1 = 6
# n! = n * (n-1) *(n-2)* ... * 1

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))

def fibonacci_recursive(n):
    if n < 2:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
print(fibonacci_recursive(6))

def fibonacci(n):
    if n < 2: