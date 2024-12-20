fruits_color = {"apple": "red","lemon": "yellow", "grapes": "puple"}

if "peach" in fruits_color:
    print(fruits_color["peach"])
else:
    print("the key is not found")

# .get()
fruit = input("フルーツの名前を指定してください")
print(fruits_color.get("fruit", "nothing")) 

#　update()
fruits_color2 = {"peach": "pink", "kiwi": "green"}
fruits_color.update(fruits_color2)
print(fruits_color)