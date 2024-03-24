import os
if os.path.exists("__file__"):
    os.remove("__file__")
else:
    print("The file does not exist")