d1 = datetime(2020, 5, 17)
d2 = datetime(2020, 12, 22)

if(d1 > d2):
    print((d1-d2).total_seconds())
else:
    print((d2-d1).total_seconds())