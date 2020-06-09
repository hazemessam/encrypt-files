from os import remove
from sys import argv

filename = argv[1]
src_img = open(filename, 'rb')
dest_img = open(f'en-{filename}', 'wb')

for line in src_img:
    dest_img.write(b'\x0b\n' + line)

src_img.close()
dest_img.close()

remove(filename)