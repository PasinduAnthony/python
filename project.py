import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os



raw_data = os.listdir("raw data")

df1 = pd.read_csv('raw data/120_FT DDMG.csv')
df2 = pd.read_csv('raw data/120_FT DM.csv')
df3 = pd.read_csv('raw data/120_FT ICOS.csv')

dconcat = pd.concat([df1,df2,df3])
#print(dconcat)

newindex = []
for y in range(dconcat.__len__()):
    newindex.append(y+1)

#Deleting unwated column
dconcat.drop('Unnamed: 0',inplace=True,axis=1)

dconcat['index'] = newindex
#dconcat.sort_values(by='date')
dconcat = dconcat.set_index('index')
#print(dconcat['date'])



data = {'name': [],
	'physics': [],
	'chemistry': []}

#create dataframe
df_marks = pd.DataFrame(data)
#print('Original DataFrame\n------------------')
#print(df_marks)

new_row = pd.Series(data={'name':'Geo', 'physics':87, 'chemistry':92}, name='x')
#append row to the dataframe
df_marks = df_marks.append(new_row, ignore_index=True)

#print('\n\nNew row added to DataFrame\n--------------------------')
#print(df_marks)

#df['date'] = pd.to_datetime(df['date'],format='%d-%m-%Y').dt.strftime('%Y-%m-%d')#specify input format '%d-%m-%Y' and output format '%Y-%m-%d' or change output as desired i.e. %d/%m/%Y

dconcat['dateonly'] = pd.to_datetime(dconcat['ActivityDates(Individual)'])
print(dconcat['dateonly'].shape)
dconcat['dateonly'] = pd.to_datetime(dconcat['dateonly'])
dconcat = dconcat.sort_values(by='dateonly')


dconcat.to_csv('raw data/test.csv')


data = {
    'Mon (8.30-11.30am)': [],
    'Mon (12.00-3.00pm)': [],
    'Mon (3.30-6.30pm)': [],
    'Tue (8.30-11.30am)': [],
    'Tue (12.00-3.00pm)': [],
    'Tue (3.30-6.30apm)': [],
    'Wed (8.30-11.30am)': [],
    'Wed (12.00-3.00pm)': [],
    'Wed (3.30-6.30pm)': [],
    'Thur (8.30-11.30am)': [],
    'Thur (12.00-3.00pm)': [],
    'Thur (3.30-6.30pm)': [],
    'Fri (8.30-11.30am)': [],
    'Fri (12.00-3.00pm)': [],
    'Fri (3.30-6.30pm)': [],
}

df_data = pd.DataFrame(data)

print(dconcat.__len__())

count = 0
i = 0

#print(pd.to_datetime(dconcat.iloc[0]['ActivityDates(Individual)']))
#print(pd.to_datetime(dconcat.iloc[64]['ActivityDates(Individual)']))

generatedDays_DateType = pd.date_range(start='2020-01-06', end='2020-03-17')

generated_days = {'fulldate': generatedDays_DateType.strftime("%Y-%m-%d"),
    'year': generatedDays_DateType.strftime("%Y"),
	'month': generatedDays_DateType.strftime("%m"),
	'days': generatedDays_DateType.strftime("%d"),
    'output': generatedDays_DateType.strftime("%A. %d %B %Y")}

generated_daysDF = pd.DataFrame(generated_days)
print(generated_daysDF)
#generated_days = generated_days.set_index('Index')

# = ''
# day = generated_daysDF.iloc[7]['days']+'/'+generated_daysDF.iloc[7]['month']+'/'+generated_daysDF.iloc[7]['year']
# dtrim2 = dconcat.loc[dconcat['dateonly'] == day, :]
# print('output : ', dtrim2.iloc[0])
# print(generated_daysDF.iloc[0]['output'])

