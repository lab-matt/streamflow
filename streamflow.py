import numpy as np
import matplotlib.pyplot as plt

array1 = np.genfromtxt('June-2021-Provo-River-Streamflow-Rates.csv',delimiter=',',dtype=str,skip_header=1)

x = array1[:,0]
y_1 = array1[:,1].astype(float)
y_2 = array1[:,2].astype(float)
y_3 = array1[:,3].astype(float)
y_4 = array1[:,4].astype(float)
y_5 = array1[:,5].astype(float)

plt.style.use('default')
plt.plot(x,y_1, color='purple', label ='10163000')
plt.plot(x,y_2, color='g', label ='10155200')
plt.plot(x,y_3, color='b', label ='10155500')
plt.plot(x,y_4, color='y', label ='10154200')
plt.plot(x,y_5, color='r', label ='10155000')

plt.title('Provo River Streamflow Data (2021)')
plt.legend(title='Site Numbers',loc='upper right')

plt.ylabel('Flowrate (cfs)')
plt.xlabel('Date')

# Shows x ticks every 384 entries
plt.xticks(x[::384], [date[:10] for date in x[::384]], rotation=45)
plt.tight_layout()
plt.grid(True)


plt.show()
