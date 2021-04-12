import matplotlib.pyplot as plt
import numpy as np
import csv
import os
import pandas as pd

def autolabel(rects):
	for rect in rects:
		height = rect.get_height()
		plt.text(rect.get_x()+rect.get_width()/2.0-0.045, 1.02*height, '%.2f' % height)

def autolabel_1(rects):
	for rect in rects:
		height = rect.get_height()
		plt.text(rect.get_x()+rect.get_width()/2.0-0.05, 1.02*height, '%.1f' % height, fontsize=12)

def autolabel_1_higher_left(rects):
	for rect in rects:
		height = rect.get_height()
		plt.text(rect.get_x()+rect.get_width()/2.0-0.053, 1.02*height, '%.1f' % height, fontsize=11)

def autolabel_1_higher(rects):
	for rect in rects:
		height = rect.get_height()
		plt.text(rect.get_x()+rect.get_width()/2.0-0.05, 1.12*height, '%.1f' % height, fontsize=11)

def autolabel_1_lower(rects):
	for rect in rects:
		height = rect.get_height()
		plt.text(rect.get_x()+rect.get_width()/2.0-0.05, 1.004*height, '%.1f' % height, fontsize=12)

def autolabel_1_left(rects):
	for rect in rects:
		height = rect.get_height()
		plt.text(rect.get_x()+rect.get_width()/2.0-0.055, 1.004*height, '%.1f' % height, fontsize=12)

csv_data = pd.read_csv('Check_result.csv')

plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
plt.rcParams['font.size'] = 12  # 字体大小
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

check_x = ('1500米', '3000米', '4500米')

# Time_headway ****************************************************************************************
# 全断面
fig1 = plt.figure(1)

value_norl = []
value_rl_inlane0 = []
value_rl_inlane1 = []
value_rl_inlane2 = []
value_rl_inlane3 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Time_headway_data = float(csv_data.at[collect_num,'Time_headway'])
	if Rl_lane_data == "none" and Check_ypos_data == "T":
		value_norl.append(Time_headway_data)
	if Rl_lane_data == "0" and Check_ypos_data == "T":
		value_rl_inlane0.append(Time_headway_data)
	if Rl_lane_data == "1" and Check_ypos_data == "T":
		value_rl_inlane1.append(Time_headway_data)
	if Rl_lane_data == "2" and Check_ypos_data == "T":
		value_rl_inlane2.append(Time_headway_data)
	if Rl_lane_data == "3" and Check_ypos_data == "T":
		value_rl_inlane3.append(Time_headway_data)

bar_width = 0.15
index_norl = np.arange(len(check_x))
index_rl_inlane0 = index_norl + bar_width
index_rl_inlane1 = index_rl_inlane0 + bar_width
index_rl_inlane2 = index_rl_inlane1 + bar_width
index_rl_inlane3 = index_rl_inlane2 + bar_width

norl = plt.bar(index_norl, height=value_norl, width=bar_width, color='r', label='无ICV')
rl_inlane0 = plt.bar(index_rl_inlane0, height=value_rl_inlane0, width=bar_width, color='g', label='ICV在车道0')
rl_inlane1 = plt.bar(index_rl_inlane1, height=value_rl_inlane1, width=bar_width, color='b', label='ICV在车道1')
rl_inlane2 = plt.bar(index_rl_inlane2, height=value_rl_inlane2, width=bar_width, color='k', label='ICV在车道2')
rl_inlane3 = plt.bar(index_rl_inlane3, height=value_rl_inlane3, width=bar_width, color='y', label='ICV在车道3')

autolabel(norl)
autolabel(rl_inlane0)
autolabel(rl_inlane1)
autolabel(rl_inlane2)
autolabel(rl_inlane3)

plt.legend(loc='right', bbox_to_anchor=(0.86, 1.1),ncol=5, handletextpad = 0.3)  # 显示图例
plt.xticks(index_norl + bar_width*2, check_x)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('检测卡口位置')
plt.ylabel('车头时距（s）')
plt.title('检测卡口的车头时距数据采集结果（全断面）')  # 图形标题
[xmin, xmax, ymin, ymax] = plt.axis()
ymin = 2.0
ymax = 4.0
plt.axis([xmin, xmax, ymin, ymax])

#plt.show()

# 车道3
fig2 = plt.figure(2)

value_norl = []
value_rl_inlane0 = []
value_rl_inlane1 = []
value_rl_inlane2 = []
value_rl_inlane3 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Time_headway_data = float(csv_data.at[collect_num,'Time_headway'])
	if Rl_lane_data == "none" and Check_ypos_data == "3":
		value_norl.append(Time_headway_data)
	if Rl_lane_data == "0" and Check_ypos_data == "3":
		value_rl_inlane0.append(Time_headway_data)
	if Rl_lane_data == "1" and Check_ypos_data == "3":
		value_rl_inlane1.append(Time_headway_data)
	if Rl_lane_data == "2" and Check_ypos_data == "3":
		value_rl_inlane2.append(Time_headway_data)
	if Rl_lane_data == "3" and Check_ypos_data == "3":
		value_rl_inlane3.append(Time_headway_data)

bar_width = 0.1
index_norl = np.arange(len(check_x))
index_rl_inlane0 = index_norl + bar_width
index_rl_inlane1 = index_rl_inlane0 + bar_width
index_rl_inlane2 = index_rl_inlane1 + bar_width
index_rl_inlane3 = index_rl_inlane2 + bar_width

ax2 = plt.subplot(411)

norl = plt.bar(index_norl, height=value_norl, width=bar_width, color='r', label='无ICV')
rl_inlane0 = plt.bar(index_rl_inlane0, height=value_rl_inlane0, width=bar_width, color='g', label='ICV在车道0')
rl_inlane1 = plt.bar(index_rl_inlane1, height=value_rl_inlane1, width=bar_width, color='b', label='ICV在车道1')
rl_inlane2 = plt.bar(index_rl_inlane2, height=value_rl_inlane2, width=bar_width, color='k', label='ICV在车道2')
rl_inlane3 = plt.bar(index_rl_inlane3, height=value_rl_inlane3, width=bar_width, color='y', label='ICV在车道3')

autolabel(norl)
autolabel(rl_inlane0)
autolabel(rl_inlane1)
autolabel(rl_inlane2)
autolabel(rl_inlane3)

#plt.legend(loc='right', bbox_to_anchor=(1, 1),ncol=1)  # 显示图例
plt.xticks(index_norl + bar_width*2, check_x)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('检测卡口位置')
plt.ylabel('车头时距（s）')
plt.title('检测卡口的车头时距数据采集结果（车道3）', fontdict={'weight': 'normal', 'size': 12})  # 图形标题

[xmin, xmax, ymin, ymax] = plt.axis()
ymin = 2.0
ymax = 5.0
plt.axis([xmin, xmax, ymin, ymax])

