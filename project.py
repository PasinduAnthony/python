import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os

raw_data = os.listdir("raw data")

df1 = pd.read_csv('raw data/120_FT DDMG.csv')
df1['date'] = pd.to_datetime(df1['ActivityDates(Individual)']+' '+df1['ScheduledStartTime'])
df2 = pd.read_csv('raw data/120_FT DM.csv')
df2['date'] = pd.to_datetime(df2['ActivityDates(Individual)']+' '+df2['ScheduledStartTime'])
df3 = pd.read_csv('raw data/120_FT ICOS.csv')
df3['date'] = pd.to_datetime(df3['ActivityDates(Individual)']+' '+df3['ScheduledStartTime'])

#filename2 = "raw data/" + raw_data[int(userinput)]
dconcat = pd.concat([df1,df2,df3])
print(dconcat.__len__())

newindex = []
for y in range(dconcat.__len__()):
    newindex.append(y+1)

dconcat.drop('Unnamed: 0',inplace=True,axis=1)
print(dconcat)
dconcat.to_csv('raw data/test.csv')
dconcat['index'] = newindex
dconcat.sort_values(by='date')
dconcat = dconcat.set_index('index')
#print(dconcat['date'])

dfm = dconcat[dconcat.ScheduledDays.isin(['Monday'])]
#dfm = dfm.sort_values(by='ActivityDates(Individual)')
dfm1 = dfm[dfm.ScheduledStartTime.isin(['8:30:00'])]
dfm2 = dfm[dfm.ScheduledStartTime.isin(['12:00:00'])]
dfm3 = dfm[dfm.ScheduledStartTime.isin(['15:30:00'])]

print(dfm.__len__())
dft = dconcat[dconcat.ScheduledDays.isin(['Tuesday'])]
#dft.sort_values(by='ActivityDates(Individual)')
dft1 = dft[dft.ScheduledStartTime.isin(['8:30:00'])]
dft2 = dft[dft.ScheduledStartTime.isin(['12:00:00'])]
dft3 = dft[dft.ScheduledStartTime.isin(['15:30:00'])]

dfw = dconcat[dconcat.ScheduledDays.isin(['Wednesday'])]
#dfw.sort_values(by='ActivityDates(Individual)')
dfw1 = dfw[dfw.ScheduledStartTime.isin(['8:30:00'])]
dfw2 = dfw[dfw.ScheduledStartTime.isin(['12:00:00'])]
dfw3 = dfw[dfw.ScheduledStartTime.isin(['15:30:00'])]

dfth = dconcat[dconcat.ScheduledDays.isin(['Thursday'])]
#dfth.sort_values(by='ActivityDates(Individual)')
dfth1 = dfth[dfth.ScheduledStartTime.isin(['8:30:00'])]
dfth2 = dfth[dfth.ScheduledStartTime.isin(['12:00:00'])]
dfth3 = dfth[dfth.ScheduledStartTime.isin(['15:30:00'])]

dff = dconcat[dconcat.ScheduledDays.isin(['Friday'])]
#dff.sort_values(by='ActivityDates(Individual)')
dff1 = dff[dff.ScheduledStartTime.isin(['8:30:00'])]
dff2 = dff[dff.ScheduledStartTime.isin(['12:00:00'])]
dff3 = dff[dff.ScheduledStartTime.isin(['15:30:00'])]

dfv = pd.DataFrame({
    'Mon (8.30-11.00am)': dfm1['Name'],
    'Mon (12.00-3.00pm)': dfm2['Name'],
    'Mon (3.30-6.30pm)': dfm3['Name'],
    'Tue (8.30-11.00am)': dft1['Name'],
    'Tue (12.00-3.00pm)': dft2['Name'],
    'Tue (3.30-6.30apm)': dft3['Name'],
    'Wed (8.30-11.00am)': dfw1['Name'],
    'Wed (12.00-3.00pm)': dfw2['Name'],
    'Wed (3.30-6.30pm)': dfw3['Name'],
    'Thur (8.30-11.00am)': dfth1['Name'],
    'Thur (12.00-3.00pm)': dfth2['Name'],
    'Thur (3.30-6.30pm)': dfth3['Name'],
    'Fri (8.30-11.00am)': dff1['Name'],
    'Fri (12.00-3.00pm)': dff2['Name'],
    'Fri (3.30-6.30pm)': dff3['Name'],
})
#,index=['0','2','3','4','5','6','7','8','9','10','11','12'])

print(dfv)
dfv.to_csv("raw data/Humidity.csv")
#df.ScheduledDays.unique()