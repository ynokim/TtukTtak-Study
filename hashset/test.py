#TEST IMAGE LOCATION: /Users/ynokim/Library/Mobile Documents/com~apple~CloudDocs/Documents/study/BoB_Study/git/TtukTtak-Study/hashset/images
#HASH LOCATION : /Users/ynokim/Library/Mobile Documents/com~apple~CloudDocs/Documents/study/BoB_Study/git/TtukTtak-Study/hashset/hash.txt

import hashlib
import os

img_list = []
count = 0
count_hash = 0

#input hash file
input_filename = input("Input Hash File Name: ")
input_filename += ".txt"
input_take = open(input_filename, 'r')

while True:
    line = input_take.readline()
    img_list.append(line)
    if not line:
        break
    img_list[count] = line
    count += 1

i = count
i -= 1

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
    enc = hashlib.md5()
    enc.update(file_reader)
    enc_text = enc.hexdigest()

    for img_file in os.listdir("./images"):
        check = compare_md5(enc_text, count)
        if check:
            print(" %s 'S HASH IS MATCHED: [%s] " % (file_list[repeat], img_list[count_hash]))
        else:
            pass
