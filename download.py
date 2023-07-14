import subprocess
import configparser

config = configparser.ConfigParser()  
configFilePath = r'input.config'
config.read(configFilePath)

listLink = []
with open(config['DEFAULT']['m3u8FileName'], 'r') as filehandle:
    for line in filehandle:
        curr_place = line[:-1]
        listLink.append(curr_place)

i = 1
for link in listLink:
    subprocess.run(['C:\\Users\\phanhuydung\\Downloads\\mp3\\ffmpeg-2023-06-26-git-285c7f6f6b-full_build\\bin\\ffmpeg.exe', 
                    '-i', link, '-c', 'copy', config['DEFAULT']['fileName'] + '-Bai' + str(i) + '(' + link.split('/')[-3].split('.')[0] + ').mp4'])
    i = i + 1
