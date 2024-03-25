import sys
import os

path_to_videos = sys.argv[1]

file_list = os.listdir(path_to_videos)

if 'mylist.txt' in file_list:
    file_list.remove('mylist.txt')

if 'output.mp4' in file_list:
    file_list.remove('output.mp4')

video_dict = {}
for file in file_list:
    clean_file = file.split('.')[0]
    order_number = clean_file.split('_')[1]
    video_dict[file] = int(order_number)

order_dict = dict(sorted(video_dict.items(), key=lambda item: item[1]))

order_dict_keys = list(order_dict.keys())

with open(path_to_videos + '/mylist.txt', 'w') as mylist:
    for file in order_dict_keys:
        mylist.write("file '{}'\n".format('./' + file))
