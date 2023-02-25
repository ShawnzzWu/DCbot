
import pandas as pd

#Feedback resources
path = 'D:\dcbot'

pf = pd.read_csv(path + '\pf.csv')
ef = pd.read_csv(path + '\ef.csv', keep_default_na=False)