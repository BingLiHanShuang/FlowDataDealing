import csv
import os
import numpy as np
import random
import pandas as pd

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
plt.rcParams['font.size'] = 12  # 字体大小
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

csv_data = pd.read_csv('Result/Result2_highway_rl_inlane0.csv')
csv_data2 = pd.read_csv('Result/Result2_highway_rl_inlane1.csv')
csv_data3 = pd.read_csv('Result/Result2_highway_rl_inlane2.csv')
csv_data4 = pd.read_csv('Result/Result2_highway_rl_inlane3.csv')

runtime_group0 = []
runtime_group1 = []
runtime_group2 = []
runtime_group3 = []

detected_percentage_group0 = []
idclear_percentage_group0 = []
blocked_percentage_group0 = []
average_speed_group0 = []
headway_spacing_group0 = []
headway_group0 = []
density_group0 = []
magnitude_group0 = []

detected_percentage_group1 = []
idclear_percentage_group1 = []
blocked_percentage_group1 = []
average_speed_group1 = []
headway_spacing_group1 = []
headway_group1 = []
density_group1 = []
magnitude_group1 = []

detected_percentage_group2 = []
idclear_percentage_group2 = []
blocked_percentage_group2 = []
average_speed_group2 = []
headway_spacing_group2 = []
headway_group2 = []
density_group2 = []
magnitude_group2 = []

detected_percentage_group3 = []
idclear_percentage_group3 = []
blocked_percentage_group3 = []
average_speed_group3 = []
headway_spacing_group3 = []
headway_group3 = []
density_group3 = []
magnitude_group3 = []

new_data_group0 = csv_data.values
for find_num in range(0,new_data_group0.shape[0]):
	runtime_group0.append(float(new_data_group0[find_num][0]))
	
	detected_percentage_group0.append(float(new_data_group0[find_num][1]))
	idclear_percentage_group0.append(float(new_data_group0[find_num][2]))
	blocked_percentage_group0.append(float(new_data_group0[find_num][3]))
	average_speed_group0.append(float(new_data_group0[find_num][4]))
	headway_spacing_group0.append(float(new_data_group0[find_num][6]))
	headway_group0.append(float(new_data_group0[find_num][7]))
	density_group0.append(float(new_data_group0[find_num][8]))
	magnitude_group0.append(float(new_data_group0[find_num][9]))

new_data_group1 = csv_data2.values
for find_num in range(0,new_data_group1.shape[0]):
	runtime_group1.append(float(new_data_group1[find_num][0]))
	detected_percentage_group1.append(float(new_data_group1[find_num][1]))
	idclear_percentage_group1.append(float(new_data_group1[find_num][2]))
	blocked_percentage_group1.append(float(new_data_group1[find_num][3]))
	average_speed_group1.append(float(new_data_group1[find_num][4]))
	headway_spacing_group1.append(float(new_data_group1[find_num][6]))
	headway_group1.append(float(new_data_group1[find_num][7]))
	density_group1.append(float(new_data_group1[find_num][8]))
	magnitude_group1.append(float(new_data_group1[find_num][9]))

new_data_group2 = csv_data3.values
for find_num in range(0,new_data_group2.shape[0]):
	runtime_group2.append(float(new_data_group2[find_num][0]))
	detected_percentage_group2.append(float(new_data_group2[find_num][1]))
	idclear_percentage_group2.append(float(new_data_group2[find_num][2]))
	blocked_percentage_group2.append(float(new_data_group2[find_num][3]))
	average_speed_group2.append(float(new_data_group2[find_num][4]))
	headway_spacing_group2.append(float(new_data_group2[find_num][6]))
	headway_group2.append(float(new_data_group2[find_num][7]))
	density_group2.append(float(new_data_group2[find_num][8]))
	magnitude_group2.append(float(new_data_group2[find_num][9]))

new_data_group3 = csv_data4.values
for find_num in range(0,new_data_group3.shape[0]):
	runtime_group3.append(float(new_data_group3[find_num][0]))
	detected_percentage_group3.append(float(new_data_group3[find_num][1]))
	idclear_percentage_group3.append(float(new_data_group3[find_num][2]))
	blocked_percentage_group3.append(float(new_data_group3[find_num][3]))
	average_speed_group3.append(float(new_data_group3[find_num][4]))
	headway_spacing_group3.append(float(new_data_group3[find_num][6]))
	headway_group3.append(float(new_data_group3[find_num][7]))
	density_group3.append(float(new_data_group3[find_num][8]))
	magnitude_group3.append(float(new_data_group3[find_num][9]))

fig1 = plt.figure(1)
ax1 = plt.subplot(311)
plt.plot(runtime_group0,detected_percentage_group0, color='r', label='L0', linewidth=1)
plt.plot(runtime_group1,detected_percentage_group1, color='g', label='L1', linewidth=1)
plt.plot(runtime_group2,detected_percentage_group2, color='b', label='L2', linewidth=1)
plt.plot(runtime_group3,detected_percentage_group3, color='k', label='L3', linewidth=1)
plt.title("被ICV检测到的车辆的比例")
plt.xlabel('运行时间（s）')
plt.ylabel('比例')

