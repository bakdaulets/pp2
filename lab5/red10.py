import re

cs = "SomeDataWith"

sc = re.sub(r'(?<!^)(?=[A-Z])', '_', cs)

sc = sc.lower()

print(sc)