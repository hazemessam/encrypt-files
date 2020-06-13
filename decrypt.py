#!/bin/python3
from sys import argv
from os import remove, rename


src_name = argv[1]
dest_name = src_name.split('.enc')[0] if src_name.endswith('.enc') else f'{src_name}.dec'
success = True

try:
    # Decrypt as a text-based file
    src_file = open(src_name, 'r')
    dest_file = open(dest_name, 'w')
    for char in src_file.read():
        dest_file.write(chr(ord(str(char)) - 1))
except:
    success = False
finally:
    src_file.close()
    dest_file.close()

if not success:
    success = True
    try:
        # Decrypt as a byte-based file
        src_file = open(src_name, 'rb')
        dest_file = open(dest_name, 'wb')
        idx = 0
        for line in src_file:
            if idx % 2 == 1:
                dest_file.write(line)
            idx += 1    
    except:
        success = False
        print('Can not decrypt it!')
    finally:
        src_file.close()
        dest_file.close()

if success:
    remove(src_name)
    if dest_name.endswith('.dec'):
        rename(dest_name, dest_name.split('.dec')[0])
else:
    remove(dest_name)