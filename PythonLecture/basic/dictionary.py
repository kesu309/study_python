# dictionary: キーと値の組み合わせを複数保持するデータ型

fruits_colors = {"apple": "red","lemon": "yellow","grapes": "puple"}

# print(fruits_colors["apple"])
# fruits_colors["peach"] = "pink"
# print(fruits_colors)
# dict_sample = {1: "one","two": 2,"three": [1, 2, 3],"four": {"inner": "dict"}}
# print(dict_sample)
# print(dict_sample["four"]["inner"])

# colors = {}
# colors[1] = "blue"
# colors[0] = "red"
# colors[2] = "green"
# print(colors)

# keys() values()
for color in fruits_colors.values():
    print(color)

for x in fruits_colors:      #一緒だが、よりわかりやすいのは上
    print(x)

#item
for fruit, color in fruits_colors.items():
    print(f"{fruit} is {color}")