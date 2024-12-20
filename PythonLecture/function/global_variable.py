CALL_COUNT = 0 #constant variable 大文字の場合は暗黙の了解で書き換えない

def print_count1():
    global CALL_COUNT
    CALL_COUNT += 1
    print(f"関数1: {CALL_COUNT}回目")

def print_count2():
    global CALL_COUNT
    CALL_COUNT += 1
    print(f"関数2: {CALL_COUNT}回目")

print_count1()
print_count2()
print_count1()
print_count1()