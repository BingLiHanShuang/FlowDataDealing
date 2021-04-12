import csv
import os
import numpy as np
import random
import pandas as pd

# 合并区间
def connect_range(A):
	for i in range(len(A) // 2):
		for j in range(i + 1, len(A) // 2):
			if A[2*i] > A[2*j]:
				A[2*i], A[2*i+1], A[2*j], A[2*j+1] = A[2*j], A[2*j+1], A[2*i], A[2*i+1]
	while True:
		B= []
		count = 0
		for i in range(0,len(A),2):
			if i+3 < len(A):
				if A[i] <= A[i+2] <= A[i+1] and A[i+2] <= A[i+1] <= A[i+3] :
					B.append(i+1)
					B.append(i+2)
					count += 1
				if A[i] <= A[i+2] <= A[i+1] and A[i+3] <= A[i+1]:
					B.append(i+2)
					B.append(i+3)
					count += 1
		if  count == 0:
			break
		for i in range(len(B)-1,-1,-1):
			A.pop(B[i])
	return A

rl_car = {'length': 4.552, 'width': 1.864, 'height': 1.654}# Lincoln MKC 4552*1864*1654
human_carGas = {'length': 4.670, 'width': 1.806, 'height': 1.474}# Volkswagen LAVIDA 4670*1806*1474 max:120km/h
human_carEle = {'length': 4.694, 'width': 1.850, 'height': 1.443}# Tesla Model3(CN) 4694*1850*1443 max:120km/h
human_bus = {'length': 7.148, 'width': 2.075, 'height': 2.770}# YUTONG T7 7148*2075*2770 max:120km/h
human_truck = {'length': 11.600, 'width': 2.550, 'height': 3.400}# SINOTRUK HOWO-A7-8*4 11600*2550*3400 max:100km/h

csv_data = pd.read_csv('Output/Output_highway_rl_inlane3.csv')

csvfile = open("Result/Result1_highway_rl_inlane3.csv", 'w')
csvwrite = csv.writer(csvfile)
fileHeader = ["lane_num","runtime","detected_percentage","idclear_percentage","blocked_percentage","average_speed","headway_spacing","headway"]
csvwrite.writerow(fileHeader)

csvfile2 = open("Result/Result2_highway_rl_inlane3.csv", 'w')
csvwrite2 = csv.writer(csvfile2)
fileHeader2 = ["runtime","detected_percentage","idclear_percentage","blocked_percentage","average_speed","rank_percentage","headway_spacing","headway","density","magnitude"]
csvwrite2.writerow(fileHeader2)

csvfile3 = open("Result/Result3_highway_rl_inlane3.csv", 'w')
csvwrite3 = csv.writer(csvfile3)
fileHeader3 = ["id","type","journey_time"]
csvwrite3.writerow(fileHeader3)

#runtime = begin_time#199.8-500.2
runtime = 85.0#199.8-500.2

id_group = []
id_data = " "
for find_num in range(0,csv_data.shape[0]):
	if float(csv_data.at[find_num,'touchResult']) != -1 and float(csv_data.at[find_num,'touchResult']) != 0:
		if float(csv_data.at[find_num,'touchResult']) == 99:
			id_data = csv_data.at[find_num,'rlid']
		else:
			id_data = csv_data.at[find_num,'touchID']
	if id_data != " " and bool(1-(id_data in id_group)):
		id_group.append(id_data)

for i in range(len(id_group)):
	if id_group[i][5] == "0":# flow_0* Rlcar
		new_data = csv_data[csv_data.rlid.isin([id_group[i]])&csv_data.touchID.isin(["own"])]
		new_data_group = new_data.values
		time_group = []
		xdata_group = []
		speed_group = []
		for run_num in range(0,new_data_group.shape[0]):
			time_data = float(new_data_group[run_num][1])
			x_data = float(new_data_group[run_num][5])
			speed_data = float(new_data_group[run_num][7])
			time_group.append(time_data)
			xdata_group.append(x_data)
			speed_group.append(speed_data)
		if min(xdata_group) <= 3100 and max(xdata_group) >= 4400:#1300m
			start_time = 0
			end_time = 0
			for run_num in range(0,len(time_group)):
				if xdata_group[run_num] > 3100 and xdata_group[run_num-1] < 3100:
					start_time = time_group[run_num-1] + float(3100 - xdata_group[run_num-1])/speed_group[run_num-1]
				if xdata_group[run_num] == 3100:
					start_time = time_group[run_num]
				if xdata_group[run_num] > 4400 and xdata_group[run_num-1] < 4400:
					end_time = time_group[run_num-1] + float(4400 - xdata_group[run_num-1])/speed_group[run_num-1]
				if xdata_group[run_num] == 4400:
					end_time = time_group[run_num]
			journey_time = end_time - start_time
			
			information = [id_group[i], "Rlcar", journey_time]
			csvwrite3.writerow(information)
	elif id_group[i][5] == "1":# flow_1* Gashumancar
		new_data = csv_data[csv_data.touchID.isin([id_group[i]])&csv_data.touchResult.isin([1])]
		new_data_group = new_data.values
		time_group = []
		xdata_group = []
		speed_group = []
		for run_num in range(0,new_data_group.shape[0]):
			time_data = float(new_data_group[run_num][1])
			x_data = float(new_data_group[run_num][5])
			speed_data = float(new_data_group[run_num][7])
			time_group.append(time_data)
			xdata_group.append(x_data)
			speed_group.append(speed_data)
		if min(xdata_group) <= 3100 and max(xdata_group) >= 4400:#1300m
			start_time = 0
			end_time = 0
			for run_num in range(0,len(time_group)):
				if xdata_group[run_num] > 3100 and xdata_group[run_num-1] < 3100:
					start_time = time_group[run_num-1] + float(3100 - xdata_group[run_num-1])/speed_group[run_num-1]
				if xdata_group[run_num] == 3100:
					start_time = time_group[run_num]
				if xdata_group[run_num] > 4400 and xdata_group[run_num-1] < 4400:
					end_time = time_group[run_num-1] + float(4400 - xdata_group[run_num-1])/speed_group[run_num-1]
				if xdata_group[run_num] == 4400:
					end_time = time_group[run_num]
			journey_time = end_time - start_time
			
			information = [id_group[i], "Gashumancar", journey_time]
			csvwrite3.writerow(information)
	elif id_group[i][5] == "2":# flow_2* Elehumancar
		new_data = csv_data[csv_data.touchID.isin([id_group[i]])&csv_data.touchResult.isin([1])]
		new_data_group = new_data.values
		time_group = []
		xdata_group = []
		speed_group = []
		for run_num in range(0,new_data_group.shape[0]):
			time_data = float(new_data_group[run_num][1])
			x_data = float(new_data_group[run_num][5])
			speed_data = float(new_data_group[run_num][7])
			time_group.append(time_data)
			xdata_group.append(x_data)
			speed_group.append(speed_data)
		if min(xdata_group) <= 3100 and max(xdata_group) >= 4400:#1300m
			start_time = 0
			end_time = 0
			for run_num in range(0,len(time_group)):
				if xdata_group[run_num] > 3100 and xdata_group[run_num-1] < 3100:
					start_time = time_group[run_num-1] + float(3100 - xdata_group[run_num-1])/speed_group[run_num-1]
				if xdata_group[run_num] == 3100:
					start_time = time_group[run_num]
				if xdata_group[run_num] > 4400 and xdata_group[run_num-1] < 4400:
					end_time = time_group[run_num-1] + float(4400 - xdata_group[run_num-1])/speed_group[run_num-1]
				if xdata_group[run_num] == 4400:
					end_time = time_group[run_num]
			journey_time = end_time - start_time
			
			information = [id_group[i], "Elehumancar", journey_time]
			csvwrite3.writerow(information)
	elif id_group[i][5] == "3":# flow_3* Bushuman
		new_data = csv_data[csv_data.touchID.isin([id_group[i]])&csv_data.touchResult.isin([1])]
		new_data_group = new_data.values
		time_group = []
		xdata_group = []
		speed_group = []
		for run_num in range(0,new_data_group.shape[0]):
			time_data = float(new_data_group[run_num][1])
			x_data = float(new_data_group[run_num][5])
			speed_data = float(new_data_group[run_num][7])
			time_group.append(time_data)
			xdata_group.append(x_data)
			speed_group.append(speed_data)
		if min(xdata_group) <= 3100 and max(xdata_group) >= 4400:#1300m
			start_time = 0
			end_time = 0
			for run_num in range(0,len(time_group)):
				if xdata_group[run_num] > 3100 and xdata_group[run_num-1] < 3100:
					start_time = time_group[run_num-1] + float(3100 - xdata_group[run_num-1])/speed_group[run_num-1]
				if xdata_group[run_num] == 3100:
					start_time = time_group[run_num]
				if xdata_group[run_num] > 4400 and xdata_group[run_num-1] < 4400:
					end_time = time_group[run_num-1] + float(4400 - xdata_group[run_num-1])/speed_group[run_num-1]
				if xdata_group[run_num] == 4400:
					end_time = time_group[run_num]
			journey_time = end_time - start_time
			
			information = [id_group[i], "Bushuman", journey_time]
			csvwrite3.writerow(information)
	elif id_group[i][5] == "4":# flow_4* Truckhuman
		new_data = csv_data[csv_data.touchID.isin([id_group[i]])&csv_data.touchResult.isin([1])]
		new_data_group = new_data.values
		time_group = []
		xdata_group = []
		speed_group = []
		for run_num in range(0,new_data_group.shape[0]):
			time_data = float(new_data_group[run_num][1])
			x_data = float(new_data_group[run_num][5])
			speed_data = float(new_data_group[run_num][7])
			time_group.append(time_data)
			xdata_group.append(x_data)
			speed_group.append(speed_data)
		if min(xdata_group) <= 3100 and max(xdata_group) >= 4400:#1300m
			start_time = 0
			end_time = 0
			for run_num in range(0,len(time_group)):
				if xdata_group[run_num] > 3100 and xdata_group[run_num-1] < 3100:
					start_time = time_group[run_num-1] + float(3100 - xdata_group[run_num-1])/speed_group[run_num-1]
				if xdata_group[run_num] == 3100:
					start_time = time_group[run_num]
				if xdata_group[run_num] > 4400 and xdata_group[run_num-1] < 4400:
					end_time = time_group[run_num-1] + float(4400 - xdata_group[run_num-1])/speed_group[run_num-1]
				if xdata_group[run_num] == 4400:
					end_time = time_group[run_num]
			journey_time = end_time - start_time
			
			information = [id_group[i], "Truckhuman", journey_time]
			csvwrite3.writerow(information)

while runtime <= 500:
	runtime = float('%.1f' % runtime)
	print(runtime)
	new_data = csv_data[csv_data.runtime.isin([str(runtime)])]
	new_data_group = new_data.values
	
	sum_speed_total = 0
	num_total = 0
	
	sum_speed_lane0 = 0
	sum_speed_lane1 = 0
	sum_speed_lane2 = 0
	sum_speed_lane3 = 0
	num_lane0 = 0
	num_lane1 = 0
	num_lane2 = 0
	num_lane3 = 0
	
	idclear_num_total = 0
	detected_num_total = 0
	blocked_num_total = 0
	total_num_total = 0
	total_num_total_standard = 0
	
	idclear_num0 = 0
	detected_num0 = 0
	blocked_num0 = 0
	total_num0 = 0
	idclear_num1 = 0
	detected_num1 = 0
	blocked_num1 = 0
	total_num1 = 0
	idclear_num2 = 0
	detected_num2 = 0
	blocked_num2 = 0
	total_num2 = 0
	idclear_num3 = 0
	detected_num3 = 0
	blocked_num3 = 0
	total_num3 = 0
	speed_group = []
	CAVspeed_group = []
	
	headwaySpacing_lane0 = 0
	hS_count_lane0 = 0
	headwaySpacing_lane1 = 0
	hS_count_lane1 = 0
	headwaySpacing_lane2 = 0
	hS_count_lane2 = 0
	headwaySpacing_lane3 = 0
	hS_count_lane3 = 0
	headwaySpacing_total = 0
	
	density_total = 0 # L = (120+150)*len(rlid_data_group)
	magnitude_total = 0
	rlid_data_group = []

	cover_range = []
	checked_id = []
	checked_FL_group = []
	
	for run_num in range(0,new_data_group.shape[0]):
		not_included = 0
		rlid_data = new_data_group[run_num][0]
		time_data = float(new_data_group[run_num][1])
		targetid_data = new_data_group[run_num][2]
		touchResult = float(new_data_group[run_num][3])
		type_data = new_data_group[run_num][4]
		x_data = float(new_data_group[run_num][5])
		y_data = float(new_data_group[run_num][6])
		speed_data = float(new_data_group[run_num][7])
		vision_point = float(new_data_group[run_num][8])
		lidar_point = float(new_data_group[run_num][9])
		
		vehicle_length = 0
		if rlid_data not in rlid_data_group:
			rlid_data_group.append(rlid_data)
		
		if targetid_data == "own" and rlid_data not in checked_id and 3000 <= x_data <= 4500:
			cover_range.append(x_data)
			checked_id.append(rlid_data)
			not_included = 1
		elif targetid_data not in checked_id:
			if type_data[0] == 'R' and 3000 <= x_data <= 4500:
				cover_range.append(x_data)
			checked_id.append(targetid_data)
			not_included = 1
		
		if type_data[0] == 'R':# Rlcar
			vehicle_length = rl_car['length']
		elif type_data[0] == 'G':# Gashumancar
			vehicle_length = human_carGas['length']
		elif type_data[0] == 'E':# Elehumancar
			vehicle_length = human_carEle['length']
		elif type_data[0] == 'B':# Bushuman
			vehicle_length = human_bus['length']
		elif type_data[0] == 'T':# Truckhuman
			vehicle_length = human_truck['length']
		
		if not_included == 1:
			if -15 <= y_data < -11.25: # Lane 0(Right)
				if touchResult == 1 or type_data[0] == 'R':
					idclear_num0 += 1
					detected_num0 += 1
				if touchResult == 0:
					detected_num0 += 1
				if touchResult == -1:
					blocked_num0 += 1
				total_num0+=1
			elif -11.25 <= y_data < -7.5: # Lane 1
				if touchResult == 1 or type_data[0] == 'R':
					idclear_num1 += 1
					detected_num1 += 1
				if touchResult == 0:
					detected_num1 += 1
				if touchResult == -1:
					blocked_num1 += 1
				total_num1+=1
			elif -7.5 <= y_data < -3.75: # Lane 2
				if touchResult == 1 or type_data[0] == 'R':
					idclear_num2 += 1
					detected_num2 += 1
				if touchResult == 0:
					detected_num2 += 1
				if touchResult == -1:
					blocked_num2 += 1
				total_num2+=1
			elif -3.75 <= y_data <= 0: # Lane 3
				if touchResult == 1 or type_data[0] == 'R':
					idclear_num3 += 1
					detected_num3 += 1
				if touchResult == 0:
					detected_num3 += 1
				if touchResult == -1:
					blocked_num3 += 1
				total_num3+=1
			# Total sum
			if touchResult == 1 or type_data[0] == 'R':
				idclear_num_total += 1
				detected_num_total += 1
			if touchResult == 0:
				detected_num_total += 1
			if touchResult == -1:
				blocked_num_total += 1
			total_num_total+=1
			if type_data[0] == 'R' or type_data[0] == 'G' or type_data[0] == 'E':# Rlcar Gashumancar Elehumancar
				total_num_total_standard += 1
			elif type_data[0] == 'B':# Bushuman
				total_num_total_standard += 1.5
			elif type_data[0] == 'T':# Truckhuman
				total_num_total_standard += 2
		
		# Count
		if touchResult != -1 or type_data[0] == 'R':
			if not_included == 1:
				sum_speed_total+=speed_data
				num_total += 1
			if -15 <= y_data < -11.25: # Lane 0(Right)
				for search_num in range(0,new_data_group.shape[0]):
					rlid_data_sear = new_data_group[search_num][0]
					targetid_data_sear = new_data_group[search_num][2] # NEW
					touchResult_sear = float(new_data_group[search_num][3])
					type_data_sear = new_data_group[search_num][4]
					x_data_sear = float(new_data_group[search_num][5])
					y_data_sear = float(new_data_group[search_num][6])
					vehicle_length_sear = 0
					if type_data_sear[0] == 'R':# Rlcar
						vehicle_length_sear = rl_car['length']
					elif type_data_sear[0] == 'G':# Gashumancar
						vehicle_length_sear = human_carGas['length']
					elif type_data_sear[0] == 'E':# Elehumancar
						vehicle_length_sear = human_carEle['length']
					elif type_data_sear[0] == 'B':# Bushuman
						vehicle_length_sear = human_bus['length']
					elif type_data_sear[0] == 'T':# Truckhuman
						vehicle_length_sear = human_truck['length']
					if rlid_data_sear == rlid_data and touchResult_sear != -1 and -15 <= y_data_sear < -11.25:
						nearby = 1
						for inside_num in range(0,new_data_group.shape[0]):
							rlid_data_sear2 = new_data_group[inside_num][0]
							touchResult_sear2 = float(new_data_group[inside_num][3])
							x_data_sear2 = float(new_data_group[inside_num][5])
							y_data_sear2 = float(new_data_group[inside_num][6])
							if rlid_data_sear2 == rlid_data and touchResult_sear2 != -1 and -15 <= y_data_sear2 < -11.25 and ((x_data_sear2 > x_data_sear and x_data_sear2 < x_data) or (x_data_sear2 < x_data_sear and x_data_sear2 > x_data)):
								nearby = 0
						if nearby == 1:
							check_prepare = []
							if targetid_data == "own":
								check_prepare.append(rlid_data)
							else:
								check_prepare.append(targetid_data)
							if targetid_data_sear == "own":
								check_prepare.append(rlid_data_sear)
							else:
								check_prepare.append(targetid_data_sear)
							if check_prepare not in checked_FL_group and [check_prepare[1],check_prepare[0]] not in checked_FL_group:
								checked_FL_group.append(check_prepare)
								checked_FL_group.append([check_prepare[1],check_prepare[0]])
								hS_count_lane0+=0.5 #1
								if x_data_sear - x_data > 0:
									headwaySpacing_lane0 += x_data_sear - x_data + vehicle_length_sear/2 - vehicle_length/2
								elif x_data_sear - x_data < 0:
									headwaySpacing_lane0 += x_data - x_data_sear - vehicle_length_sear/2 + vehicle_length/2
				if not_included == 1:
					sum_speed_lane0+=speed_data
					num_lane0+=1
			elif -11.25 <= y_data < -7.5: # Lane 1
				for search_num in range(0,new_data_group.shape[0]):
					rlid_data_sear = new_data_group[search_num][0]
					targetid_data_sear = new_data_group[search_num][2] # NEW
					touchResult_sear = float(new_data_group[search_num][3])
					type_data_sear = new_data_group[search_num][4]
					x_data_sear = float(new_data_group[search_num][5])
					y_data_sear = float(new_data_group[search_num][6])
					vehicle_length_sear = 0
					if type_data_sear[0] == 'R':# Rlcar
						vehicle_length_sear = rl_car['length']
					elif type_data_sear[0] == 'G':# Gashumancar
						vehicle_length_sear = human_carGas['length']
					elif type_data_sear[0] == 'E':# Elehumancar
						vehicle_length_sear = human_carEle['length']
					elif type_data_sear[0] == 'B':# Bushuman
						vehicle_length_sear = human_bus['length']
					elif type_data_sear[0] == 'T':# Truckhuman
						vehicle_length_sear = human_truck['length']
					if rlid_data_sear == rlid_data and touchResult_sear != -1 and -11.25 <= y_data_sear < -7.5:
						nearby = 1
						for inside_num in range(0,new_data_group.shape[0]):
							rlid_data_sear2 = new_data_group[inside_num][0]
							touchResult_sear2 = float(new_data_group[inside_num][3])
							x_data_sear2 = float(new_data_group[inside_num][5])
							y_data_sear2 = float(new_data_group[inside_num][6])
							if rlid_data_sear2 == rlid_data and touchResult_sear2 != -1 and -11.25 <= y_data_sear2 < -7.5 and ((x_data_sear2 > x_data_sear and x_data_sear2 < x_data) or (x_data_sear2 < x_data_sear and x_data_sear2 > x_data)):
								nearby = 0
						if nearby == 1:
							check_prepare = []
							if targetid_data == "own":
								check_prepare.append(rlid_data)
							else:
								check_prepare.append(targetid_data)
							if targetid_data_sear == "own":
								check_prepare.append(rlid_data_sear)
							else:
								check_prepare.append(targetid_data_sear)
							if check_prepare not in checked_FL_group and [check_prepare[1],check_prepare[0]] not in checked_FL_group:
								checked_FL_group.append(check_prepare)
								checked_FL_group.append([check_prepare[1],check_prepare[0]])
								hS_count_lane1+=0.5
								if x_data_sear - x_data > 0:
									headwaySpacing_lane1 += x_data_sear - x_data + vehicle_length_sear/2 - vehicle_length/2
								elif x_data_sear - x_data < 0:
									headwaySpacing_lane1 += x_data - x_data_sear - vehicle_length_sear/2 + vehicle_length/2
				if not_included == 1:
					sum_speed_lane1+=speed_data
					num_lane1+=1
			elif -7.5 <= y_data < -3.75: # Lane 2
				for search_num in range(0,new_data_group.shape[0]):
					rlid_data_sear = new_data_group[search_num][0]
					targetid_data_sear = new_data_group[search_num][2] # NEW
					touchResult_sear = float(new_data_group[search_num][3])
					type_data_sear = new_data_group[search_num][4]
					x_data_sear = float(new_data_group[search_num][5])
					y_data_sear = float(new_data_group[search_num][6])
					vehicle_length_sear = 0
					if type_data_sear[0] == 'R':# Rlcar
						vehicle_length_sear = rl_car['length']
					elif type_data_sear[0] == 'G':# Gashumancar
						vehicle_length_sear = human_carGas['length']
					elif type_data_sear[0] == 'E':# Elehumancar
						vehicle_length_sear = human_carEle['length']
					elif type_data_sear[0] == 'B':# Bushuman
						vehicle_length_sear = human_bus['length']
					elif type_data_sear[0] == 'T':# Truckhuman
						vehicle_length_sear = human_truck['length']
					if rlid_data_sear == rlid_data and touchResult_sear != -1 and -7.5 <= y_data_sear < -3.75:
						nearby = 1
						for inside_num in range(0,new_data_group.shape[0]):
							rlid_data_sear2 = new_data_group[inside_num][0]
							touchResult_sear2 = float(new_data_group[inside_num][3])
							x_data_sear2 = float(new_data_group[inside_num][5])
							y_data_sear2 = float(new_data_group[inside_num][6])
							if rlid_data_sear2 == rlid_data and touchResult_sear2 != -1 and -7.5 <= y_data_sear2 < -3.75 and ((x_data_sear2 > x_data_sear and x_data_sear2 < x_data) or (x_data_sear2 < x_data_sear and x_data_sear2 > x_data)):
								nearby = 0
						if nearby == 1:
							check_prepare = []
							if targetid_data == "own":
								check_prepare.append(rlid_data)
							else:
								check_prepare.append(targetid_data)
							if targetid_data_sear == "own":
								check_prepare.append(rlid_data_sear)
							else:
								check_prepare.append(targetid_data_sear)
							if check_prepare not in checked_FL_group and [check_prepare[1],check_prepare[0]] not in checked_FL_group:
								checked_FL_group.append(check_prepare)
								checked_FL_group.append([check_prepare[1],check_prepare[0]])
								hS_count_lane2+=0.5
								if x_data_sear - x_data > 0:
									headwaySpacing_lane2 += x_data_sear - x_data + vehicle_length_sear/2 - vehicle_length/2
								elif x_data_sear - x_data < 0:
									headwaySpacing_lane2 += x_data - x_data_sear - vehicle_length_sear/2 + vehicle_length/2
				if not_included == 1:
					sum_speed_lane2+=speed_data
					num_lane2+=1
			elif -3.75 <= y_data <= 0: # Lane 3
				for search_num in range(0,new_data_group.shape[0]):
					rlid_data_sear = new_data_group[search_num][0]
					targetid_data_sear = new_data_group[search_num][2] # NEW
					touchResult_sear = float(new_data_group[search_num][3])
					type_data_sear = new_data_group[search_num][4]
					x_data_sear = float(new_data_group[search_num][5])
					y_data_sear = float(new_data_group[search_num][6])
					vehicle_length_sear = 0
					if type_data_sear[0] == 'R':# Rlcar
						vehicle_length_sear = rl_car['length']
					elif type_data_sear[0] == 'G':# Gashumancar
						vehicle_length_sear = human_carGas['length']
					elif type_data_sear[0] == 'E':# Elehumancar
						vehicle_length_sear = human_carEle['length']
					elif type_data_sear[0] == 'B':# Bushuman
						vehicle_length_sear = human_bus['length']
					elif type_data_sear[0] == 'T':# Truckhuman
						vehicle_length_sear = human_truck['length']
					if rlid_data_sear == rlid_data and touchResult_sear != -1 and -3.75 <= y_data_sear <= 0:
						nearby = 1
						for inside_num in range(0,new_data_group.shape[0]):
							rlid_data_sear2 = new_data_group[inside_num][0]
							touchResult_sear2 = float(new_data_group[inside_num][3])
							x_data_sear2 = float(new_data_group[inside_num][5])
							y_data_sear2 = float(new_data_group[inside_num][6])
							if rlid_data_sear2 == rlid_data and touchResult_sear2 != -1 and -3.75 <= y_data_sear2 <= 0 and ((x_data_sear2 > x_data_sear and x_data_sear2 < x_data) or (x_data_sear2 < x_data_sear and x_data_sear2 > x_data)):
								nearby = 0
						if nearby == 1:
							check_prepare = []
							if targetid_data == "own":
								check_prepare.append(rlid_data)
							else:
								check_prepare.append(targetid_data)
							if targetid_data_sear == "own":
								check_prepare.append(rlid_data_sear)
							else:
								check_prepare.append(targetid_data_sear)
							if check_prepare not in checked_FL_group and [check_prepare[1],check_prepare[0]] not in checked_FL_group:
								checked_FL_group.append(check_prepare)
								checked_FL_group.append([check_prepare[1],check_prepare[0]])
								hS_count_lane3+=0.5
								if x_data_sear - x_data > 0:
									headwaySpacing_lane3 += x_data_sear - x_data + vehicle_length_sear/2 - vehicle_length/2
								elif x_data_sear - x_data < 0:
									headwaySpacing_lane3 += x_data - x_data_sear - vehicle_length_sear/2 + vehicle_length/2
				if not_included == 1:
					sum_speed_lane3+=speed_data
					num_lane3+=1
			#elif y_data == : # No other places
			
			if not_included == 1:
				speed_group.append(speed_data)
				if targetid_data == "own":
					CAVspeed_group.append(speed_group)
	
	if total_num_total == 0:
		runtime += 0.1
		continue
	
	if total_num_total == 0:
		detected_percentage_total = 0
		idclear_percentage_total = 0
		blocked_percentage_total = 0
	else:
		detected_percentage_total = float(detected_num_total)/total_num_total
		idclear_percentage_total = float(idclear_num_total)/total_num_total
		blocked_percentage_total = float(blocked_num_total)/total_num_total
	if num_total == 0:
		average_speed_total = 0
	else:
		average_speed_total = float(sum_speed_total)/num_total
	
	if total_num0 == 0:
		detected_percentage_lane0 = 0
		idclear_percentage_lane0 = 0
		blocked_percentage_lane0 = 0
	else:
		detected_percentage_lane0 = float(detected_num0)/total_num0
		idclear_percentage_lane0 = float(idclear_num0)/total_num0
		blocked_percentage_lane0 = float(blocked_num0)/total_num0
	if total_num1 == 0:
		detected_percentage_lane1 = 0
		idclear_percentage_lane1 = 0
		blocked_percentage_lane1 = 0
	else:
		detected_percentage_lane1 = float(detected_num1)/total_num1
		idclear_percentage_lane1 = float(idclear_num1)/total_num1
		blocked_percentage_lane1 = float(blocked_num1)/total_num1
	if total_num2 == 0:
		detected_percentage_lane2 = 0
		idclear_percentage_lane2 = 0
		blocked_percentage_lane2 = 0
	else:
		detected_percentage_lane2 = float(detected_num2)/total_num2
		idclear_percentage_lane2 = float(idclear_num2)/total_num2
		blocked_percentage_lane2 = float(blocked_num2)/total_num2
	if total_num3 == 0:
		detected_percentage_lane3 = 0
		idclear_percentage_lane3 = 0
		blocked_percentage_lane3 = 0
	else:
		detected_percentage_lane3 = float(detected_num3)/total_num3
		idclear_percentage_lane3 = float(idclear_num3)/total_num3
		blocked_percentage_lane3 = float(blocked_num3)/total_num3
	
	if num_lane0 == 0:
		average_speed_lane0 = 0
	else:
		average_speed_lane0 = float(sum_speed_lane0)/num_lane0
	if num_lane1 == 0:
		average_speed_lane1 = 0
	else:
		average_speed_lane1 = float(sum_speed_lane1)/num_lane1
	if num_lane2 == 0:
		average_speed_lane2 = 0
	else:
		average_speed_lane2 = float(sum_speed_lane2)/num_lane2
	if num_lane3 == 0:
		average_speed_lane3 = 0
	else:
		average_speed_lane3 = float(sum_speed_lane3)/num_lane3
	
	for i in range(len(speed_group)):
		for j in range(0, len(speed_group)-i-1):
			if speed_group[j] > speed_group[j+1]:
				speed_group[j], speed_group[j+1] = speed_group[j+1], speed_group[j]
	rank_sum = 0
	for i in range(len(speed_group)):
		for j in range(len(CAVspeed_group)):
			if CAVspeed_group[j] == speed_group[i]:
				rank_sum += i
	rank_percentage = float(rank_sum)/len(CAVspeed_group)/len(speed_group)*100
	
	if hS_count_lane0 + hS_count_lane1 + hS_count_lane2 + hS_count_lane3 == 0:
		headwaySpacing_total = 0
	else:
		headwaySpacing_total = float(headwaySpacing_lane0 + headwaySpacing_lane1 + headwaySpacing_lane2 + headwaySpacing_lane3)/(hS_count_lane0 + hS_count_lane1 + hS_count_lane2 + hS_count_lane3)
	if hS_count_lane0 == 0:
		headwaySpacing_lane0 = 0
	else:
		headwaySpacing_lane0 = float(headwaySpacing_lane0)/hS_count_lane0
	if hS_count_lane1 == 0:
		headwaySpacing_lane1 = 0
	else:
		headwaySpacing_lane1 = float(headwaySpacing_lane1)/hS_count_lane1
	if hS_count_lane2 == 0:
		headwaySpacing_lane2 = 0
	else:
		headwaySpacing_lane2 = float(headwaySpacing_lane2)/hS_count_lane2
	if hS_count_lane3 == 0:
		headwaySpacing_lane3 = 0
	else:
		headwaySpacing_lane3 = float(headwaySpacing_lane3)/hS_count_lane3
	
	if average_speed_total == 0:
		headway_total = 0
	else:
		headway_total = float(headwaySpacing_total)/average_speed_total
	if average_speed_lane0 == 0:
		headway_lane0 = 0
	else:
		headway_lane0 = float(headwaySpacing_lane0)/average_speed_lane0
	if average_speed_lane1 == 0:
		headway_lane1 = 0
	else:
		headway_lane1 = float(headwaySpacing_lane1)/average_speed_lane1
	if average_speed_lane2 == 0:
		headway_lane2 = 0
	else:
		headway_lane2 = float(headwaySpacing_lane2)/average_speed_lane2
	if average_speed_lane3 == 0:
		headway_lane3 = 0
	else:
		headway_lane3 = float(headwaySpacing_lane3)/average_speed_lane3
	
	#print(rlid_data_group)
	#density_total = float(1000)/headwaySpacing_total
	range_input = []
	for pos in cover_range:
		range_input.append(pos-120)
		range_input.append(pos+150)
	detected_A = connect_range(range_input)
	detected_length = 0
	for i in range(0, len(detected_A)-1, 2):
		detected_length = detected_length + detected_A[i+1] - detected_A[i]
	if total_num_total_standard == 0:
		density_total = 0
		print("total_num_total_standard == 0 ???")
	else:
		density_total = total_num_total_standard/float(detected_length)    # Rlcar, Gashumancar, Elehumancar - 1pcu, Bushuman - 1.5pcu, Truckhuman - 2pcu
		print("detected_length:", detected_length)
	magnitude_total = density_total*average_speed_total*1000*3.6
	
	#Write in or Draw-
	information = [0, runtime, detected_percentage_lane0, idclear_percentage_lane0, blocked_percentage_lane0, average_speed_lane0, headwaySpacing_lane0, headway_lane0]
	csvwrite.writerow(information)
	information = [1, runtime, detected_percentage_lane1, idclear_percentage_lane1, blocked_percentage_lane1, average_speed_lane1, headwaySpacing_lane1, headway_lane1]
	csvwrite.writerow(information)
	information = [2, runtime, detected_percentage_lane2, idclear_percentage_lane2, blocked_percentage_lane2, average_speed_lane2, headwaySpacing_lane2, headway_lane2]
	csvwrite.writerow(information)
	information = [3, runtime, detected_percentage_lane3, idclear_percentage_lane3, blocked_percentage_lane3, average_speed_lane3, headwaySpacing_lane3, headway_lane3]
	csvwrite.writerow(information)
	
	information = [runtime, detected_percentage_total, idclear_percentage_total, blocked_percentage_total, average_speed_total, rank_percentage, headwaySpacing_total, headway_total, density_total, magnitude_total]
	csvwrite2.writerow(information)
	
	runtime += 0.1

#rl_x:3000m-5850m

