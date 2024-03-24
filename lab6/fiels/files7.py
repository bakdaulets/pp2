import os
with open(r"C:\\Users\\baha\\Desktop\\code\\py\\lab6\\fiels\\6.txt", 'r') as f:
    date = f.read()
with open(r"__file__", 'w') as fy:
    fy.write(date)