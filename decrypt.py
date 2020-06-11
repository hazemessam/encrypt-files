from sys import argv
from os import remove


filename = argv[1]
success = True

try:
    # Decrypt as a text-based file
    src_file = open(filename, 'r')
    dest_file = open(filename[3:], 'w')
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
        src_file = open(filename, 'rb')
        dest_file = open(filename[3:], 'wb')
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
    remove(filename)
else:
    remove(filename[3:])