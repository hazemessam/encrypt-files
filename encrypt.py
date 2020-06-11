from os import remove
from sys import argv


filename = argv[1]
success = True

try:
    # Encrypt as a text-based file
    src_file = open(filename, 'r')
    dest_file = open(f'en-{filename}', 'w')
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
        src_file = open(filename, 'rb')
        dest_file = open(f'en-{filename}', 'wb')
        for line in src_file:
            dest_file.write(b'\x0b\n' + line)
    except:
        success = False
        print('Can not encrypt it!')
    finally:
        src_file.close()
        dest_file.close()

if success:
    remove(filename)
else:
    remove(f'en-{filename}')