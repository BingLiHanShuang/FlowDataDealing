import csv
import os
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
plt.rcParams['font.size'] = 12  # 字体大小
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

check_x = ('ICV在车道0', 'ICV在车道1', 'ICV在车道2', 'ICV在车道3')

def autolabel(rects):
	for rect in rects:
		height = rect.get_height()
		plt.text(rect.get_x()+rect.get_width()/2.0-0.07, 1.01*height, '%.1f' % height)

csv_data = pd.read_csv('Result/Result3_highway_rl_inlane0.csv')
csv_data2 = pd.read_csv('Result/Result3_highway_rl_inlane1.csv')
csv_data3 = pd.read_csv('Result/Result3_highway_rl_inlane2.csv')
csv_data4 = pd.read_csv('Result/Result3_highway_rl_inlane3.csv')

rl_car_AVEjourney = []
human_carGas_AVEjourney = []
human_carEle_AVEjourney = []
human_bus_AVEjourney = []
human_truck_AVEjourney = []
total_AVEjourney = []

rl_car = []
human_carGas = []
human_carEle = []
human_bus = []
human_truck = []
total = []
for collect_num in range(0,csv_data.shape[0]):
	id_data = csv_data.at[collect_num,'id']
	type_data = csv_data.at[collect_num,'type']
	journey_time_data = csv_data.at[collect_num,'journey_time']
	if type_data == "Rlcar":
		rl_car.append(journey_time_data)
	if type_data == "Gashumancar":
		human_carGas.append(journey_time_data)
	if type_data == "Elehumancar":
		human_carEle.append(journey_time_data)
	if type_data == "Bushuman":
		human_bus.append(journey_time_data)
	if type_data == "Truckhuman":
		human_truck.append(journey_time_data)
	total.append(journey_time_data)
rl_car_AVEjourney.append(float(sum(rl_car))/len(rl_car))
if len(human_carGas) == 0:
	human_carGas_AVEjourney.append(0)
else:
	human_carGas_AVEjourney.append(float(sum(human_carGas))/len(human_carGas))
human_carEle_AVEjourney.append(float(sum(human_carEle))/len(human_carEle))
human_bus_AVEjourney.append(float(sum(human_bus))/len(human_bus))
human_truck_AVEjourney.append(float(sum(human_truck))/len(human_truck))
total_AVEjourney.append(float(sum(total))/len(total))

rl_car = []
human_carGas = []
human_carEle = []
human_bus = []
human_truck = []
total = []
for collect_num in range(0,csv_data2.shape[0]):
	id_data = csv_data2.at[collect_num,'id']
	type_data = csv_data2.at[collect_num,'type']
	journey_time_data = csv_data2.at[collect_num,'journey_time']
	if type_data == "Rlcar":
		rl_car.append(journey_time_data)
	if type_data == "Gashumancar":
		human_carGas.append(journey_time_data)
	if type_data == "Elehumancar":
		human_carEle.append(journey_time_data)
	if type_data == "Bushuman":
		human_bus.append(journey_time_data)
	if type_data == "Truckhuman":
		human_truck.append(journey_time_data)
	total.append(journey_time_data)
rl_car_AVEjourney.append(float(sum(rl_car))/len(rl_car))
human_carGas_AVEjourney.append(float(sum(human_carGas))/len(human_carGas))
human_carEle_AVEjourney.append(float(sum(human_carEle))/len(human_carEle))
human_bus_AVEjourney.append(float(sum(human_bus))/len(human_bus))
human_truck_AVEjourney.append(float(sum(human_truck))/len(human_truck))
total_AVEjourney.append(float(sum(total))/len(total))

rl_car = []
human_carGas = []
human_carEle = []
human_bus = []
human_truck = []
total = []
for collect_num in range(0,csv_data3.shape[0]):
	id_data = csv_data3.at[collect_num,'id']
	type_data = csv_data3.at[collect_num,'type']
	journey_time_data = csv_data3.at[collect_num,'journey_time']
	if type_data == "Rlcar":
		rl_car.append(journey_time_data)
	if type_data == "Gashumancar":
		human_carGas.append(journey_time_data)
	if type_data == "Elehumancar":
		human_carEle.append(journey_time_data)
	if type_data == "Bushuman":
		human_bus.append(journey_time_data)
	if type_data == "Truckhuman":
		human_truck.append(journey_time_data)
	total.append(journey_time_data)
