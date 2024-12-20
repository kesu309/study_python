# forループ
fruits = ["apple", "peach", "grapes", "banana"]

# for fruit in fruits:
#     print(f"I love {fruit}!!")

# for char in "hello world!!":
#     print(f"char:{char}")

# # iterationとiterable
# favorite = input("好きなフルーツは何ですか？")
# for fruit in fruits:
#     if fruit == favorite:
#         print(f"I love {fruit}!!")
#     else:
#         print(f"{fruit}は別に好きではない")

favorite_fruits = []
normal_fruits = []
for fruit in fruits:
    choice = input(f"{fruit}は好き？ yes/no")

    if choice == "yes":                       #yesを選んだらfavorite_fruitsに追加される
        favorite_fruits.append(fruit)
    else:
        normal_fruits.append(fruit)

print(f"favorite fruits:{favorite_fruits}")   #最後のprintはchoice list
print(f"normal fruits:{normal_fruits}")