ax2 = plt.subplot(312)
plt.plot(runtime_group0,idclear_percentage_group0, color='r', label='ICV_in_L0', linewidth=1)
plt.plot(runtime_group1,idclear_percentage_group1, color='g', label='ICV_in_L1', linewidth=1)
plt.plot(runtime_group2,idclear_percentage_group2, color='b', label='ICV_in_L2', linewidth=1)
plt.plot(runtime_group3,idclear_percentage_group3, color='k', label='ICV_in_L3', linewidth=1)
plt.title("被ICV检测到的身份信息确定车辆的比例")
plt.xlabel('运行时间（s）')
plt.ylabel('比例')

ax3 = plt.subplot(313)
plt.plot(runtime_group0,blocked_percentage_group0, color='r', label='L0', linewidth=1)
plt.plot(runtime_group1,blocked_percentage_group1, color='g', label='L1', linewidth=1)
plt.plot(runtime_group2,blocked_percentage_group2, color='b', label='L2', linewidth=1)
plt.plot(runtime_group3,blocked_percentage_group3, color='k', label='L3', linewidth=1)
plt.title("ICV完全检测不到的车辆的比例")
plt.xlabel('运行时间（s）')
plt.ylabel('比例')

#box = ax1.get_position()
#ax1.set_position([box.x0, box.y0, box.width , box.height* 0.8])
#ax1.set_position([box.x0, box.y0, box.width , box.height* 0.8])
ax1.legend(loc='right', bbox_to_anchor=(0.665, 1.4),ncol=4)
plt.subplots_adjust(hspace=0.6) # wspace=0.2, 

fig2 = plt.figure(2)
ax4 = plt.subplot(311)
plt.plot(runtime_group0,average_speed_group0, color='r', label='L0', linewidth=1)
plt.plot(runtime_group1,average_speed_group1, color='g', label='L1', linewidth=1)
plt.plot(runtime_group2,average_speed_group2, color='b', label='L2', linewidth=1)
plt.plot(runtime_group3,average_speed_group3, color='k', label='L3', linewidth=1)
plt.title("被检测到的车辆的平均车速")
plt.xlabel('运行时间（s）')
plt.ylabel('平均车速（m/s）')

ax6 = plt.subplot(312)
plt.plot(runtime_group0,headway_group0, color='r', label='L0', linewidth=1)
plt.plot(runtime_group1,headway_group1, color='g', label='L1', linewidth=1)
plt.plot(runtime_group2,headway_group2, color='b', label='L2', linewidth=1)
plt.plot(runtime_group3,headway_group3, color='k', label='L3', linewidth=1)
plt.title("被检测到的车辆的平均车头时距")
plt.xlabel('运行时间（s）')
plt.ylabel('平均车头时距（s）')

ax5 = plt.subplot(313)
plt.plot(runtime_group0,headway_spacing_group0, color='r', label='L0', linewidth=1)
plt.plot(runtime_group1,headway_spacing_group1, color='g', label='L1', linewidth=1)
plt.plot(runtime_group2,headway_spacing_group2, color='b', label='L2', linewidth=1)
plt.plot(runtime_group3,headway_spacing_group3, color='k', label='L3', linewidth=1)
plt.title("被检测到的车辆的平均车头间距")
plt.xlabel('运行时间（s）')
plt.ylabel('平均车头间距（m）')
ax4.legend(loc='right', bbox_to_anchor=(0.665, 1.3),ncol=4)
plt.subplots_adjust(hspace=0.5) # wspace=0.2, 

fig3 = plt.figure(3)
ax7 = plt.subplot(211)
plt.plot(runtime_group0,density_group0, color='r', label='L0', linewidth=1)
plt.plot(runtime_group1,density_group1, color='g', label='L1', linewidth=1)
plt.plot(runtime_group2,density_group2, color='b', label='L2', linewidth=1)
plt.plot(runtime_group3,density_group3, color='k', label='L3', linewidth=1)
plt.title("交通流量密度")
plt.xlabel('运行时间（s）')
plt.ylabel('交通流量密度（米/标准车）')

ax8 = plt.subplot(212)
plt.plot(runtime_group0,magnitude_group0, color='r', label='L0', linewidth=1)
plt.plot(runtime_group1,magnitude_group1, color='g', label='L1', linewidth=1)
plt.plot(runtime_group2,magnitude_group2, color='b', label='L2', linewidth=1)
plt.plot(runtime_group3,magnitude_group3, color='k', label='L3', linewidth=1)
plt.title("交通流量")
plt.xlabel('运行时间（s）')
plt.ylabel('交通流量（标准车/小时）')
ax7.legend(loc='right', bbox_to_anchor=(0.665, 1.2),ncol=4)

plt.subplots_adjust(hspace=0.3) # wspace=0.2, 
plt.show()
