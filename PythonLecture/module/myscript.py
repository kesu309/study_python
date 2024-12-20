# 標準ライブラリ, サードパーティのライブラリ, 自分たちのライブラリ, 
import sys
sys.path.append("C:/Users/shiga/udemy/PythonLecture/function")
import docstring
import mymodule as mm
# from mymodule import myfunc, myvariable, anotherfunc
# from mymodule import *
# mymodule.myfunc()
mm.myfunc()
mm._anotherfunc()
print(mm.myvariable)
# print(mymodule.myvariable)
print(sys.path)
print(docstring.multiply(3, 4))