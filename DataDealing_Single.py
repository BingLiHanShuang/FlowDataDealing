import csv
import os
import numpy as np
import random
import pandas as pd

import SensorDetection

csv_data = pd.read_csv('Lite_highway/Lite_highway_rl_inlane3.csv')

begin_time = 5000
end_time = 0
for find_num in range(0,csv_data.shape[0]):
	#id_data = csv_data.at[find_num,'id']
	type_data = csv_data.at[find_num,'type']
	time_data = float(csv_data.at[find_num,'time'])
	x_data = float(csv_data.at[find_num,'x'])
	#y_data = float(csv_data.at[find_num,'y'])
	#speed_data = float(csv_data.at[find_num,'speed'])
	
	if x_data >= 3000 and time_data < begin_time:
		begin_time = time_data
	if x_data <= 4500 and time_data > end_time:
		end_time = time_data
print(begin_time)
print(end_time)

csvfile = open("Output/Output_highway_rl_inlane3.csv", 'w')
csvwrite = csv.writer(csvfile)
fileHeader = ["rlid","runtime","touchID","touchResult","type_group","x_group","y_group","speed_group","vision_point_group","lidar_point_group"]
csvwrite.writerow(fileHeader)

#runtime = begin_time#199.8-500.2
runtime = 85.0#199.8-500.2 300.0
while runtime <= end_time:
	runtime = float('%.1f' % runtime)
	print(runtime)
	new_data = csv_data[csv_data.time.isin([str(runtime)])]
	#print(new_data.shape[0])
	#print(new_data.values)
	#new_data_group = []
	new_data_group = new_data.values
	
	for run_num in range(0,new_data_group.shape[0]):
		id_data = new_data_group[run_num][0]
		type_data = new_data_group[run_num][1]
		time_data = float(new_data_group[run_num][2])
		x_data = float(new_data_group[run_num][3])
		y_data = float(new_data_group[run_num][4])
		speed_data = float(new_data_group[run_num][6])
		if type_data[0] == 'R' and 3000 <= x_data <= 4500: # 4850, 5850
			#print(run_num)
			information0 = [id_data, time_data, "own", 99, type_data, x_data, y_data, speed_data, 99 ,99]
			csvwrite.writerow(information0)
			touchID_group = []
			touchResult_group = []
			type_group = []
			x_group = []
			y_group = []
			speed_group = []
			vision_point_group = []
			lidar_point_group = []
			touchID_group, touchResult_group, type_group, x_group, y_group, speed_group, vision_point_group, lidar_point_group = SensorDetection.SearchTargetCar(id_data, new_data_group, runtime, x_data, y_data)
			for i in range(len(touchID_group)):
				information = [id_data, time_data, touchID_group[i], touchResult_group[i], type_group[i], x_group[i], y_group[i], speed_group[i], vision_point_group[i], lidar_point_group[i]]
				csvwrite.writerow(information)
				
	runtime += 0.1

#rl_x:3000m-4500m