# 车道2
value_norl = []
value_rl_inlane0 = []
value_rl_inlane1 = []
value_rl_inlane2 = []
value_rl_inlane3 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Time_headway_data = float(csv_data.at[collect_num,'Time_headway'])
	if Rl_lane_data == "none" and Check_ypos_data == "2":
		value_norl.append(Time_headway_data)
	if Rl_lane_data == "0" and Check_ypos_data == "2":
		value_rl_inlane0.append(Time_headway_data)
	if Rl_lane_data == "1" and Check_ypos_data == "2":
		value_rl_inlane1.append(Time_headway_data)
	if Rl_lane_data == "2" and Check_ypos_data == "2":
		value_rl_inlane2.append(Time_headway_data)
	if Rl_lane_data == "3" and Check_ypos_data == "2":
		value_rl_inlane3.append(Time_headway_data)

bar_width = 0.1
index_norl = np.arange(len(check_x))
index_rl_inlane0 = index_norl + bar_width
index_rl_inlane1 = index_rl_inlane0 + bar_width
index_rl_inlane2 = index_rl_inlane1 + bar_width
index_rl_inlane3 = index_rl_inlane2 + bar_width

ax3 = plt.subplot(412)

norl = plt.bar(index_norl, height=value_norl, width=bar_width, color='r', label='无ICV')
rl_inlane0 = plt.bar(index_rl_inlane0, height=value_rl_inlane0, width=bar_width, color='g', label='ICV在车道0')
rl_inlane1 = plt.bar(index_rl_inlane1, height=value_rl_inlane1, width=bar_width, color='b', label='ICV在车道1')
rl_inlane2 = plt.bar(index_rl_inlane2, height=value_rl_inlane2, width=bar_width, color='k', label='ICV在车道2')
rl_inlane3 = plt.bar(index_rl_inlane3, height=value_rl_inlane3, width=bar_width, color='y', label='ICV在车道3')

autolabel(norl)
autolabel(rl_inlane0)
autolabel(rl_inlane1)
autolabel(rl_inlane2)
autolabel(rl_inlane3)

#plt.legend(loc='right', bbox_to_anchor=(1, 1),ncol=1)  # 显示图例
plt.xticks(index_norl + bar_width*2, check_x)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('检测卡口位置')
plt.ylabel('车头时距（s）')
plt.title('检测卡口的车头时距数据采集结果（车道2）', fontdict={'weight': 'normal', 'size': 12})  # 图形标题

[xmin, xmax, ymin, ymax] = plt.axis()
ymin = 2.0
ymax = 4.5
plt.axis([xmin, xmax, ymin, ymax])

# 车道1
value_norl = []
value_rl_inlane0 = []
value_rl_inlane1 = []
value_rl_inlane2 = []
value_rl_inlane3 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Time_headway_data = float(csv_data.at[collect_num,'Time_headway'])
	if Rl_lane_data == "none" and Check_ypos_data == "1":
		value_norl.append(Time_headway_data)
	if Rl_lane_data == "0" and Check_ypos_data == "1":
		value_rl_inlane0.append(Time_headway_data)
	if Rl_lane_data == "1" and Check_ypos_data == "1":
		value_rl_inlane1.append(Time_headway_data)
	if Rl_lane_data == "2" and Check_ypos_data == "1":
		value_rl_inlane2.append(Time_headway_data)
	if Rl_lane_data == "3" and Check_ypos_data == "1":
		value_rl_inlane3.append(Time_headway_data)

bar_width = 0.1
index_norl = np.arange(len(check_x))
index_rl_inlane0 = index_norl + bar_width
index_rl_inlane1 = index_rl_inlane0 + bar_width
index_rl_inlane2 = index_rl_inlane1 + bar_width
index_rl_inlane3 = index_rl_inlane2 + bar_width

ax4 = plt.subplot(413)

norl = plt.bar(index_norl, height=value_norl, width=bar_width, color='r', label='无ICV')
rl_inlane0 = plt.bar(index_rl_inlane0, height=value_rl_inlane0, width=bar_width, color='g', label='ICV在车道0')
rl_inlane1 = plt.bar(index_rl_inlane1, height=value_rl_inlane1, width=bar_width, color='b', label='ICV在车道1')
rl_inlane2 = plt.bar(index_rl_inlane2, height=value_rl_inlane2, width=bar_width, color='k', label='ICV在车道2')
rl_inlane3 = plt.bar(index_rl_inlane3, height=value_rl_inlane3, width=bar_width, color='y', label='ICV在车道3')

autolabel(norl)
autolabel(rl_inlane0)
autolabel(rl_inlane1)
autolabel(rl_inlane2)
autolabel(rl_inlane3)

#plt.legend(loc='right', bbox_to_anchor=(1, 1),ncol=1)  # 显示图例
plt.xticks(index_norl + bar_width*2, check_x)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('检测卡口位置')
plt.ylabel('车头时距（s）')
plt.title('检测卡口的车头时距数据采集结果（车道1）', fontdict={'weight': 'normal', 'size': 12})  # 图形标题

[xmin, xmax, ymin, ymax] = plt.axis()
ymin = 3.0
ymax = 7.0
plt.axis([xmin, xmax, ymin, ymax])

# 车道0
value_norl = []
value_rl_inlane0 = []
value_rl_inlane1 = []
value_rl_inlane2 = []
value_rl_inlane3 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Time_headway_data = float(csv_data.at[collect_num,'Time_headway'])
	if Rl_lane_data == "none" and Check_ypos_data == "0":
		value_norl.append(Time_headway_data)
	if Rl_lane_data == "0" and Check_ypos_data == "0":
		value_rl_inlane0.append(Time_headway_data)
	if Rl_lane_data == "1" and Check_ypos_data == "0":
		value_rl_inlane1.append(Time_headway_data)
	if Rl_lane_data == "2" and Check_ypos_data == "0":
		value_rl_inlane2.append(Time_headway_data)
	if Rl_lane_data == "3" and Check_ypos_data == "0":
		value_rl_inlane3.append(Time_headway_data)

bar_width = 0.1
index_norl = np.arange(len(check_x))
index_rl_inlane0 = index_norl + bar_width
index_rl_inlane1 = index_rl_inlane0 + bar_width
index_rl_inlane2 = index_rl_inlane1 + bar_width
index_rl_inlane3 = index_rl_inlane2 + bar_width

ax5 = plt.subplot(414)

norl = plt.bar(index_norl, height=value_norl, width=bar_width, color='r', label='无ICV')
rl_inlane0 = plt.bar(index_rl_inlane0, height=value_rl_inlane0, width=bar_width, color='g', label='ICV在车道0')
rl_inlane1 = plt.bar(index_rl_inlane1, height=value_rl_inlane1, width=bar_width, color='b', label='ICV在车道1')
rl_inlane2 = plt.bar(index_rl_inlane2, height=value_rl_inlane2, width=bar_width, color='k', label='ICV在车道2')
rl_inlane3 = plt.bar(index_rl_inlane3, height=value_rl_inlane3, width=bar_width, color='y', label='ICV在车道3')

