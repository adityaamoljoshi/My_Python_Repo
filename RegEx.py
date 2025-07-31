import re

f = open("anagha.txt","r")
try:

    a=f.read()

    b = re.sub("A", "4",a)


    print(b)
finally:

    f.close()