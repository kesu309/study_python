# Whileループ
# count = 0
# while count < 10:
#     print(count)
#     count += 1

# break と　continue
# while True:
#     age = int(input("あなたは何歳ですか？"))
#     if not 0 <= age < 120:
#         print("入力された値は正しくありません")
#         continue                              #例えば-20で入力した場合、正しくないのでcontinueでまた何歳か聞かれる（ループされる）
#     else:                                     #continueはなくてもいい
#         print(f"あなたは{age}歳です")
#         break

age = int(input("何歳ですか？"))
casino_age = 18
game_text = """プレイするゲームを選択してください
1: ルーレット
2: ブラックジャック
3: ポーカー
"""

if age >= casino_age:
    print("どうぞお入りください")
    while True:
        game = input(game_text)
        if game == "1":
            print("あなたはルーレットを選びました")
            break
        elif game == "2":
            print("あなたはブラックジャックを選びました")
            break
        elif game == "3":
            print("あなたはポーカーを選びました")
            break
        else:
            print("1～3を選んでください")
else:
    print("入れません")