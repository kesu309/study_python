# if文

age = 20
age_alcohol = 21
if age >= age_alcohol:
    print("You can drink beer!")
else:
    print("You can too young to drink beer")


age_drive = 18
if age >= age_alcohol: #False
    print("You can drink beer!")
elif age < age_drive: #そうではないけどもし〇〇なら（別の条件）#False
    print("You cannot even drive!")
else:
    print("You are not allowed to drink beer but you can drive only if you have a driver's license ")

if not 0 < age < 120: #もしageがこの範囲でなければ
    print("The value is invalid!!")

balance = 1000000
withdrawal = 1300000
# if balance > withdrawal:
#     balance = balance - withdrawal
#     print("Your new balance is {}".format(balance))
# else:
#     print("You dont have money")

withdrawal_limit = 10000000

if withdrawal > withdrawal_limit:
    print("引き出せません")
elif balance > withdrawal:
    balance -= withdrawal
    print("Your new balance is {}".format(balance))