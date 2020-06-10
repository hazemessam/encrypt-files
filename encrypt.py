from os import remove
from sys import argv


def is_media_based(filename):
    media_types = ['.mp4', '.mp3', '.png', '.jpg', 'jif', '.pdf', '.exe']
    for media_type in media_types:
        if filename.lower().endswith(media_type):
            return True
    return False

filename = argv[1]
success = True
try:
    if is_media_based(filename):
        src_file = open(filename, 'rb')
        dest_file = open(f'en-{filename}', 'wb')
        for line in src_file:
            dest_file.write(b'\x0b\n' + line)
    else:
        src_file = open(filename, 'r')
        dest_file = open(f'en-{filename}', 'w')
        for char in src_file.read():
            dest_file.write(chr(ord(str(char)) + 1))
except:
    print('Can not encrypt it!')
    success = False
finally:
    src_file.close()
    dest_file.close()

if success:
    remove(filename)
else:
    remove(f'en-{filename}')