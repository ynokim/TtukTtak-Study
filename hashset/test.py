#TEST IMAGE LOCATION: /Users/ynokim/Library/Mobile Documents/com~apple~CloudDocs/Documents/study/BoB_Study/git/TtukTtak-Study/hashset/images
#HASH LOCATION : /Users/ynokim/Library/Mobile Documents/com~apple~CloudDocs/Documents/study/BoB_Study/git/TtukTtak-Study/hashset/hash.txt

import hashlib
import os
from PIL import Image

img_list = []
count = 0
count_hash = 0

#input hash file
input_filename = input("Input Hash File Name: ")
input_filename += ".txt"
input_take = open(input_filename, 'r')

while True:
    line = input_take.readline()
    line = line.strip()
    img_list.append(line)
    if not line:
        break
    #print(line)
    img_list[count] = line
    count += 1

#input directory
find_directory = input("Input Directory you want to find: ")
file_list = os.listdir(find_directory)

#check md5 match
def compare_md5(text, count):
    global count_hash
    for j in range(0, count):
        if text == img_list[j]:
            count_hash = j
            return 1
        else:
            pass
    return 0

#compare md5 hash
for repeat in range(len(file_list)):
    with open(find_directory + '/' + file_list[repeat], 'rb') as file_take:
        file_reader = file_take.read(4096)
        #print(file_reader)

        extension = os.path.splitext()

        enc = hashlib.md5()
        enc.update(file_reader)
        enc_text = enc.hexdigest()
        check = compare_md5(enc_text, count)
        #print(check)
    if check:
        print(" %s'S HASH [%s] IS MATCHED: [%s] " % (file_list[repeat], enc_text, img_list[count_hash]))
    else:
        print(" %s'S HASH [%s] IS NOT MATCHED: [%s] " % (file_list[repeat], enc_text, img_list[count_hash]))
        pass
