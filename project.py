import pandas as pd
from reportlab.pdfgen import canvas
import os

raw_data = os.listdir("userSelect")
raw_data = pd.DataFrame(raw_data)
print(raw_data)
userinput = input("Enter the number :")
selected = raw_data.iloc[int(userinput)]
selected = selected.to_string()
print("Folder ' " + selected + " ' selected")

if(userinput==0):
    selected = 'raw data'
    raw_data = os.listdir("userSelect/raw data")
    raw_data = pd.DataFrame(raw_data)
    print(raw_data)

df1 = pd.read_csv('userSelect/raw data/120_FT DDMG.csv')
df2 = pd.read_csv('userSelect/raw data/120_FT DM.csv')
df3 = pd.read_csv('userSelect/raw data/120_FT ICOS.csv')

dconcat = pd.concat([df1,df2,df3])
newindex = []
for y in range(dconcat.__len__()):
    newindex.append(y+1)

#Deleting unwated column
dconcat.drop('Unnamed: 0',inplace=True,axis=1)

dconcat['index'] = newindex
dconcat = dconcat.set_index('index')

dconcat['dateonly'] = pd.to_datetime(dconcat['ActivityDates(Individual)'])
print(dconcat['dateonly'].shape)
dconcat['dateonly'] = pd.to_datetime(dconcat['dateonly'])
dconcat = dconcat.sort_values(by='dateonly')

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

generatedDays_DateType = pd.date_range(start='2020-01-06', end='2020-03-17')

generated_days = {'fulldate': generatedDays_DateType.strftime("%Y-%m-%d"),
    'year': generatedDays_DateType.strftime("%Y"),
	'month': generatedDays_DateType.strftime("%m"),
	'days': generatedDays_DateType.strftime("%d"),
    'output': generatedDays_DateType.strftime("%A. %d %B %Y"),
    'outputDay': generatedDays_DateType.strftime("%A"),
    'outputMonth': generatedDays_DateType.strftime("%B")}

generated_daysDF = pd.DataFrame(generated_days)
print(generated_daysDF)

i = 0
mondaystack = generated_daysDF.loc[generated_daysDF['outputDay'] == 'Monday', :]
mondaystack = pd.DataFrame(mondaystack)
print('mon : ',mondaystack.__len__())
tuesdaystack = generated_daysDF.loc[generated_daysDF['outputDay'] == 'Tuesday', :]
tuesdaystack = pd.DataFrame(tuesdaystack)
print('tue : ',tuesdaystack.__len__())
wednsdaystack = generated_daysDF.loc[generated_daysDF['outputDay'] == 'Wednesday', :]
wednsdaystack = pd.DataFrame(wednsdaystack)
print('wed : ',wednsdaystack.__len__())
thursdaystack = generated_daysDF.loc[generated_daysDF['outputDay'] == 'Thursday', :]
thursdaystack = pd.DataFrame(thursdaystack)
print('Thur : ',thursdaystack.__len__())
fridaystack = generated_daysDF.loc[generated_daysDF['outputDay'] == 'Friday', :]
fridaystack = pd.DataFrame(fridaystack)
print('Fri : ',fridaystack.__len__())

