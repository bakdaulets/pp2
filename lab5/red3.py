import re
txt=" Av vvA ADFVb bsdd  a_c"
x=re.findall(r'[a-z]+_[a-z]+',txt)
print(x)