# in演算子
fruits = ["apple", "peach", "grapes", "banana"]
print("lemon" not in fruits)
print("h" in "hello")

hearing = input("好きなフルーツは何ですか？")

if hearing in fruits:
    # フルーツを削除
    fruits.remove(hearing)
    print("{}ですね、差し上げますよ".format(hearing))
else:
    # フルーツを追加
    fruits.append(hearing)
    print("{}ですね、仕入れました".format(hearing))

print("今あるフルーツはこちらです{}".format(fruits))