autolabel_1(norl)
autolabel_1(rl_inlane0)
autolabel_1(rl_inlane1)
autolabel_1(rl_inlane2)
autolabel_1(rl_inlane3)

plt.legend(loc='right', bbox_to_anchor=(0.86, 7.7),ncol=5, handletextpad = 0.3)  # 显示图例
plt.xticks(index_norl + bar_width*2, check_x)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('检测卡口位置')
plt.ylabel('车头时距（s）')
plt.title('检测卡口的车头时距数据采集结果（车道0）', fontdict={'weight': 'normal', 'size': 12})  # 图形标题

[xmin, xmax, ymin, ymax] = plt.axis()
ymin = 2.5
ymax = 20.0 # 12.7
plt.axis([xmin, xmax, ymin, ymax])

plt.subplots_adjust(hspace=1) # wspace=0.2, 
plt.show()


# Space_headway ****************************************************************************************
fig1 = plt.figure(1)

value_norl = []
value_rl_inlane0 = []
value_rl_inlane1 = []
value_rl_inlane2 = []
value_rl_inlane3 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Space_headway_data = float(csv_data.at[collect_num,'Space_headway'])
	if Rl_lane_data == "none" and Check_ypos_data == "T":
		value_norl.append(Space_headway_data)
	if Rl_lane_data == "0" and Check_ypos_data == "T":
		value_rl_inlane0.append(Space_headway_data)
	if Rl_lane_data == "1" and Check_ypos_data == "T":
		value_rl_inlane1.append(Space_headway_data)
	if Rl_lane_data == "2" and Check_ypos_data == "T":
		value_rl_inlane2.append(Space_headway_data)
	if Rl_lane_data == "3" and Check_ypos_data == "T":
		value_rl_inlane3.append(Space_headway_data)

bar_width = 0.15
index_norl = np.arange(len(check_x))
index_rl_inlane0 = index_norl + bar_width
index_rl_inlane1 = index_rl_inlane0 + bar_width
index_rl_inlane2 = index_rl_inlane1 + bar_width
index_rl_inlane3 = index_rl_inlane2 + bar_width

norl = plt.bar(index_norl, height=value_norl, width=bar_width, color='r', label='无ICV')
rl_inlane0 = plt.bar(index_rl_inlane0, height=value_rl_inlane0, width=bar_width, color='g', label='ICV在车道0')
rl_inlane1 = plt.bar(index_rl_inlane1, height=value_rl_inlane1, width=bar_width, color='b', label='ICV在车道1')
rl_inlane2 = plt.bar(index_rl_inlane2, height=value_rl_inlane2, width=bar_width, color='k', label='ICV在车道2')
rl_inlane3 = plt.bar(index_rl_inlane3, height=value_rl_inlane3, width=bar_width, color='y', label='ICV在车道3')

autolabel_1(norl)
autolabel_1(rl_inlane0)
autolabel_1(rl_inlane1)
autolabel_1(rl_inlane2)
autolabel_1(rl_inlane3)

plt.legend(loc='right', bbox_to_anchor=(0.86, 1.1),ncol=5, handletextpad = 0.3)  # 显示图例
plt.xticks(index_norl + bar_width*2, check_x)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('检测卡口位置')
plt.ylabel('车头间距（m）')
plt.title('检测卡口的车头间距数据采集结果（全断面）')  # 图形标题
[xmin, xmax, ymin, ymax] = plt.axis()
ymin = 80
ymax = 120
plt.axis([xmin, xmax, ymin, ymax])

#plt.show()

# 车道3
fig2 = plt.figure(2)

value_norl = []
value_rl_inlane0 = []
value_rl_inlane1 = []
value_rl_inlane2 = []
value_rl_inlane3 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Space_headway_data = float(csv_data.at[collect_num,'Space_headway'])
	if Rl_lane_data == "none" and Check_ypos_data == "3":
		value_norl.append(Space_headway_data)
	if Rl_lane_data == "0" and Check_ypos_data == "3":
		value_rl_inlane0.append(Space_headway_data)
	if Rl_lane_data == "1" and Check_ypos_data == "3":
		value_rl_inlane1.append(Space_headway_data)
	if Rl_lane_data == "2" and Check_ypos_data == "3":
		value_rl_inlane2.append(Space_headway_data)
	if Rl_lane_data == "3" and Check_ypos_data == "3":
		value_rl_inlane3.append(Space_headway_data)

bar_width = 0.1
index_norl = np.arange(len(check_x))
index_rl_inlane0 = index_norl + bar_width
index_rl_inlane1 = index_rl_inlane0 + bar_width
index_rl_inlane2 = index_rl_inlane1 + bar_width
index_rl_inlane3 = index_rl_inlane2 + bar_width

ax2 = plt.subplot(411)

norl = plt.bar(index_norl, height=value_norl, width=bar_width, color='r', label='无ICV')
rl_inlane0 = plt.bar(index_rl_inlane0, height=value_rl_inlane0, width=bar_width, color='g', label='ICV在车道0')
rl_inlane1 = plt.bar(index_rl_inlane1, height=value_rl_inlane1, width=bar_width, color='b', label='ICV在车道1')
rl_inlane2 = plt.bar(index_rl_inlane2, height=value_rl_inlane2, width=bar_width, color='k', label='ICV在车道2')
rl_inlane3 = plt.bar(index_rl_inlane3, height=value_rl_inlane3, width=bar_width, color='y', label='ICV在车道3')

autolabel_1_higher_left(norl)
autolabel_1_higher_left(rl_inlane0)
autolabel_1_higher_left(rl_inlane1)
autolabel_1_higher_left(rl_inlane2)
autolabel_1_higher_left(rl_inlane3)

#plt.legend(loc='right', bbox_to_anchor=(1, 1),ncol=1)  # 显示图例
plt.xticks(index_norl + bar_width*2, check_x)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('检测卡口位置')
plt.ylabel('车头间距（m）')
plt.title('检测卡口的车头间距数据采集结果（车道3）', fontdict={'weight': 'normal', 'size': 12})  # 图形标题

[xmin, xmax, ymin, ymax] = plt.axis()
ymin = 80
ymax = 130
plt.axis([xmin, xmax, ymin, ymax])

