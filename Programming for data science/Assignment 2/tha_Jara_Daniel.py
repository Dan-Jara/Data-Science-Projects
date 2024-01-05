import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Hospital = pd.read_csv("data/CaliforniaHospitalData.csv")
Hospital = pd.DataFrame(Hospital)
Personnel = pd.read_table("data/CaliforniaHospitalData_Personnel.txt")
Personnel = pd.DataFrame(Personnel)
data = pd.concat([Hospital, Personnel], axis = 1)
data.head()

data = data.drop(['Work_ID', 'PositionID', 'Website'], axis = 1)
data.head()

hospital_data_new=data[(data["Teaching"]=="Small/Rural")&(data["AvlBeds"]>=15)&(data["OperInc"]>=0)]
hospital_data_new
hospital_data_new.to_csv(r'data/hospital_data_new.txt', header = True, sep ='\t')

new_data = pd.read_table('data/hospital_data_new.txt')
new_data = pd.DataFrame(new_data)
new_data = new_data.rename(columns = {'NoFTE':'FullTimeCount','NetPatRev': 'NetPatientRevenue',
'InOperExp':'InpatientOperExp','OutOperExp':'OutpatientOperExp', 'OperRev': 'Operating_Revenue',
'OperInc': 'Operating_Income'})
new_data.head()
new_data = new_data.drop(['Unnamed: 0'], axis = 1)

new_data.columns

new_rows = [{'HospitalID':'17741.0','Name':'St. Elizabeth Community Hospital',
'Zip':'96080','TypeControl':'Non Profit',
'Teaching':'Small/Rural','DonorType':'Charity',
'FullTimeCount':397.5,'NetPatientRevenue':232503.0191,
'InpatientOperExp':3.668289e+07, 'OutpatientOperExp':34916220.47,
'Operating_Revenue':47629675.18,'Operating_Income':49825763.57,
'AvlBeds':10,'HospitalID.1':'-','LastName':'Jara','FirstName':'Daniel',
'Gender':'M','PositionTitle':'State Board Representative',
'Compensation':89473,'MaxTerm':3,'StartDate':'9/12/2022','Phone':'405-762-5831',
'Email':'djaraco@okstate.edu'},
{'HospitalID':'46996.0','Name':'Ridgecrest Regional Hospital',
'Zip':'93555','TypeControl':'Non Profit',
'Teaching':'Small/Rural','DonorType':'Charity','FullTimeCount':400.0,
'NetPatientRevenue':139170.3798,'InpatientOperExp':2.338557e+07,
'OutpatientOperExp':34916220.47,'Operating_Revenue':53425429.78,
'Operating_Income':53467864.60,'AvlBeds':13,'HospitalID.1':'-',
'LastName':'Jara','FirstName':'Daniel','Gender':'M',
'PositionTitle':'Regional Representative',
'Compensation':46978,'MaxTerm':4,'StartDate':'9/12/2022',
'Phone':'405-762-5831','Email':'djaraco@okstate.edu'}]

new_merge = new_data.append(new_rows,ignore_index = True)
new_merge.tail()

new_merge['StartDate'] = pd.to_datetime(new_merge['StartDate'])
new_merge.dtypes

new_dataframe = new_merge[(new_merge['TypeControl']=='Non Profit')&
(new_merge['FullTimeCount']>250.0)&
(new_merge['NetPatientRevenue']>=109000)]
new_dataframe = new_dataframe[0:12]
new_dataframe.to_csv(r'data/new_dataframe.txt', header = True, sep ='\t')

filtered_personnel = new_merge[(new_merge['PositionTitle']=='Regional Representative')&
(new_merge['Operating_Income']>100000)]
filtered_personnel = filtered_personnel[14:23]
filtered_personnel.to_csv(r'data/filtered_personnel.txt', header = True, sep = '\t')