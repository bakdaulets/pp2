import re
txt = "abb"
x = re.findall(r'a[b]*', txt)
print(x)