import csv
import os
import numpy as np
import random
import pandas as pd

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
plt.rcParams['font.size'] = 12  # 字体大小
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

csv_data = pd.read_csv('Result/Result1_highway_rl_inlane3.csv')

runtime_group = []

detected_percentage_group0 = []
idclear_percentage_group0 = []
blocked_percentage_group0 = []
average_speed_group0 = []
headway_spacing_group0 = []
headway_group0 = []

detected_percentage_group1 = []
idclear_percentage_group1 = []
blocked_percentage_group1 = []
average_speed_group1 = []
headway_spacing_group1 = []
headway_group1 = []

detected_percentage_group2 = []
idclear_percentage_group2 = []
blocked_percentage_group2 = []
average_speed_group2 = []
headway_spacing_group2 = []
headway_group2 = []

detected_percentage_group3 = []
idclear_percentage_group3 = []
blocked_percentage_group3 = []
average_speed_group3 = []
headway_spacing_group3 = []
headway_group3 = []

new_data0 = csv_data[csv_data.lane_num.isin([0])]
new_data_group0 = new_data0.values
for find_num in range(0,new_data_group0.shape[0]):
	runtime_group.append(float(new_data_group0[find_num][1]))
	
	detected_percentage_group0.append(float(new_data_group0[find_num][2]))
	idclear_percentage_group0.append(float(new_data_group0[find_num][3]))
	blocked_percentage_group0.append(float(new_data_group0[find_num][4]))
	average_speed_group0.append(float(new_data_group0[find_num][5]))
	headway_spacing_group0.append(float(new_data_group0[find_num][6]))
	headway_group0.append(float(new_data_group0[find_num][7]))

new_data1 = csv_data[csv_data.lane_num.isin([1])]
new_data_group1 = new_data1.values
for find_num in range(0,new_data_group1.shape[0]):	
	detected_percentage_group1.append(float(new_data_group1[find_num][2]))
	idclear_percentage_group1.append(float(new_data_group1[find_num][3]))
	blocked_percentage_group1.append(float(new_data_group1[find_num][4]))
	average_speed_group1.append(float(new_data_group1[find_num][5]))
	headway_spacing_group1.append(float(new_data_group1[find_num][6]))
	headway_group1.append(float(new_data_group1[find_num][7]))

new_data2 = csv_data[csv_data.lane_num.isin([2])]
new_data_group2 = new_data2.values
for find_num in range(0,new_data_group2.shape[0]):	
	detected_percentage_group2.append(float(new_data_group2[find_num][2]))
	idclear_percentage_group2.append(float(new_data_group2[find_num][3]))
	blocked_percentage_group2.append(float(new_data_group2[find_num][4]))
	average_speed_group2.append(float(new_data_group2[find_num][5]))
	headway_spacing_group2.append(float(new_data_group2[find_num][6]))
	headway_group2.append(float(new_data_group2[find_num][7]))

new_data3 = csv_data[csv_data.lane_num.isin([3])]
new_data_group3 = new_data3.values
for find_num in range(0,new_data_group3.shape[0]):	
	detected_percentage_group3.append(float(new_data_group3[find_num][2]))
	idclear_percentage_group3.append(float(new_data_group3[find_num][3]))
	blocked_percentage_group3.append(float(new_data_group3[find_num][4]))
	average_speed_group3.append(float(new_data_group3[find_num][5]))
	headway_spacing_group3.append(float(new_data_group3[find_num][6]))
	headway_group3.append(float(new_data_group3[find_num][7]))

ax1 = plt.subplot(231)
plt.plot(runtime_group,detected_percentage_group0, color='r', label='L0', linewidth=1)
plt.plot(runtime_group,detected_percentage_group1, color='g', label='L1', linewidth=1)
plt.plot(runtime_group,detected_percentage_group2, color='b', label='L2', linewidth=1)
plt.plot(runtime_group,detected_percentage_group3, color='k', label='L3', linewidth=1)
plt.title("被ICV检测到的车辆的比例")
plt.xlabel('运行时间（s）')
plt.ylabel('被ICV检测到的车辆的比例')

ax2 = plt.subplot(232)
plt.plot(runtime_group,idclear_percentage_group0, color='r', label='flow_in_L0', linewidth=1)
plt.plot(runtime_group,idclear_percentage_group1, color='g', label='flow_in_L1', linewidth=1)
plt.plot(runtime_group,idclear_percentage_group2, color='b', label='flow_in_L2', linewidth=1)
plt.plot(runtime_group,idclear_percentage_group3, color='k', label='flow_in_L3', linewidth=1)
plt.title("被ICV检测到的身份信息确定车辆的比例")
plt.xlabel('运行时间（s）')
plt.ylabel('被ICV检测到的身份信息确定车辆的比例')

ax3 = plt.subplot(233)
plt.plot(runtime_group,blocked_percentage_group0, color='r', label='L0', linewidth=1)
plt.plot(runtime_group,blocked_percentage_group1, color='g', label='L1', linewidth=1)
plt.plot(runtime_group,blocked_percentage_group2, color='b', label='L2', linewidth=1)
plt.plot(runtime_group,blocked_percentage_group3, color='k', label='L3', linewidth=1)
plt.title("ICV完全检测不到的车辆的比例")
plt.xlabel('运行时间（s）')
plt.ylabel('ICV完全检测不到的车辆的比例')

#box = ax1.get_position()
#ax1.set_position([box.x0, box.y0, box.width , box.height* 0.8])
#ax1.set_position([box.x0, box.y0, box.width , box.height* 0.8])
ax2.legend(loc='center left', bbox_to_anchor=(-0.67, 1.25),ncol=4)

ax4 = plt.subplot(234)
plt.plot(runtime_group,average_speed_group0, color='r', label='L0', linewidth=1)
plt.plot(runtime_group,average_speed_group1, color='g', label='L1', linewidth=1)
plt.plot(runtime_group,average_speed_group2, color='b', label='L2', linewidth=1)
plt.plot(runtime_group,average_speed_group3, color='k', label='L3', linewidth=1)
plt.title("被检测到的车辆的平均车速")
plt.xlabel('运行时间（s）')
plt.ylabel('被检测到的车辆的平均车速（m/s）')

ax5 = plt.subplot(235)
plt.plot(runtime_group,headway_spacing_group0, color='r', label='L0', linewidth=1)
plt.plot(runtime_group,headway_spacing_group1, color='g', label='L1', linewidth=1)
plt.plot(runtime_group,headway_spacing_group2, color='b', label='L2', linewidth=1)
plt.plot(runtime_group,headway_spacing_group3, color='k', label='L3', linewidth=1)
plt.title("被检测到的车辆的平均车头间距")
plt.xlabel('运行时间（s）')
plt.ylabel('被检测到的车辆的平均车头间距（m）')

ax6 = plt.subplot(236)
plt.plot(runtime_group,headway_group0, color='r', label='L0', linewidth=1)
plt.plot(runtime_group,headway_group1, color='g', label='L1', linewidth=1)
plt.plot(runtime_group,headway_group2, color='b', label='L2', linewidth=1)
plt.plot(runtime_group,headway_group3, color='k', label='L3', linewidth=1)
plt.title("被检测到的车辆的平均车头时距")
plt.xlabel('运行时间（s）')
plt.ylabel('被检测到的车辆的平均车头时距（s）')

plt.subplots_adjust(wspace=0.3, hspace=0.4) # wspace=0.2, 
plt.show()
