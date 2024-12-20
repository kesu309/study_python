# 関数の中で関数を定義（nested function）
# def outer(outer_param):
#     def inner():
#         print("This is inner function")
#         print(outer_param)
#     inner()

# outer("outer arg")
# # inner()

msg = "I am global"

def outer():
    msg = "I am outer"

    def inner():
        nonlocal msg  # I am outerを指していたが、I　am innerにシフトする
        msg = "I am inner"
        print("This is inner function")
        print(msg)
    inner()
    print(msg)

outer()
print(msg)