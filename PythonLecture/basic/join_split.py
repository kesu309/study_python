# join
text = " ".join(["Hi", "My", "name", "is", "john" ])
text = "**".join(["Hi", "My", "name", "is", "john" ])
print(text)
# "Hi My name is John"

# split
print("Hi My name is John".split(" "))
print("Hi My name is John".split("/"))

filename = "sample.py"
print(filename.split(".")[0])