rl_car_AVEjourney.append(float(sum(rl_car))/len(rl_car))
human_carGas_AVEjourney.append(float(sum(human_carGas))/len(human_carGas))
human_carEle_AVEjourney.append(float(sum(human_carEle))/len(human_carEle))
human_bus_AVEjourney.append(float(sum(human_bus))/len(human_bus))
human_truck_AVEjourney.append(float(sum(human_truck))/len(human_truck))
total_AVEjourney.append(float(sum(total))/len(total))

rl_car = []
human_carGas = []
human_carEle = []
human_bus = []
human_truck = []
total = []
for collect_num in range(0,csv_data4.shape[0]):
	id_data = csv_data4.at[collect_num,'id']
	type_data = csv_data4.at[collect_num,'type']
	journey_time_data = csv_data4.at[collect_num,'journey_time']
	if type_data == "Rlcar":
		rl_car.append(journey_time_data)
	if type_data == "Gashumancar":
		human_carGas.append(journey_time_data)
	if type_data == "Elehumancar":
		human_carEle.append(journey_time_data)
	if type_data == "Bushuman":
		human_bus.append(journey_time_data)
	if type_data == "Truckhuman":
		human_truck.append(journey_time_data)
	total.append(journey_time_data)
rl_car_AVEjourney.append(float(sum(rl_car))/len(rl_car))
human_carGas_AVEjourney.append(float(sum(human_carGas))/len(human_carGas))
human_carEle_AVEjourney.append(float(sum(human_carEle))/len(human_carEle))
human_bus_AVEjourney.append(float(sum(human_bus))/len(human_bus))
if len(human_truck) == 0:
	human_truck_AVEjourney.append(0)
else:
	human_truck_AVEjourney.append(float(sum(human_truck))/len(human_truck))
total_AVEjourney.append(float(sum(total))/len(total))

bar_width = 0.15
index_rl_car = np.arange(len(check_x))
index_human_carGas = index_rl_car + bar_width
index_human_carEle = index_human_carGas + bar_width
index_human_bus = index_human_carEle + bar_width
index_human_truck = index_human_bus + bar_width
index_total = index_human_truck + bar_width

rl_car_bar = plt.bar(index_rl_car, height=rl_car_AVEjourney, width=bar_width, color='r', label='智能网联汽车')
human_carGas_bar = plt.bar(index_human_carGas, height=human_carGas_AVEjourney, width=bar_width, color='g', label='有人驾驶燃油汽车')
human_carEle_bar = plt.bar(index_human_carEle, height=human_carEle_AVEjourney, width=bar_width, color='b', label='有人驾驶电动汽车')
human_bus_bar = plt.bar(index_human_bus, height=human_bus_AVEjourney, width=bar_width, color='k', label='有人驾驶巴士')
human_truck_bar = plt.bar(index_human_truck, height=human_truck_AVEjourney, width=bar_width, color='y', label='有人驾驶卡车')
total_bar = plt.bar(index_total, height=total_AVEjourney, width=bar_width, color='m', label='所有车辆')

autolabel(rl_car_bar)
autolabel(human_carGas_bar)
autolabel(human_carEle_bar)
autolabel(human_bus_bar)
autolabel(human_truck_bar)
autolabel(total_bar)

plt.legend(loc='right', bbox_to_anchor=(1.025, 1.1),ncol=6, handletextpad = 0.3)  # 显示图例
plt.xticks(index_rl_car + bar_width*2, check_x)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('ICV所在车道')
plt.ylabel('行程时间（s）')
plt.title('智能网联汽车行程时间采集结果')  # 图形标题
[xmin, xmax, ymin, ymax] = plt.axis()
ymin = 20
ymax = 60
plt.axis([xmin, xmax, ymin, ymax])
plt.show()

