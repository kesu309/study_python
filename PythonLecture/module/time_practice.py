from functools import lru_cache
import time

# .time(): 1970/1/1 秒数が表示
print(time.time())
print(time.time()/(60*60*24*365))

@lru_cache
def fib(n):
    print(f"fibonacci with {n} is running...")
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

before = time.time()
print(fib(30))
after = time.time()
print(after - before)

# .ctime() 今のローカル時間を文字列で返す
print(time.ctime())

# .localtime = time.localtime()
localtime = time.localtime()
print(localtime)
print(f"今の時刻は{localtime.tm_year}年{localtime.tm_mon}月{localtime.tm_mday}日{localtime.tm_hour}時{localtime.tm_min}分です")
print("今の時刻は{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分です".format(localtime))


# .sleep(secs) secs秒だけプログラムが待機する
sec = 10
print(f"{sec}秒待ってください")
time.sleep(sec)
print(f"{sec}秒経ちました")

def timer(func):
    def inner(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()
        print(f"{func.__name__}took{after-before:.2f}sec")
    return inner


@timer
def lazy_func(sec):
    print(f"I'm working so hard")
    time.sleep(sec)
    print(f"I'm finally done!!")

lazy_func(4)