# range(start, stop, step)
for i in range(4, 25, 2):
    print(i)

# challenge
for i in range(1,51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 15 == 0:
        print("Buzz")
    else:
        print(i)
    