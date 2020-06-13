#!/bin/python3
from os import remove
from sys import argv


src_name = argv[1]
dest_name = f'{src_name}.enc'
success = True

try:
    # Encrypt as a text-based file
    src_file = open(src_name, 'r')
    dest_file = open(dest_name, 'w')
    for char in src_file.read():
        dest_file.write(chr(ord(str(char)) + 1))
except:
    success = False
finally:
    src_file.close()
    dest_file.close()

if not success:
    success = True
    try:
        # Encrypt as a byte-based file
        src_file = open(src_name, 'rb')
        dest_file = open(dest_name, 'wb')
        for line in src_file:
            dest_file.write(b'\x0b\n' + line)
    except:
        success = False
        print('Can not encrypt it!')
    finally:
        src_file.close()
        dest_file.close()

if success:
    remove(src_name)
else:
    remove(dest_name)