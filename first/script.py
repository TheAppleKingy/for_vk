import pathlib
import datetime
import sys
import pandas as pd

date=datetime.datetime.strptime(sys.argv[1:][0],'%Y-%m-%d')
print(date)

filesdirs=pathlib.Path('D:/vkdata/first/inputlogs/')#получили имена файлов(тк имя файла содержит только дату то сразу перевели в формат datetime) которые нам нужны
filesdt=[datetime.datetime.strptime(str(i).split('\\')[-1][:-4:],'%Y-%m-%d') for i in filesdirs.rglob('*') if datetime.timedelta(0)<=(date-datetime.datetime.strptime(str(i).split('\\')[-1][:-4:],'%Y-%m-%d'))<=datetime.timedelta(7)]

commonframe=pd.concat([pd.read_csv(f'D:/vkdata/first/inputlogs/{i.year}-{i.month}-{i.day}.csv') for i in filesdt],axis=0,ignore_index=True)

res=pd.DataFrame(columns=['email','CREATE_count','READ_count','UPDATE_count','DELETE_count'])
for i in commonframe['email'].unique():#для удобства использую датафреймы и получаю датафрейм с небходимой информацией 
    res.loc[len(res)]=(i,len(commonframe[(commonframe['email']==i)&(commonframe['action']=='CREATE')]),len(commonframe[(commonframe['email']==i)&(commonframe['action']=='READ')]),len(commonframe[(commonframe['email']==i)&(commonframe['action']=='UPDATE')]),len(commonframe[(commonframe['email']==i)&(commonframe['action']=='DELETE')]))

res.to_csv(f'D:/vkdata/first/output/{date.strftime('%Y-%m-%d')}.csv',index=False,sep='\t')



