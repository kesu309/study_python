# args
print("Hello", "world", "test")
def get_avrage(*args):
    num = len(args)
    if num == 0:
        return 0
    total = sum(args)
    return total / num


average = get_avrage(1, 2, 3, 4, 5)
print(average)

# **kwargs
def kwargs_func(**kwargs):
   param1 =kwargs.get("param1", 1)
   param2 =kwargs.get("param2", 2)
   param3 =kwargs.get("param3", 3)

   print(f"param1: {param1}, param2: {param2}, param3: {param3}")

kwargs_func(param1=10, param2=6, param3=100)

# *と**はunpacking operator
numbers = (1, 2, 3)
print(*numbers)
