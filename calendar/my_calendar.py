# 月の日数を計算する関数
def get_num_days(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
# うるう年かどうか判定している
# 基本的に、4で割り切れる年がうるう年（year % 4 == 0）
# ただし、100で割り切れる年はうるう年ではない（year % 100 != 0）
# 例外として、400で割り切れる年はうるう年です（year % 400 == 0）
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return 29
        else:
            return 28
    else:
        return 30

# 指定された年月の1日が週のどの日に当たるかを計算する関数
# 1月1日からその年の1月1日までに経過した「総日数」を計算。具体的には、次のようにうるう年を考慮して計算。
# (year - 1) * 365: 指定された年 year の前年までの通常の365日で計算される日数。
# (year - 1) // 4: うるう年の分だけ1日多い年があるので、year - 1 年までのうるう年の回数を加算します（4で割り切れる年はうるう年）。
# (year - 1) // 100: 100で割り切れる年はうるう年ではないので、これを除外します。
# (year - 1) // 400: 400で割り切れる年はうるう年に戻るため、ここで再度加算します。
def get_first_day(year, month):
    # 1年1月1日が月曜日であることを利用
    days = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    for m in range(1, month):
        days += get_num_days(year, m)
    return (days + 1) % 7

# カレンダーを出力する関数
def print_calendar(year, month):
    num_days = get_num_days(year, month)
    first_day = get_first_day(year, month)

    # 月と年を出力
    print(f"{year}年 {month}月")

    # 曜日の頭文字を出力
    print("日 月 火 水 木 金 土")

    # 1日の前の空白を出力
    print(" " * 3 * first_day, end="")

    # 日付を出力
    for day in range(1, num_days + 1):
        print(f"{day:2d} ", end="")
        if (day + first_day) % 7 == 0:
            print()

    print()  # 改行

# 使用例
print_calendar(2024,11)