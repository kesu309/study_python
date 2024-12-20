age = int(input("何歳ですか？"))
casino_age = 18
# game_text = """プレイするゲームを選択してください
# 1: ルーレット
# 2: ブラックジャック
# 3: ポーカー
# """
game_dict = {"1": "ルーレット", "2": "ブラックジャック", "3": "ポーカー",}

if age >= casino_age:
    print("どうぞお入りください")
    while True:
        print("プレイするゲームを選択してください")
        for num, game_name in game_dict.items():
            print(f"{num}: {game_name}")
        game = input(":")
        if game in game_dict:
            print(f"あなたは{game_dict[game]}を選びました")
            break
        # if game == "1":
        #     print("あなたはルーレットを選びました")
        #     break
        # elif game == "2":
        #     print("あなたはブラックジャックを選びました")
        #     break
        # elif game == "3":
        #     print("あなたはポーカーを選びました")
        #     break
        else:
            print("正しい選択肢を選んでください")
else:
    print(f"{casino_age}歳未満の方はカジノに入れません")