import os 
Path = r"C:\\Users\\baha\\Desktop\\code\\py"
if os.path.exists(Path):
    print( "Name of the file :" + os.path.basename(Path))
    print( "Name of the directory :" + os.path.dirname(Path))
else:
    print("Path doesn't exist") 