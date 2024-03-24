string = str(input())
def acceptcount(string):
    count_upper_case = count_lower_case = 0
    for i in string:
        if i.upper() == i:
            count_upper_case +=1
        
    return count_upper_case
x = acceptcount(string)
print("Upper case : ", x ,"Lower case : ", len(string) - x) 
   