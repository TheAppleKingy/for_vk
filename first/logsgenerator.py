import datetime
import os
import random
import string
import sys
import csv


EMAIL_PROVIDERS = [
    "gmail.com",
    "ya.ru",
    "mail.ru",
]

ACTION_TYPES = [
    "CREATE",
    "READ",
    "UPDATE",
    "DELETE",
]
logscount=random.randint(1,500)
filescount=random.randint(100,500)


for i in range(filescount):
    year=2024
    month=random.randint(1,12)
    day=random.randint(1,28)
    with open(f'D:/vkdata/first/inputlogs/{year}-{month}-{day}.csv','w',newline='') as logsperday:
        logs=csv.writer(logsperday)
        logsperday.write('email,action,dt\n')
        for i in range(logscount):
            logs.writerow([random.choice(EMAIL_PROVIDERS),random.choice(ACTION_TYPES),datetime.datetime(year,month,day,random.randint(0,23),random.randint(0,59),random.randint(0,59))])