# 车道2
value_norl = []
value_rl_inlane0 = []
value_rl_inlane1 = []
value_rl_inlane2 = []
value_rl_inlane3 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Space_headway_data = float(csv_data.at[collect_num,'Space_headway'])
	if Rl_lane_data == "none" and Check_ypos_data == "2":
		value_norl.append(Space_headway_data)
	if Rl_lane_data == "0" and Check_ypos_data == "2":
		value_rl_inlane0.append(Space_headway_data)
	if Rl_lane_data == "1" and Check_ypos_data == "2":
		value_rl_inlane1.append(Space_headway_data)
	if Rl_lane_data == "2" and Check_ypos_data == "2":
		value_rl_inlane2.append(Space_headway_data)
	if Rl_lane_data == "3" and Check_ypos_data == "2":
		value_rl_inlane3.append(Space_headway_data)

bar_width = 0.1
index_norl = np.arange(len(check_x))
index_rl_inlane0 = index_norl + bar_width
index_rl_inlane1 = index_rl_inlane0 + bar_width
index_rl_inlane2 = index_rl_inlane1 + bar_width
index_rl_inlane3 = index_rl_inlane2 + bar_width

ax3 = plt.subplot(412)

norl = plt.bar(index_norl, height=value_norl, width=bar_width, color='r', label='无ICV')
rl_inlane0 = plt.bar(index_rl_inlane0, height=value_rl_inlane0, width=bar_width, color='g', label='ICV在车道0')
rl_inlane1 = plt.bar(index_rl_inlane1, height=value_rl_inlane1, width=bar_width, color='b', label='ICV在车道1')
rl_inlane2 = plt.bar(index_rl_inlane2, height=value_rl_inlane2, width=bar_width, color='k', label='ICV在车道2')
rl_inlane3 = plt.bar(index_rl_inlane3, height=value_rl_inlane3, width=bar_width, color='y', label='ICV在车道3')

autolabel_1_higher_left(norl)
autolabel_1_higher_left(rl_inlane0)
autolabel_1_higher_left(rl_inlane1)
autolabel_1_higher_left(rl_inlane2)
autolabel_1_higher_left(rl_inlane3)

#plt.legend(loc='right', bbox_to_anchor=(1, 1),ncol=1)  # 显示图例
plt.xticks(index_norl + bar_width*2, check_x)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('检测卡口位置')
plt.ylabel('车头间距（m）')
plt.title('检测卡口的车头间距数据采集结果（车道2）', fontdict={'weight': 'normal', 'size': 12})  # 图形标题

[xmin, xmax, ymin, ymax] = plt.axis()
ymin = 60
ymax = 120
plt.axis([xmin, xmax, ymin, ymax])

# 车道1
value_norl = []
value_rl_inlane0 = []
value_rl_inlane1 = []
value_rl_inlane2 = []
value_rl_inlane3 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Space_headway_data = float(csv_data.at[collect_num,'Space_headway'])
	if Rl_lane_data == "none" and Check_ypos_data == "1":
		value_norl.append(Space_headway_data)
	if Rl_lane_data == "0" and Check_ypos_data == "1":
		value_rl_inlane0.append(Space_headway_data)
	if Rl_lane_data == "1" and Check_ypos_data == "1":
		value_rl_inlane1.append(Space_headway_data)
	if Rl_lane_data == "2" and Check_ypos_data == "1":
		value_rl_inlane2.append(Space_headway_data)
	if Rl_lane_data == "3" and Check_ypos_data == "1":
		value_rl_inlane3.append(Space_headway_data)

bar_width = 0.1
index_norl = np.arange(len(check_x))
index_rl_inlane0 = index_norl + bar_width
index_rl_inlane1 = index_rl_inlane0 + bar_width
index_rl_inlane2 = index_rl_inlane1 + bar_width
index_rl_inlane3 = index_rl_inlane2 + bar_width

ax4 = plt.subplot(413)

norl = plt.bar(index_norl, height=value_norl, width=bar_width, color='r', label='无ICV')
rl_inlane0 = plt.bar(index_rl_inlane0, height=value_rl_inlane0, width=bar_width, color='g', label='ICV在车道0')
rl_inlane1 = plt.bar(index_rl_inlane1, height=value_rl_inlane1, width=bar_width, color='b', label='ICV在车道1')
rl_inlane2 = plt.bar(index_rl_inlane2, height=value_rl_inlane2, width=bar_width, color='k', label='ICV在车道2')
rl_inlane3 = plt.bar(index_rl_inlane3, height=value_rl_inlane3, width=bar_width, color='y', label='ICV在车道3')

autolabel_1_higher_left(norl)
autolabel_1_higher_left(rl_inlane0)
autolabel_1_higher_left(rl_inlane1)
autolabel_1_higher_left(rl_inlane2)
autolabel_1_higher_left(rl_inlane3)

#plt.legend(loc='right', bbox_to_anchor=(1, 1),ncol=1)  # 显示图例
plt.xticks(index_norl + bar_width*2, check_x)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('检测卡口位置')
plt.ylabel('车头间距（m）')
plt.title('检测卡口的车头间距数据采集结果（车道1）', fontdict={'weight': 'normal', 'size': 12})  # 图形标题

[xmin, xmax, ymin, ymax] = plt.axis()
ymin = 80
ymax = 200
plt.axis([xmin, xmax, ymin, ymax])

# 车道0
value_norl = []
value_rl_inlane0 = []
value_rl_inlane1 = []
value_rl_inlane2 = []
value_rl_inlane3 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Space_headway_data = float(csv_data.at[collect_num,'Space_headway'])
	if Rl_lane_data == "none" and Check_ypos_data == "0":
		value_norl.append(Space_headway_data)
	if Rl_lane_data == "0" and Check_ypos_data == "0":
		value_rl_inlane0.append(Space_headway_data)
	if Rl_lane_data == "1" and Check_ypos_data == "0":
		value_rl_inlane1.append(Space_headway_data)
	if Rl_lane_data == "2" and Check_ypos_data == "0":
		value_rl_inlane2.append(Space_headway_data)
	if Rl_lane_data == "3" and Check_ypos_data == "0":
		value_rl_inlane3.append(Space_headway_data)

bar_width = 0.1
index_norl = np.arange(len(check_x))
index_rl_inlane0 = index_norl + bar_width
index_rl_inlane1 = index_rl_inlane0 + bar_width
index_rl_inlane2 = index_rl_inlane1 + bar_width
index_rl_inlane3 = index_rl_inlane2 + bar_width

ax5 = plt.subplot(414)

norl = plt.bar(index_norl, height=value_norl, width=bar_width, color='r', label='无ICV')
rl_inlane0 = plt.bar(index_rl_inlane0, height=value_rl_inlane0, width=bar_width, color='g', label='ICV在车道0')
rl_inlane1 = plt.bar(index_rl_inlane1, height=value_rl_inlane1, width=bar_width, color='b', label='ICV在车道1')
rl_inlane2 = plt.bar(index_rl_inlane2, height=value_rl_inlane2, width=bar_width, color='k', label='ICV在车道2')
rl_inlane3 = plt.bar(index_rl_inlane3, height=value_rl_inlane3, width=bar_width, color='y', label='ICV在车道3')

