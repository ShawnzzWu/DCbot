
import pandas as pd
import json


#Feedback resources
path = 'D:\dcbot'

pf = pd.read_csv(path + '\pf.csv')
ef = pd.read_csv(path + '\ef.csv', keep_default_na=False)


with open(path + '//target.json', 'r') as jsfile:
    target = json.load(jsfile)
jsfile.close()