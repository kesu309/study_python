import re

# Regular Expression (正規表現　通称RegEx)

# email = "myemail@gmail.com"
# print("@" in email)

# matched = re.search("@\w\.", email)
# print(matched)

# matched = re.search("@\w+\.", email)
# if matched:
#     print(matched)
#     print("Matched")
# else: 
#     print("Not found")
# print(re.search("[abc]", "apple"))

# ^ 最初の文字
# print(re.search("^[0-9]", "test0"))

# {n} n回リピート
# print(re.search("^[0-9]{4}", "21/3/31"))

# {n, m} 最低n回, 最高m回リピート
# print(re.search("^[0-9]{2,4}", "21/3/31"))

# $　最後の文字
# print(re.search("[0-9]{2}$", "2021/3/31"))

# *左のパターンを0回以上繰り返す
# print(re.search("a*b", "a"))

# + 左のパターンを1回以上繰り返す
# print(re.search("a+b", "a"))

# ?　左のパターンを0回か1回繰り返す
# print(re.search("ab?c", "abbbc"))

# | or
# print(re.search("abc | 012", "abc"))

# () グループ
# print(re.search("te(s | X)", "tet"))

# . 任意の１文字
# print(re.search("h.t", "hot"))

# \ エスケープ
# print(re.search("h\.t", "h.t"))

# \w [a-zA-Z0-9] 全てのアルファベット,数字およびアンダースコア
# print(re.search("h\wt"))


# pattern_dob = "^(19|20)[0-9]{2}/(0[1-9]|1[0-2])/(0[1-9]|[12]|[0-9]|3[01])$"
# while True:
#     dob = input("生年月日を入力してください(yyyy/mm/dd)")
#     result = re.search(pattern_dob, dob)
#     if result:
#         print(f"{dob}は正しいフォーマットです")
#         break
#     else:
#         print(f"{dob}は正しくないフォーマットです。再度入力してください。")


pattern_email = "^(\w|.|-)+@(\w|.|-)+\.[a-zA-Z]{2,3}$"
while True:
    email = input("emailを入力してください(yyyy/mm/dd)")
    result = re.search(pattern_email, email)
    if result:
        print(f"{email}は正しいフォーマットです")
        break
    else:
        print(f"{email}は正しくないフォーマットです。再度入力してください。")