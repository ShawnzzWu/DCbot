
import pandas as pd
import json


#Feedback resources
path = 'D:\dcbot'

voice_path = 'D:\\dcbot\\voice'

FFmpeg = "D:\\dcbot\FFmpeg\\ffmpeg-6.0-full_build-shared\\bin\\ffmpeg.exe"

pf = pd.read_csv(path + '\pf.csv')
ef = pd.read_csv(path + '\ef.csv', keep_default_na=False)


with open(path + '//target.json', 'r') as jsfile:
    target = json.load(jsfile)
jsfile.close()

voice_client = None