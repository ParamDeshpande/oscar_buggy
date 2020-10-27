import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import doctest
doctest.testmod()
data = np.genfromtxt("logAngles.txt", delimiter=",", names=["date&time","raw_yaw" ,"filter_yaw","smooth_yaw" , "raw_pitch","filter_pitch","smooth_pitch" ])
BUFFERSIZE = 15
dataBuffer = [0]*BUFFERSIZE
print(type(data)) 

root= tk.Tk() 
  
figure1 = plt.Figure(figsize=(5,4), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax1.plot(data['raw_yaw'])
ax1.set_xlabel("Time(in Seconds)")
ax1.set_ylabel("Changes in Angles(in Degree)")
ax1.legend("Raw Data")
ax1.set_title('Raw Data')

figure2 = plt.Figure(figsize=(5,4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax2.plot(data['filter_pitch'],color='red')
ax2.set_xlabel("Time(in Seconds)")
ax2.set_ylabel("Changes in Angles(in Degree)")
ax2.legend("Filtered Data")
ax2.set_title('Mad Filter Output')

figure3 = plt.Figure(figsize=(5,4), dpi=100)
ax3 = figure3.add_subplot(111)
scatter3 = FigureCanvasTkAgg(figure3, root) 
scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax3.plot(data['smooth_pitch'],color='orange')
ax3.set_xlabel("Time(in Seconds)")
ax3.set_ylabel("Changes in Angles(in Degree)")
ax3.legend("Spline Curve")
ax3.set_title('Spline Curve')

root.mainloop()
