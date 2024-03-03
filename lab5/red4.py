import re
txt=" Av vvA ADFVb bsdd  a_c"
x=re.findall(r'[A-Z][a-z]+',txt)
print(x)