autolabel_1_higher(norl)
autolabel_1_higher(rl_inlane0)
autolabel_1_higher(rl_inlane1)
autolabel_1_higher(rl_inlane2)
autolabel_1_higher(rl_inlane3)

plt.legend(loc='right', bbox_to_anchor=(0.86, 7.7),ncol=5, handletextpad = 0.3)  # 显示图例
plt.xticks(index_norl + bar_width*2, check_x)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('检测卡口位置')
plt.ylabel('车头间距（m）')
plt.title('检测卡口的车头间距数据采集结果（车道0）', fontdict={'weight': 'normal', 'size': 12})  # 图形标题

[xmin, xmax, ymin, ymax] = plt.axis()
ymin = 50
ymax = 550
plt.axis([xmin, xmax, ymin, ymax])

plt.subplots_adjust(hspace=1) # wspace=0.2, 
plt.show()


# Speed ****************************************************************************************
fig1 = plt.figure(1)

value_norl = []
value_rl_inlane0 = []
value_rl_inlane1 = []
value_rl_inlane2 = []
value_rl_inlane3 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Speed_data = float(csv_data.at[collect_num,'Speed'])
	if Rl_lane_data == "none" and Check_ypos_data == "T":
		value_norl.append(Speed_data)
	if Rl_lane_data == "0" and Check_ypos_data == "T":
		value_rl_inlane0.append(Speed_data)
	if Rl_lane_data == "1" and Check_ypos_data == "T":
		value_rl_inlane1.append(Speed_data)
	if Rl_lane_data == "2" and Check_ypos_data == "T":
		value_rl_inlane2.append(Speed_data)
	if Rl_lane_data == "3" and Check_ypos_data == "T":
		value_rl_inlane3.append(Speed_data)

bar_width = 0.15
index_norl = np.arange(len(check_x))
index_rl_inlane0 = index_norl + bar_width
index_rl_inlane1 = index_rl_inlane0 + bar_width
index_rl_inlane2 = index_rl_inlane1 + bar_width
index_rl_inlane3 = index_rl_inlane2 + bar_width

norl = plt.bar(index_norl, height=value_norl, width=bar_width, color='r', label='无ICV')
rl_inlane0 = plt.bar(index_rl_inlane0, height=value_rl_inlane0, width=bar_width, color='g', label='ICV在车道0')
rl_inlane1 = plt.bar(index_rl_inlane1, height=value_rl_inlane1, width=bar_width, color='b', label='ICV在车道1')
rl_inlane2 = plt.bar(index_rl_inlane2, height=value_rl_inlane2, width=bar_width, color='k', label='ICV在车道2')
rl_inlane3 = plt.bar(index_rl_inlane3, height=value_rl_inlane3, width=bar_width, color='y', label='ICV在车道3')

autolabel_1_lower(norl)
autolabel_1_lower(rl_inlane0)
autolabel_1_lower(rl_inlane1)
autolabel_1_lower(rl_inlane2)
autolabel_1_lower(rl_inlane3)

plt.legend(loc='right', bbox_to_anchor=(0.86, 1.1),ncol=5, handletextpad = 0.3)  # 显示图例
plt.xticks(index_norl + bar_width*2, check_x)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('检测卡口位置')
plt.ylabel('车速（m/s）')
plt.title('检测卡口的车速数据采集结果（全断面）')  # 图形标题
[xmin, xmax, ymin, ymax] = plt.axis()
ymin = 27
ymax = 29.0
plt.axis([xmin, xmax, ymin, ymax])

#plt.show()

# 车道3
fig2 = plt.figure(2)

value_norl = []
value_rl_inlane0 = []
value_rl_inlane1 = []
value_rl_inlane2 = []
value_rl_inlane3 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Speed_data = float(csv_data.at[collect_num,'Speed'])
	if Rl_lane_data == "none" and Check_ypos_data == "3":
		value_norl.append(Speed_data)
	if Rl_lane_data == "0" and Check_ypos_data == "3":
		value_rl_inlane0.append(Speed_data)
	if Rl_lane_data == "1" and Check_ypos_data == "3":
		value_rl_inlane1.append(Speed_data)
	if Rl_lane_data == "2" and Check_ypos_data == "3":
		value_rl_inlane2.append(Speed_data)
	if Rl_lane_data == "3" and Check_ypos_data == "3":
		value_rl_inlane3.append(Speed_data)

bar_width = 0.1
index_norl = np.arange(len(check_x))
index_rl_inlane0 = index_norl + bar_width
index_rl_inlane1 = index_rl_inlane0 + bar_width
index_rl_inlane2 = index_rl_inlane1 + bar_width
index_rl_inlane3 = index_rl_inlane2 + bar_width

ax2 = plt.subplot(411)

norl = plt.bar(index_norl, height=value_norl, width=bar_width, color='r', label='无ICV')
rl_inlane0 = plt.bar(index_rl_inlane0, height=value_rl_inlane0, width=bar_width, color='g', label='ICV在车道0')
rl_inlane1 = plt.bar(index_rl_inlane1, height=value_rl_inlane1, width=bar_width, color='b', label='ICV在车道1')
rl_inlane2 = plt.bar(index_rl_inlane2, height=value_rl_inlane2, width=bar_width, color='k', label='ICV在车道2')
rl_inlane3 = plt.bar(index_rl_inlane3, height=value_rl_inlane3, width=bar_width, color='y', label='ICV在车道3')

autolabel_1(norl)
autolabel_1(rl_inlane0)
autolabel_1(rl_inlane1)
autolabel_1(rl_inlane2)
autolabel_1(rl_inlane3)

#plt.legend(loc='right', bbox_to_anchor=(1, 1),ncol=1)  # 显示图例
plt.xticks(index_norl + bar_width*2, check_x)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('检测卡口位置')
plt.ylabel('车速（m/s）')
plt.title('检测卡口的车速数据采集结果（车道3）', fontdict={'weight': 'normal', 'size': 12})  # 图形标题

[xmin, xmax, ymin, ymax] = plt.axis()
ymin = 26
ymax = 33
plt.axis([xmin, xmax, ymin, ymax])

# 车道2
value_norl = []
value_rl_inlane0 = []
value_rl_inlane1 = []
value_rl_inlane2 = []
value_rl_inlane3 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Speed_data = float(csv_data.at[collect_num,'Speed'])
	if Rl_lane_data == "none" and Check_ypos_data == "2":
		value_norl.append(Speed_data)
	if Rl_lane_data == "0" and Check_ypos_data == "2":
		value_rl_inlane0.append(Speed_data)
	if Rl_lane_data == "1" and Check_ypos_data == "2":
		value_rl_inlane1.append(Speed_data)
	if Rl_lane_data == "2" and Check_ypos_data == "2":
		value_rl_inlane2.append(Speed_data)
	if Rl_lane_data == "3" and Check_ypos_data == "2":
		value_rl_inlane3.append(Speed_data)

