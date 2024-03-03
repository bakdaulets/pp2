import re  
data = "TermiNal"
x = re.sub("[A-Z]", " " , data)
print(x)