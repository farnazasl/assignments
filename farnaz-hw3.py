# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import os
import numpy as np
import sys

# <codecell>

file='fluxes_13.7500_-0.2500'
temp = cwd , file
current_file='/'.join(temp)
data=np.loadtxt(current_file)
sum=np.zeros(12)
counter=np.zeros(12)
for i in range(0,data.shape[0]):
    sum[data[i,1]-1]+=data[i,3]
    counter[data[i,1]-1]+=1.0
mean=np.zeros(12)
for j in range(0,12):
    mean[j]=sum[j]/counter[j]
lat = file.split("_")[1]
lon = file.split("_")[2]
temp= 'monthly','precipitation',lat,lon
temp1='_'.join(temp)
temp2= cwd,temp1
output_file_path='/'.join(temp2)
print data[1,1]
f=open(output_file_path, 'w')
for i in range(0,12):
   f.write("%2d  %6f  \n" % (i+1,mean[i]))
f.close()
print data.shape[1]

# <codecell>

os.chdir('/net/jet/home/farnaz')
os.chdir('/net/jet/home/farnaz/fluxes')
cwd=os.getcwd()
for file in os.listdir(cwd):
    temp = cwd , file
    current_file='/'.join(temp)
    data=np.loadtxt(current_file)
    sum=np.zeros(12)
    counter=np.zeros(12)
    for i in range(0,data.shape[0]):
        sum[data[i,1]-1]+=data[i,3]
        counter[data[i,1]-1]+=1.0
    mean=np.zeros(12)
    for j in range(0,12):
        mean[j]=sum[j]/counter[j]
    lat = file.split("_")[1]
    lon = file.split("_")[2]
    temp= 'monthly','precipitation',lat,lon
    temp1='_'.join(temp)
    temp2= cwd,temp1
    output_file_path='/'.join(temp2)
    f=open(output_file_path, 'w')
    for i in range(0,12):
        f.write("%2d  %6f  \n" % (i+1,mean[i]))
    f.close()

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


