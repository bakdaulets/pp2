import re
txt = "abb abbbb abbb ab"
x = re.findall(r'a[b]*', txt)
print(x)