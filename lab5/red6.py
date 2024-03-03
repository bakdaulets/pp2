import re
data = "wwewfw erfrw,rf43"
x = re.sub("[\s,.]" , ":" , data)
print(x)