i = 0
while (i != (generated_daysDF.__len__())):
    m8visit = False
    m12visit = False
    m15visit = False
    t8visit = False
    t12visit = False
    t15visit = False
    w8visit = False
    w12visit = False
    w15visit = False
    th8visit = False
    th12visit = False
    th15visit = False
    f8visit = False
    f12visit = False
    f15visit = False

    m8 = ''
    m12 = ''
    m15 = ''
    t8 = ''
    t12 = ''
    t15 = ''
    w8 = ''
    w12 = ''
    w15 = ''
    th8 = ''
    th12 = ''
    th15 = ''
    f8 = ''
    f12 = ''
    f15 = ''

    y = 0
    while (y != 5):
        #print('dconct : '+dconcat_iloc2['ActivityDates(Individual)'])
        #dtrim = dconcat.loc[dconcat['ActivityDates(Individual)'] == dconcat_iloc2['ActivityDates(Individual)'], :]
        #print('week : ',i)
        day2 = generated_daysDF.iloc[i]['days'] + '/' + generated_daysDF.iloc[i]['month'] + '/' +generated_daysDF.iloc[i]['year']
        dtrim = dconcat.loc[dconcat['dateonly'] == day2, :]
        #print(dtrim)
        day = str(generated_daysDF.iloc[i]['output'])
        #print(day)
        if(y==0):
            m8 = day
            m12 = day
            m15 = day
        elif(y==1):
            t8 = day
            t12 = day
            t15 = day
        elif(y==2):
            w8 = day
            w12 = day
            w15 = day
        elif(y==3):
            th8 = day
            th12 = day
            th15 = day
        elif(y==4):
            f8 = day
            f12 = day
            f15 = day

        for x in range(dtrim.__len__()):
            startTime = dtrim.iloc[x]['ScheduledStartTime']
            dconcat_iloc = dtrim.iloc[x]
            #print(startTime + ' ' + dconcat_iloc['ScheduledDays'])

            if (startTime == '8:30:00' and dconcat_iloc['ScheduledDays'] == 'Monday' and m8visit == False and y == 0):
                m8 = str(day) + '\n' + dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                m8visit = True
            print(m8)

            if (startTime == '12:00:00' and dconcat_iloc['ScheduledDays'] == 'Monday' and m12visit == False and y == 0):
                m12 = str(day) + '\n' + dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                m12visit = True
            print(m12)

            if (startTime == '15:30:00' and dconcat_iloc['ScheduledDays'] == 'Monday' and m15visit == False and y == 0):
                m15 = str(day) + '\n' + dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                m15visit = True
            print(m15)

            if (startTime == '8:30:00' and dconcat_iloc['ScheduledDays'] == 'Tuesday' and t8visit == False and y == 1):
                t8 = str(day) + '\n' + dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                t8visit = True
            print(t8)

            if (startTime == '12:00:00' and dconcat_iloc['ScheduledDays'] == 'Tuesday' and t12visit == False and y == 1):
                t12 = str(day) + '\n' + dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                t12visit = True
            print(t12)

            if (startTime == '15:30:00' and dconcat_iloc['ScheduledDays'] == 'Tuesday' and t15visit == False and y == 1):
                t15 = str(day) + '\n' + dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                t15visit = True
            print(t15)

            if (startTime == '8:30:00' and dconcat_iloc['ScheduledDays'] == 'Wednesday' and w8visit == False and y == 2):
                w8 = str(day) + '\n' + dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                w8visit = True
            print(w8)

            if (startTime == '12:00:00' and dconcat_iloc['ScheduledDays'] == 'Wednesday' and w12visit == False and y == 2):
                w12 = str(day) + '\n' + dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                w12visit = True
            print(w12)

            if (startTime == '15:30:00' and dconcat_iloc['ScheduledDays'] == 'Wednesday' and w15visit == False and y == 2):
                w15 = str(day) + '\n' + dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                w15visit = True
            print(w15)

            if (startTime == '8:30:00' and dconcat_iloc['ScheduledDays'] == 'Thursday' and th8visit == False and y == 3):
                th8 = str(day) + '\n' + dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                th8visit = True
            print(th8)

            if (startTime == '12:00:00' and dconcat_iloc['ScheduledDays'] == 'Thursday' and th12visit == False and y == 3):
                th12 = str(day) + '\n' + dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                th12visit = True
            print(th12)

            if (startTime == '15:30:00' and dconcat_iloc['ScheduledDays'] == 'Thursday' and th15visit == False and y == 3):
                th15 = str(day) + '\n' + dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                th15visit = True
            print(th15)

            if (startTime == '8:30:00' and dconcat_iloc['ScheduledDays'] == 'Friday' and f8visit == False and y == 4):
                f8 = str(day) + '\n' + dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                f8visit = True
            print(f8)

            if (startTime == '12:00:00' and dconcat_iloc['ScheduledDays'] == 'Friday' and f12visit == False and y == 4):
                f12 = str(day) + '\n' + dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                f12visit = True
            print(f12)

            if (startTime == '15:30:00' and dconcat_iloc['ScheduledDays'] == 'Friday' and f15visit == False and y == 4):
                f15 = str(day) + '\n' + dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                f15visit = True
            print(f15)

            count = count + 1

        i = i + 1
        if(y==0):
            temprow = "'Mon (8.30-11.30am)': " + m8 + ", 'Mon (12.00-3.00pm)': " + m12 + ", 'Mon (3.30-6.30pm)': " + m15
        elif(y==1):
            temprow = temprow + ", 'Tue (8.30-11.30am)': " + t8 + ", 'Tue (12.00-3.00pm)': " + t12 + ", 'Tue (3.30-6.30apm)': " + t15
        elif(y==2):
            temprow = temprow + ", 'Wed (8.30-11.30am)': " + w8 + ", 'Wed (12.00-3.00pm)': " + w12 + ", 'Wed (3.30-6.30pm)': " + w15
        elif(y==3):
            temprow = temprow + ", 'Thur (8.30-11.30am)': " + th8 + ", 'Thur (12.00-3.00pm)': " + th12 + ", 'Thur (3.30-6.30pm)': " + th15
        elif(y==4):
            temprow = temprow + ", 'Fri (8.30-11.30am)': " + f8 + ", 'Fri (12.00-3.00pm)': " + f12 + ", 'Fri (3.30-6.30pm)': " + f15
        y = y + 1

    i = i + 1 #to skip sat & sun

    print(temprow)

    #new_row = pd.Series(
        #data={'Mon (8.30-11.30am)': m8, 'Mon (12.00-3.00pm)': m12, 'Mon (3.30-6.30pm)': m15, 'Tue (8.30-11.30am)': t8,
              #'Tue (12.00-3.00pm)': t12, 'Tue (3.30-6.30apm)': t15, 'Wed (8.30-11.30am)': w8, 'Wed (12.00-3.00pm)': w12,
              #'Wed (3.30-6.30pm)': w15, 'Thur (8.30-11.30am)': th8, 'Thur (12.00-3.00pm)': th12,
              #'Thur (3.30-6.30pm)': th15, 'Fri (8.30-11.30am)': f8, 'Fri (12.00-3.00pm)': f12,
              #'Fri (3.30-6.30pm)': f15})
    new_row = pd.Series(data={temprow})
    df_data = df_data.append(new_row, ignore_index=True)
   
    print('-------------------------------------------------------')


#print(dfv)
print(df_data)
df_data.to_csv("raw data/Humidity.csv")
#df.ScheduledDays.unique()



