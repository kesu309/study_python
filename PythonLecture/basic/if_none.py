# if文のNoneの取り扱い
a = None
if a is None:
    print("a is None")
else:
    print("a has Value")

if not a:
    print("a has value")
else:
    print("a is None")