moncount = 0
tuecount = 0
wedcount = 0
thurcount = 0
fricount = 0

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

    m8date = ''
    m12date = ''
    m15date = ''
    t8date = ''
    t12date = ''
    t15date = ''
    w8date = ''
    w12date = ''
    w15date = ''
    th8date = ''
    th12date = ''
    th15date = ''
    f8date = ''
    f12date = ''
    f15date = ''

    while (y != 5):
        if( y == 0 and moncount < 11):
            day2 = mondaystack.iloc[moncount]['days'] + '/' + mondaystack.iloc[moncount]['month'] + '/' + mondaystack.iloc[moncount]['year']
            moncount = moncount + 1
        elif( y == 1 and tuecount < 11):
            day2 = tuesdaystack.iloc[tuecount]['days'] + '/' + tuesdaystack.iloc[tuecount]['month'] + '/' + tuesdaystack.iloc[tuecount]['year']
            tuecount = tuecount + 1
        elif( y == 2 and wedcount < 10):
            day2 = wednsdaystack.iloc[wedcount]['days'] + '/' + wednsdaystack.iloc[wedcount]['month'] + '/' + wednsdaystack.iloc[wedcount]['year']
            wedcount = wedcount + 1
        elif( y == 3 and thurcount < 10):
            day2 = thursdaystack.iloc[thurcount]['days'] + '/' + thursdaystack.iloc[thurcount]['month'] + '/' + thursdaystack.iloc[thurcount]['year']
            thurcount = thurcount + 1
        elif( y == 4 and fricount < 10):
            day2 = fridaystack.iloc[fricount]['days'] + '/' + fridaystack.iloc[fricount]['month'] + '/' + fridaystack.iloc[fricount]['year']
            fricount = fricount + 1

        dtrim = dconcat.loc[dconcat['dateonly'] == day2, :]
        day = str(generated_daysDF.iloc[i]['days'])+' '+str(generated_daysDF.iloc[i]['outputMonth'])
        print(day)

        for x in range(dtrim.__len__()):
            startTime = dtrim.iloc[x]['ScheduledStartTime']
            dconcat_iloc = dtrim.iloc[x]

            if (y == 0):
                m8date = str(mondaystack.iloc[moncount-1]['outputDay']) + ','
                m12date = str(mondaystack.iloc[moncount-1]['days']) + ' ' + str(mondaystack.iloc[moncount-1]['outputMonth'])
                m15date = str(mondaystack.iloc[moncount-1]['year'])
            elif (y == 1):
                t8date = str(tuesdaystack.iloc[tuecount-1]['outputDay'])
                t12date = str(tuesdaystack.iloc[tuecount-1]['days']) + ' ' + str(tuesdaystack.iloc[tuecount-1]['outputMonth'])
                t15date = str(tuesdaystack.iloc[tuecount-1]['year'])
            elif (y == 2):
                w8date = str(wednsdaystack.iloc[wedcount-1]['outputDay'])
                w12date = str(wednsdaystack.iloc[wedcount-1]['days']) + ' ' + str(wednsdaystack.iloc[wedcount-1]['outputMonth'])
                w15date = str(wednsdaystack.iloc[wedcount-1]['year'])
            elif (y == 3):
                th8date = str(thursdaystack.iloc[thurcount-1]['outputDay'])
                th12date = str(thursdaystack.iloc[thurcount-1]['days']) + ' ' + str(thursdaystack.iloc[thurcount-1]['outputMonth'])
                th15date = str(thursdaystack.iloc[thurcount-1]['year'])
            elif (y == 4):
                f8date = str(fridaystack.iloc[fricount-1]['outputDay'])
                f12date = str(fridaystack.iloc[fricount-1]['days']) + ' ' + str(fridaystack.iloc[fricount-1]['outputMonth'])
                f15date = str(fridaystack.iloc[fricount-1]['year'])

            if (startTime == '8:30:00' and dconcat_iloc['ScheduledDays'] == 'Monday' and m8visit == False and y == 0):
                m8 = dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                m8visit = True
            print(m8)

            if (startTime == '12:00:00' and dconcat_iloc['ScheduledDays'] == 'Monday' and m12visit == False and y == 0):
                m12 = dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                m12visit = True
            print(m12)

            if (startTime == '15:30:00' and dconcat_iloc['ScheduledDays'] == 'Monday' and m15visit == False and y == 0):
                m15 = dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                m15visit = True
            print(m15)

            if (startTime == '8:30:00' and dconcat_iloc['ScheduledDays'] == 'Tuesday' and t8visit == False and y == 1):
                t8 = dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                t8visit = True
            print(t8)

            if (startTime == '12:00:00' and dconcat_iloc['ScheduledDays'] == 'Tuesday' and t12visit == False and y == 1):
                t12 = dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                t12visit = True
            print(t12)

            if (startTime == '15:30:00' and dconcat_iloc['ScheduledDays'] == 'Tuesday' and t15visit == False and y == 1):
                t15 = dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                t15visit = True
            print(t15)

            if (startTime == '8:30:00' and dconcat_iloc['ScheduledDays'] == 'Wednesday' and w8visit == False and y == 2):
                w8 = dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                w8visit = True
            print(w8)

            if (startTime == '12:00:00' and dconcat_iloc['ScheduledDays'] == 'Wednesday' and w12visit == False and y == 2):
                w12 = dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                w12visit = True
            print(w12)

            if (startTime == '15:30:00' and dconcat_iloc['ScheduledDays'] == 'Wednesday' and w15visit == False and y == 2):
                w15 = dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                w15visit = True
            print(w15)

            if (startTime == '8:30:00' and dconcat_iloc['ScheduledDays'] == 'Thursday' and th8visit == False and y == 3):
                th8 = dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                th8visit = True
            print(th8)

            if (startTime == '12:00:00' and dconcat_iloc['ScheduledDays'] == 'Thursday' and th12visit == False and y == 3):
                th12 = dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                th12visit = True
            print(th12)

            if (startTime == '15:30:00' and dconcat_iloc['ScheduledDays'] == 'Thursday' and th15visit == False and y == 3):
                th15 = dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                th15visit = True
            print(th15)

            if (startTime == '8:30:00' and dconcat_iloc['ScheduledDays'] == 'Friday' and f8visit == False and y == 4):
                f8 = dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                f8visit = True
            print(f8)

            if (startTime == '12:00:00' and dconcat_iloc['ScheduledDays'] == 'Friday' and f12visit == False and y == 4):
                f12 = dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                f12visit = True
            print(f12)

            if (startTime == '15:30:00' and dconcat_iloc['ScheduledDays'] == 'Friday' and f15visit == False and y == 4):
                f15 = dconcat_iloc['Name'] + '\n(' + startTime + '-' + str(dconcat_iloc['ScheduledEndTime']) + ')\n' + str(dconcat_iloc['AllocatedLocationName'])
                f15visit = True
            print(f15)
            count = count + 1

        y = y + 1
        i = i + 1

    i = i + 1 #to skip sat & sun

    row_one = pd.Series(data={'Mon (8.30-11.30am)': m8date, 'Mon (12.00-3.00pm)': m12date, 'Mon (3.30-6.30pm)': m15date, 'Tue (8.30-11.30am)': t8date,'Tue (12.00-3.00pm)': t12date, 'Tue (3.30-6.30apm)': t15date, 'Wed (8.30-11.30am)': w8date, 'Wed (12.00-3.00pm)': w12date,'Wed (3.30-6.30pm)': w15date, 'Thur (8.30-11.30am)': th8date, 'Thur (12.00-3.00pm)': th12date,'Thur (3.30-6.30pm)': th15date, 'Fri (8.30-11.30am)': f8date, 'Fri (12.00-3.00pm)': f12date,'Fri (3.30-6.30pm)': f15date})
    row_two = pd.Series(data={'Mon (8.30-11.30am)': m8, 'Mon (12.00-3.00pm)': m12, 'Mon (3.30-6.30pm)': m15, 'Tue (8.30-11.30am)': t8,'Tue (12.00-3.00pm)': t12, 'Tue (3.30-6.30apm)': t15, 'Wed (8.30-11.30am)': w8, 'Wed (12.00-3.00pm)': w12,'Wed (3.30-6.30pm)': w15, 'Thur (8.30-11.30am)': th8, 'Thur (12.00-3.00pm)': th12,'Thur (3.30-6.30pm)': th15, 'Fri (8.30-11.30am)': f8, 'Fri (12.00-3.00pm)': f12,'Fri (3.30-6.30pm)': f15})
    #new_row = pd.Series(data={temprow})
    df_data = df_data.append(row_one, ignore_index=True)
    df_data = df_data.append(row_two, ignore_index=True)
   
    print('-------------------------------------------------------')



print(df_data)
df_data.to_csv("output/TimeTable.csv")

pdf = canvas.Canvas("output/TimeTable.pdf")
pdf.setTitle("TimeTable")
pdf.save()
