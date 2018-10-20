import requests
import json
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://modis.ornl.gov/rst/api/v1/"
header = {'Accept': 'application/json'}

response = requests.get('https://modis.ornl.gov/rst/api/v1/MOD11A2/dates?latitude=6.4281&longitude=9.4295', headers=header)
dates = json.loads(response.text)['dates']

modis_dates = [i['modis_date'] for i in dates]
calendar_dates = [i['calendar_date'] for i in dates]

dates[0:10]
response = requests.get('https://modis.ornl.gov/rst/api/v1/MOD11A2/subset?latitude=6.4281&longitude=9.4295&band=LST_Day_1km&startDate=A2001001&endDate=A2001001&kmAboveBelow=1&kmLeftRight=1', headers=header)

subset = json.loads(response.text)
subset['subset']

lat = 6.4281
lon = 9.4295
prod = 'MOD11A2'
data_band = 'LST_Day_1Km'
qc_band = 'QC_Day'
above_below = 10
left_right = 10

dates = modis_dates[modis_dates.index('A2001001'):modis_dates.index('A2001001') + 137]

lstdata = []
qcdata = []

for dt in range(0,len(dates)):
    requestURL = url+prod+"/subset?latitude="+str(lat)+"&longitude="+str(lon)+"&band="+data_band+"&startDate="+dates[dt]+"&endDate="+dates[dt + 9]+"&kmAboveBelow="+str(above_below)+"&kmLeftRight="+str(left_right)
    response = requests.get(requestURL, headers=header)
    for tstep in json.loads(response.text)['subset']:
        lstdata.append(tstep['data'])

requestURL = url+prod+"/subset?latitude="+str(lat)+"&longitude="+str(lon)+"&band="+qc_band+"&startDate="+dates[dt + 10]+"&endDate="+dates[-1]+"&kmAboveBelow="+str(above_below)+"&kmLeftRight="+str(left_right)
response = requests.get(requestURL, headers=header)

for tstep in json.loads(response.text)['subset']:
    qcdata.append(tstep['data'])

requestURL = url+prod+"/subset?latitude="+str(lat)+"&longitude="+str(lon)+"&band="+data_band+"&startDate="+dates[dt + 10]+"&endDate="+dates[-1]+"&kmAboveBelow="+str(above_below)+"&kmLeftRight="+str(left_right)

response = requests.get(requestURL, headers=header)

for tstep in json.loads(response.txt)['subset']:
    lstdata.append(tstep['data'])

dates = [(datetime.datetime(int(date[1:5]), 1, 1) + datetime.timedelta(int(date[5:]))).strftime('%Y-%m-%d') for date in dates]

lstdata = pd.DataFrame(lstdata, index=dates)
qcdata = pd.DataFrame(qcdata, index=dates)

qcvals = pd.unique(qcdata.values.ravel())
qcvals

QC_Data = []

for integr in range(0, 256, 1):
    bits = list(map(int, list("{0:b}".format(integer).zfill(8))))

if (bits[6] == 0 and bits[7] == 0):
    Mandatory_QA = 'LST GOOD'
if (bits[6] == 0 and bits[7] == 1):
    Mandatory_QA = 'LST Produced,Other Quality'
if (bits[6] == 1 and bits[7] == 0):
    Mandatory_QA = 'No Pixel,clouds'
if (bits[6] == 1 and bits[7] == 1):
    Mandatory_QA = 'No Pixel, Other QA'

if (bits[4] == 0 and bits[5] == 0):
    Data_Quality = 'Good Data'
if (bits[4] == 0 and bits[5] == 1):
    Data_Quality = 'Other Quality'
if (bits[4] == 1 and bits[5] == 0):
    Data_Quality = 'TBD'
if (bits[4] == 1 and bits[5] == 1):
    Data_Quality = 'TBD'

if (bits[2] == 0 and bits[3] == 0):
    Emiss_Err = 'Emiss Err <= .01'
if (bits[2] == 0 and bits[3] == 1):
    Emiss_Err = 'Emiss Err <= .02'
if (bits[2] == 1 and bits[3] == 0):
    Emiss_Err = 'Emiss Err <= .04'
if (bits[2] == 1 and bits[3] == 1):
    Emiss_Err = 'Emiss Err > .04'

if (bits[0] == 0 and bits[1] == 0):
    LST_Err = 'LST Err <= 1K'
if (bits[0] == 0 and bits[1] == 1):
    LST_Err = 'LST Err <= 3K'
if (bits[0] == 1 and bits[1] == 0):
    LST_Err = 'LST Err <= 2K'
if (bits[0] == 1 and bits[1] == 1):
    LST_Err = 'LST Err > 3K'

QC_Data.append([integer] + bits + [Mandatory_QA, Data_Quality, Emiss_Err, LST_Err])
QC_Data = pd.DataFrame(QC_Data, columns=['Integer_Value', 'Bit7', 'Bit6', 'Bit5', 'Bit4', 'Bit3', 'Bit2', 'Bit1', 'Bit0', 'Mandatory_QA', 'Data_Quality', 'Emiss_Err', 'LST_Err'])
QC_Data

filter = QC_Data['Integer_Value'].tolist()
lstdata_filt = lstdata.mask(qcdata.isin(filter))

scale = json.loads(response.text)['scale']
lstdata_filt_scale = lstdata_filt*float(scale)

ncol = int(json.loads(response.text)['ncols'])
nrow = int(json.loads(response.text)['nrows'])


lststats = pd.DataFrame(np.column_stack([lstdata_filt_scale.mean(axis=1), 
                                         lstdata_filt_scale.std(axis=1), 
                                         lstdata_filt_scale.apply(lambda row: (float(row.count())/(ncol*nrow))*100, axis=1)]), 
                        columns=['mean', 'sd', 'quality'], index=dates)

# converting dataframe index to date time
lststats.index = pd.to_datetime(lststats.index)

lststats

plt.rcParams['figure.figsize'] = (15,8)

fig, ax1 = plt.subplots()

ax1.set_xlabel('Date')
ax1.set_ylabel('LST (K)')
ax1.plot(lststats.index, lststats['mean'], 'k-')
ax1.fill_between(lststats.index, lststats['mean']-lststats['sd'], lststats['mean']+lststats['sd'])
ax1.tick_params(axis='y')
fig.autofmt_xdate()

ax2 = ax1.twinx()
ax2.set_ylabel('% Good Pixels')
ax2.bar(lststats.index, lststats['quality'], 5, alpha = 0.5)
ax2.tick_params(axis='y')

plt.show()

