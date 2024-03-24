import os
print('Exist:', os.access('C:\\Users\\baha\\Desktop\\code\\py', os.F_OK))
print('Readable:', os.access('C:\\Users\\baha\\Desktop\\code\\py', os.R_OK))
print('Writable:', os.access('C:\\Users\\baha\\Desktop\\code\\py', os.W_OK))
print('Executable:', os.access('C:\\Users\\baha\\Desktop\\code\\py', os.X_OK))