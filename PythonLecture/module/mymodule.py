myvariable = "This is global variable" 




def myfunc():
    print("This is my function!!")

def _anotherfunc():
    print("This is another function!!")


if __name__ == "__main__":
    myfunc()
    _anotherfunc()
    print(myvariable)
    print("This is mymodule")