bar_width = 0.1
index_norl = np.arange(len(check_x))
index_rl_inlane0 = index_norl + bar_width
index_rl_inlane1 = index_rl_inlane0 + bar_width
index_rl_inlane2 = index_rl_inlane1 + bar_width
index_rl_inlane3 = index_rl_inlane2 + bar_width

ax3 = plt.subplot(412)

norl = plt.bar(index_norl, height=value_norl, width=bar_width, color='r', label='无ICV')
rl_inlane0 = plt.bar(index_rl_inlane0, height=value_rl_inlane0, width=bar_width, color='g', label='ICV在车道0')
rl_inlane1 = plt.bar(index_rl_inlane1, height=value_rl_inlane1, width=bar_width, color='b', label='ICV在车道1')
rl_inlane2 = plt.bar(index_rl_inlane2, height=value_rl_inlane2, width=bar_width, color='k', label='ICV在车道2')
rl_inlane3 = plt.bar(index_rl_inlane3, height=value_rl_inlane3, width=bar_width, color='y', label='ICV在车道3')

autolabel_1(norl)
autolabel_1(rl_inlane0)
autolabel_1(rl_inlane1)
autolabel_1(rl_inlane2)
autolabel_1(rl_inlane3)

#plt.legend(loc='right', bbox_to_anchor=(1, 1),ncol=1)  # 显示图例
plt.xticks(index_norl + bar_width*2, check_x)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('检测卡口位置')
plt.ylabel('车速（m/s）')
plt.title('检测卡口的车速数据采集结果（车道2）', fontdict={'weight': 'normal', 'size': 12})  # 图形标题

[xmin, xmax, ymin, ymax] = plt.axis()
ymin = 25
ymax = 30
plt.axis([xmin, xmax, ymin, ymax])

# 车道1
value_norl = []
value_rl_inlane0 = []
value_rl_inlane1 = []
value_rl_inlane2 = []
value_rl_inlane3 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Speed_data = float(csv_data.at[collect_num,'Speed'])
	if Rl_lane_data == "none" and Check_ypos_data == "1":
		value_norl.append(Speed_data)
	if Rl_lane_data == "0" and Check_ypos_data == "1":
		value_rl_inlane0.append(Speed_data)
	if Rl_lane_data == "1" and Check_ypos_data == "1":
		value_rl_inlane1.append(Speed_data)
	if Rl_lane_data == "2" and Check_ypos_data == "1":
		value_rl_inlane2.append(Speed_data)
	if Rl_lane_data == "3" and Check_ypos_data == "1":
		value_rl_inlane3.append(Speed_data)

bar_width = 0.1
index_norl = np.arange(len(check_x))
index_rl_inlane0 = index_norl + bar_width
index_rl_inlane1 = index_rl_inlane0 + bar_width
index_rl_inlane2 = index_rl_inlane1 + bar_width
index_rl_inlane3 = index_rl_inlane2 + bar_width

ax4 = plt.subplot(413)

norl = plt.bar(index_norl, height=value_norl, width=bar_width, color='r', label='无ICV')
rl_inlane0 = plt.bar(index_rl_inlane0, height=value_rl_inlane0, width=bar_width, color='g', label='ICV在车道0')
rl_inlane1 = plt.bar(index_rl_inlane1, height=value_rl_inlane1, width=bar_width, color='b', label='ICV在车道1')
rl_inlane2 = plt.bar(index_rl_inlane2, height=value_rl_inlane2, width=bar_width, color='k', label='ICV在车道2')
rl_inlane3 = plt.bar(index_rl_inlane3, height=value_rl_inlane3, width=bar_width, color='y', label='ICV在车道3')

autolabel_1(norl)
autolabel_1(rl_inlane0)
autolabel_1(rl_inlane1)
autolabel_1(rl_inlane2)
autolabel_1(rl_inlane3)

#plt.legend(loc='right', bbox_to_anchor=(1, 1),ncol=1)  # 显示图例
plt.xticks(index_norl + bar_width*2, check_x)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('检测卡口位置')
plt.ylabel('车速（m/s）')
plt.title('检测卡口的车速数据采集结果（车道1）', fontdict={'weight': 'normal', 'size': 12})  # 图形标题

[xmin, xmax, ymin, ymax] = plt.axis()
ymin = 22
ymax = 28
plt.axis([xmin, xmax, ymin, ymax])

# 车道0
value_norl = []
value_rl_inlane0 = []
value_rl_inlane1 = []
value_rl_inlane2 = []
value_rl_inlane3 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Speed_data = float(csv_data.at[collect_num,'Speed'])
	if Rl_lane_data == "none" and Check_ypos_data == "0":
		value_norl.append(Speed_data)
	if Rl_lane_data == "0" and Check_ypos_data == "0":
		value_rl_inlane0.append(Speed_data)
	if Rl_lane_data == "1" and Check_ypos_data == "0":
		value_rl_inlane1.append(Speed_data)
	if Rl_lane_data == "2" and Check_ypos_data == "0":
		value_rl_inlane2.append(Speed_data)
	if Rl_lane_data == "3" and Check_ypos_data == "0":
		value_rl_inlane3.append(Speed_data)

bar_width = 0.1
index_norl = np.arange(len(check_x))
index_rl_inlane0 = index_norl + bar_width
index_rl_inlane1 = index_rl_inlane0 + bar_width
index_rl_inlane2 = index_rl_inlane1 + bar_width
index_rl_inlane3 = index_rl_inlane2 + bar_width

ax5 = plt.subplot(414)

norl = plt.bar(index_norl, height=value_norl, width=bar_width, color='r', label='无ICV')
rl_inlane0 = plt.bar(index_rl_inlane0, height=value_rl_inlane0, width=bar_width, color='g', label='ICV在车道0')
rl_inlane1 = plt.bar(index_rl_inlane1, height=value_rl_inlane1, width=bar_width, color='b', label='ICV在车道1')
rl_inlane2 = plt.bar(index_rl_inlane2, height=value_rl_inlane2, width=bar_width, color='k', label='ICV在车道2')
rl_inlane3 = plt.bar(index_rl_inlane3, height=value_rl_inlane3, width=bar_width, color='y', label='ICV在车道3')

autolabel_1(norl)
autolabel_1(rl_inlane0)
autolabel_1(rl_inlane1)
autolabel_1(rl_inlane2)
autolabel_1(rl_inlane3)

