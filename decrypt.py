from sys import argv
from os import remove
from sys import exit


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
        dest_file = open(filename[3:], 'wb')
        idx = 0
        for line in src_file:
            if idx % 2 == 1:
                dest_file.write(line)
            idx += 1    
    else:
        src_file = open(filename, 'r')
        dest_file = open(filename[3:], 'w')
        for char in src_file.read():
            dest_file.write(chr(ord(str(char)) - 1))
except:
    print('Can not decrypt it!')
    success = False
finally:
    src_file.close()
    dest_file.close()

if success:
    remove(filename)
else:
    remove(filename[3:])