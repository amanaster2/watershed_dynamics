#Import necessary modules
import numpy as np
from numpy.random import rand, randint
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

#Create random arrays for generic example
arr_1 = rand(1826) #random array of floats between 0 and 1 with len=1826
arr_2 = randint(0, 10, 1826) #random array of integers between 0 and 10 with len=1826

#Create dictionary for ease of bringing into pandas dataframe
d = {'Val_1': arr_1, 'Val_2': arr_2}

#Create pandas dataframe
df = pd.DataFrame(data=d)

#Reset the index of the dataframe to be dates
day0 = datetime(2018, 10, 1)
df.set_index(pd.DatetimeIndex([day0+timedelta(days=np.float(time)) for time in np.arange(0, 1826)]), inplace=True)

#Create ticklabels using list comprehension
ticklabels = [item.strftime('%Y') for item in df.index[::366]]

#Create figure of size (13, 5)
fig, ax = plt.subplots(figsize=(13,5))

#Plot first variable
df.plot(y='Val_1', ax=ax, color = '#8a0c80', legend=False, label='Variable 1', kind='bar')
ax.set_xlabel('Date', fontsize=14, fontweight='bold') #note: only need to set xlabel once
ax.set_ylabel('Variable 1', fontsize=14, fontweight='bold')
ax.set_ylim(0,5)
ax.grid(False)

#Create another y-axis with the same x-axis
ax1 = ax.twinx()

#Plot second variable
df.plot(y='Val_2', ax=ax1, color='#0c3c8a', legend=False, label='Variable 2', kind='bar')
ax1.set_ylabel('Variable 2', fontsize=14, fontweight='bold')
ax1.set_ylim(0, 15)
ax1.invert_yaxis() #makes the second y-axis inverted
ax1.grid(False)


fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax.transAxes) #add legend
ax.set_xticks(np.arange(0,366*len(ticklabels),366)) #set xtick locations
ax.set_xticklabels(ticklabels, rotation=45) #set xtick labels
plt.tight_layout() #fixes any weird white space problems
plt.show()