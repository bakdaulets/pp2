import re 
snake_case = "camel_case_something"
otherCamelCase = re.findall("_[a-z]*" , snake_case )
print("{}{}".format(re.sub("_[a-z]*","" ,snake_case), "".join([word[1:].capitalize() for word in otherCamelCase])))