plt.legend(loc='right', bbox_to_anchor=(0.86, 7.7),ncol=5, handletextpad = 0.3)  # 显示图例
plt.xticks(index_norl + bar_width*2, check_x)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('检测卡口位置')
plt.ylabel('车速（m/s）')
plt.title('检测卡口的车速数据采集结果（车道0）', fontdict={'weight': 'normal', 'size': 12})  # 图形标题

[xmin, xmax, ymin, ymax] = plt.axis()
ymin = 22
ymax = 30
plt.axis([xmin, xmax, ymin, ymax])

plt.subplots_adjust(hspace=1) # wspace=0.2, 
plt.show()


# Magnitude ****************************************************************************************
fig1 = plt.figure(1)
value_norl = []
value_rl_inlane0 = []
value_rl_inlane1 = []
value_rl_inlane2 = []
value_rl_inlane3 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Magnitude_data = float(csv_data.at[collect_num,'Magnitude'])
	if Rl_lane_data == "none" and Check_ypos_data == "T":
		value_norl.append(Magnitude_data)
	if Rl_lane_data == "0" and Check_ypos_data == "T":
		value_rl_inlane0.append(Magnitude_data)
	if Rl_lane_data == "1" and Check_ypos_data == "T":
		value_rl_inlane1.append(Magnitude_data)
	if Rl_lane_data == "2" and Check_ypos_data == "T":
		value_rl_inlane2.append(Magnitude_data)
	if Rl_lane_data == "3" and Check_ypos_data == "T":
		value_rl_inlane3.append(Magnitude_data)

bar_width = 0.15
index_norl = np.arange(len(check_x))
index_rl_inlane0 = index_norl + bar_width
index_rl_inlane1 = index_rl_inlane0 + bar_width
index_rl_inlane2 = index_rl_inlane1 + bar_width
index_rl_inlane3 = index_rl_inlane2 + bar_width

norl = plt.bar(index_norl, height=value_norl, width=bar_width, color='r', label='无ICV')
rl_inlane0 = plt.bar(index_rl_inlane0, height=value_rl_inlane0, width=bar_width, color='g', label='ICV在车道0')
rl_inlane1 = plt.bar(index_rl_inlane1, height=value_rl_inlane1, width=bar_width, color='b', label='ICV在车道1')
rl_inlane2 = plt.bar(index_rl_inlane2, height=value_rl_inlane2, width=bar_width, color='k', label='ICV在车道2')
rl_inlane3 = plt.bar(index_rl_inlane3, height=value_rl_inlane3, width=bar_width, color='y', label='ICV在车道3')

autolabel_1_left(norl)
autolabel_1_left(rl_inlane0)
autolabel_1_left(rl_inlane1)
autolabel_1_left(rl_inlane2)
autolabel_1_left(rl_inlane3)

plt.legend(loc='right', bbox_to_anchor=(0.86, 1.1),ncol=5, handletextpad = 0.3)  # 显示图例
plt.xticks(index_norl + bar_width*2, check_x)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('检测卡口位置')
plt.ylabel('交通流量（标准车数/次运行）')
plt.title('检测卡口的交通流量数据采集结果（全断面）')  # 图形标题
[xmin, xmax, ymin, ymax] = plt.axis()
ymin = 300
ymax = 470
plt.axis([xmin, xmax, ymin, ymax])

#plt.show()

# 无ICV时
fig2 = plt.figure(2)
value_1500 = []
value_3000 = []
value_4500 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Magnitude_data = float(csv_data.at[collect_num,'Magnitude'])
	if Rl_lane_data == "none" and Check_xpos_data == 1500 and Check_ypos_data != "T":
		value_1500.append(Magnitude_data)
	if Rl_lane_data == "none" and Check_xpos_data == 3000 and Check_ypos_data != "T":
		value_3000.append(Magnitude_data)
	if Rl_lane_data == "none" and Check_xpos_data == 4500 and Check_ypos_data != "T":
		value_4500.append(Magnitude_data)

label_checky = ['车道0', '车道1', '车道2', '车道3']
cols = ['r','g','m','y']

ax1 = plt.subplot(131)
plt.pie(value_1500,
        labels=label_checky,
        colors=cols,
        startangle=90,
        shadow= False,
        explode=(0,0,0,0),
        autopct='%1.1f%%')
plt.title('无ICV时1500米断面交通流量', fontdict={'weight': 'normal', 'size': 14})  # 图形标题

ax2 = plt.subplot(132)
plt.pie(value_3000,
        labels=label_checky,
        colors=cols,
        startangle=90,
        shadow= False,
        explode=(0,0,0,0),
        autopct='%1.1f%%')
plt.title('无ICV时3000米断面交通流量', fontdict={'weight': 'normal', 'size': 14})  # 图形标题

ax3 = plt.subplot(133)
plt.pie(value_4500,
        labels=label_checky,
        colors=cols,
        startangle=90,
        shadow= False,
        explode=(0,0,0,0),
        autopct='%1.1f%%')
plt.title('无ICV时4500米断面交通流量', fontdict={'weight': 'normal', 'size': 14})  # 图形标题
plt.legend(loc='right', bbox_to_anchor=(0.1, 1.2),ncol=4, handletextpad = 0.3)
plt.subplots_adjust(wspace=0.2, hspace=0.5) # wspace=0.2, 

# ICV在车道3
fig3 = plt.figure(3)
value_1500 = []
value_3000 = []
value_4500 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Magnitude_data = float(csv_data.at[collect_num,'Magnitude'])
	if Rl_lane_data == "3" and Check_xpos_data == 1500 and Check_ypos_data != "T":
		value_1500.append(Magnitude_data)
	if Rl_lane_data == "3" and Check_xpos_data == 3000 and Check_ypos_data != "T":
		value_3000.append(Magnitude_data)
	if Rl_lane_data == "3" and Check_xpos_data == 4500 and Check_ypos_data != "T":
		value_4500.append(Magnitude_data)

label_checky = ['车道0', '车道1', '车道2', '车道3']
cols = ['r','g','m','y']

ax4 = plt.subplot(131)
plt.pie(value_1500,
        labels=label_checky,
        colors=cols,
        startangle=90,
        shadow= False,
        explode=(0,0,0,0),
        autopct='%1.1f%%')
plt.title('ICV在车道3时1500米断面交通流量', fontdict={'weight': 'normal', 'size': 14})  # 图形标题

ax5 = plt.subplot(132)
plt.pie(value_3000,
        labels=label_checky,
        colors=cols,
        startangle=90,
        shadow= False,
        explode=(0,0,0,0),
        autopct='%1.1f%%')
plt.title('ICV在车道3时3000米断面交通流量', fontdict={'weight': 'normal', 'size': 14})  # 图形标题

ax6 = plt.subplot(133)
plt.pie(value_4500,
        labels=label_checky,
        colors=cols,
        startangle=90,
        shadow= False,
        explode=(0,0,0,0),
        autopct='%1.1f%%')
