# is演算子：同じオブジェクトかどうか判定する
a = 1
b = 1
c = 3
d = a
e = 2 - 1
print(id(1))
print(id(a))
print(id(b))
print(a is b)
print(a is not c)

print(d is a)
print(d is b)

print(a is e)

hello = "hello"
hello2 = "h" + "e" + "l" + "l" + "o" # "hello"
print(hello, hello2)
print(hello is hello2)
hello = "konnichiwa" #ここでhelloを1回削除して新しいhelloとkonnichiwaを作った（別のオブジェクトを作った）
print(hello is hello2) 

# Noneかどうかの判定によく使う

nothing = None
print(nothing is none)
print(id(None))