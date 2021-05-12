# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#========================================================
#Code starts here
census = np.concatenate((data,new_record),axis=0)
# print(census)
# print(data.shape,census.shape)
#========================================================
maxInage = np.amax(census, axis=0)
minInage = np.amin(census, axis=0)
max_age = maxInage[0]
min_age = minInage[0]
agee_mean = np.mean(census, axis=0)
age_mean = round(agee_mean[0],2)
stdd = np.std(census,axis = 0)
age_std = round(stdd[0],2)
# print(max_age,min_age,age_mean,age_std)
#========================================================
races = np.array(census[:,2])
l0,l1,l2,l3,l4 = [],[],[],[],[]
for i in range(len(races)):
    if races[i]==0:
        l0.append(census[i,:])
    elif races[i]==1:
        l1.append(census[i,:])
    elif races[i]==2:
        l2.append(census[i,:])
    elif races[i]==3:
        l3.append(census[i,:])
    else:
        l4.append(census[i,:]) 

# print(len(l0),len(l1),len(l2),len(l3),len(l4))
race_0 = np.array(l0)
race_1 = np.array(l1) 
race_2 = np.array(l2)
race_3 = np.array(l3)
race_4 = np.array(l4)
len_0 =  len(l0)
len_1 =  len(l1)
len_2 = len(l2)
len_3 = len(l3)
len_4 = len(l4)
lengths = np.array([len(l0),len(l1),len(l2),len(l3),len(l4)])
# print(lengths)
minority_race = np.amin(lengths)
for i in range(5):
    if lengths[i] == minority_race:
        minority_race = i
        break
# print(minority_race)

# for i in range(len(races)):
#     if races[i] == 4:
#         # race_4.append(census[i])
#         np.concatenate((race_4,census[i]))
# print(race_4)        
#=======================================================================
senior_citizens = census[census[:,0]>60]
senior_citizens_len =  len(senior_citizens)
working_hours_sum = 0
for i in range(senior_citizens_len):
    working_hours_sum += senior_citizens[i,6]
# print(working_hours_sum)
avg_working_hours = working_hours_sum / senior_citizens_len
avg_working_hours = round(avg_working_hours,2)
print(avg_working_hours)
#=======================================================================
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])
print(round(avg_pay_high,2),round(avg_pay_low,2))


