import os
list =["1","2","3"]
with open('s.txt', 'w+') as fyle:
    for i in list:
        fyle.write(i + "\n")   