plt.title('ICV在车道3时4500米断面交通流量', fontdict={'weight': 'normal', 'size': 14})  # 图形标题
plt.legend(loc='right', bbox_to_anchor=(0.1, 1.2),ncol=4, handletextpad = 0.3)
plt.subplots_adjust(wspace=0.2, hspace=0.5) # wspace=0.2, 

# ICV在车道2
fig4 = plt.figure(4)
value_1500 = []
value_3000 = []
value_4500 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Magnitude_data = float(csv_data.at[collect_num,'Magnitude'])
	if Rl_lane_data == "2" and Check_xpos_data == 1500 and Check_ypos_data != "T":
		value_1500.append(Magnitude_data)
	if Rl_lane_data == "2" and Check_xpos_data == 3000 and Check_ypos_data != "T":
		value_3000.append(Magnitude_data)
	if Rl_lane_data == "2" and Check_xpos_data == 4500 and Check_ypos_data != "T":
		value_4500.append(Magnitude_data)

label_checky = ['车道0', '车道1', '车道2', '车道3']
cols = ['r','g','m','y']

ax7 = plt.subplot(1,3,1)
plt.pie(value_1500,
        labels=label_checky,
        colors=cols,
        startangle=90,
        shadow= False,
        explode=(0,0,0,0),
        autopct='%1.1f%%')
plt.title('ICV在车道2时1500米断面交通流量', fontdict={'weight': 'normal', 'size': 14})  # 图形标题

ax8 = plt.subplot(1,3,2)
plt.pie(value_3000,
        labels=label_checky,
        colors=cols,
        startangle=90,
        shadow= False,
        explode=(0,0,0,0),
        autopct='%1.1f%%')
plt.title('ICV在车道2时3000米断面交通流量', fontdict={'weight': 'normal', 'size': 14})  # 图形标题

ax9 = plt.subplot(1,3,3)
plt.pie(value_4500,
        labels=label_checky,
        colors=cols,
        startangle=90,
        shadow= False,
        explode=(0,0,0,0),
        autopct='%1.1f%%')
plt.title('ICV在车道2时4500米断面交通流量', fontdict={'weight': 'normal', 'size': 14})  # 图形标题
plt.legend(loc='right', bbox_to_anchor=(0.1, 1.2),ncol=4, handletextpad = 0.3)
plt.subplots_adjust(wspace=0.2, hspace=0.5) # wspace=0.2, 

# ICV在车道1
fig5 = plt.figure(5)
value_1500 = []
value_3000 = []
value_4500 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Magnitude_data = float(csv_data.at[collect_num,'Magnitude'])
	if Rl_lane_data == "1" and Check_xpos_data == 1500 and Check_ypos_data != "T":
		value_1500.append(Magnitude_data)
	if Rl_lane_data == "1" and Check_xpos_data == 3000 and Check_ypos_data != "T":
		value_3000.append(Magnitude_data)
	if Rl_lane_data == "1" and Check_xpos_data == 4500 and Check_ypos_data != "T":
		value_4500.append(Magnitude_data)

label_checky = ['车道0', '车道1', '车道2', '车道3']
cols = ['r','g','m','y']

ax10 = plt.subplot(1,3,1)
plt.pie(value_1500,
        labels=label_checky,
        colors=cols,
        startangle=90,
        shadow= False,
        explode=(0,0,0,0),
        autopct='%1.1f%%')
plt.title('ICV在车道1时1500米断面交通流量', fontdict={'weight': 'normal', 'size': 14})  # 图形标题

ax11 = plt.subplot(1,3,2)
plt.pie(value_3000,
        labels=label_checky,
        colors=cols,
        startangle=90,
        shadow= False,
        explode=(0,0,0,0),
        autopct='%1.1f%%')
plt.title('ICV在车道1时3000米断面交通流量', fontdict={'weight': 'normal', 'size': 14})  # 图形标题

ax12 = plt.subplot(1,3,3)
plt.pie(value_4500,
        labels=label_checky,
        colors=cols,
        startangle=90,
        shadow= False,
        explode=(0,0,0,0),
        autopct='%1.1f%%')
plt.title('ICV在车道1时4500米断面交通流量', fontdict={'weight': 'normal', 'size': 14})  # 图形标题
plt.legend(loc='right', bbox_to_anchor=(0.1, 1.2),ncol=4, handletextpad = 0.3)
plt.subplots_adjust(wspace=0.2, hspace=0.5) # wspace=0.2, 

# ICV在车道0
fig6 = plt.figure(6)
value_1500 = []
value_3000 = []
value_4500 = []

for collect_num in range(0,csv_data.shape[0]):
	Rl_lane_data = csv_data.at[collect_num,'Rl_lane']
	Check_xpos_data = csv_data.at[collect_num,'Check_xpos']
	Check_ypos_data = csv_data.at[collect_num,'Check_ypos']
	Magnitude_data = float(csv_data.at[collect_num,'Magnitude'])
	if Rl_lane_data == "0" and Check_xpos_data == 1500 and Check_ypos_data != "T":
		value_1500.append(Magnitude_data)
	if Rl_lane_data == "0" and Check_xpos_data == 3000 and Check_ypos_data != "T":
		value_3000.append(Magnitude_data)
	if Rl_lane_data == "0" and Check_xpos_data == 4500 and Check_ypos_data != "T":
		value_4500.append(Magnitude_data)

label_checky = ['车道0', '车道1', '车道2', '车道3']
cols = ['r','g','m','y']

ax13 = plt.subplot(1,3,1)
plt.pie(value_1500,
        labels=label_checky,
        colors=cols,
        startangle=90,
        shadow= False,
        explode=(0,0,0,0),
        autopct='%1.1f%%')
plt.title('ICV在车道0时1500米断面交通流量', fontdict={'weight': 'normal', 'size': 14})  # 图形标题

ax14 = plt.subplot(1,3,2)
plt.pie(value_3000,
        labels=label_checky,
        colors=cols,
        startangle=90,
        shadow= False,
        explode=(0,0,0,0),
        autopct='%1.1f%%')
plt.title('ICV在车道0时3000米断面交通流量', fontdict={'weight': 'normal', 'size': 14})  # 图形标题

ax15 = plt.subplot(1,3,3)
plt.pie(value_4500,
        labels=label_checky,
        colors=cols,
        startangle=90,
        shadow= False,
        explode=(0,0,0,0),
        autopct='%1.1f%%')
plt.title('ICV在车道0时4500米断面交通流量', fontdict={'weight': 'normal', 'size': 14})  # 图形标题
plt.legend(loc='right', bbox_to_anchor=(0.1, 1.2),ncol=4, handletextpad = 0.3)
plt.subplots_adjust(wspace=0.2, hspace=0.5) # wspace=0.2, 

plt.show()