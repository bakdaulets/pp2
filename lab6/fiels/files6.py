import os 
Engalp= "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
Listofalp = list(map(str , Engalp.split(" "))) 
for char in Listofalp:    
    with open( char +".txt", "w") as file:
        file.write("6")