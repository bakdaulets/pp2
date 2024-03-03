import re
data = "SomeDataWithSpaces"
x = ""
x = re.findall("[A-Z][a-z]*"  , data )
print(*x)