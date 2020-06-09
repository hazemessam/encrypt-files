from sys import argv
from os import remove


filename = argv[1]
src_img = open(filename, 'rb')
dest_img = open(filename[3:], 'wb')

idx = 0
for line in src_img:
    if idx % 2 == 1:
        dest_img.write(line)
    idx += 1
        
src_img.close()
dest_img.close()
remove(filename)