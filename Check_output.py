import csv
import os
import numpy as np
import random
import pandas as pd

csvfile = open("Check_result.csv", 'w')
csvwrite = csv.writer(csvfile)
fileHeader = ["Rl_lane", "Check_xpos", "Check_ypos", "Time_headway", "Space_headway", "Speed", "Magnitude"]
csvwrite.writerow(fileHeader)

for csv_num in range(5):
	if csv_num == 0:
		csv_data = pd.read_csv('Lite_highway_Check/Lite_highway_Check_norl.csv')
	elif csv_num == 1:
		csv_data = pd.read_csv('Lite_highway_Check/Lite_highway_Check_rl_inlane0.csv')
	elif csv_num == 2:
		csv_data = pd.read_csv('Lite_highway_Check/Lite_highway_Check_rl_inlane1.csv')
	elif csv_num == 3:
		csv_data = pd.read_csv('Lite_highway_Check/Lite_highway_Check_rl_inlane2.csv')
	elif csv_num == 4:
		csv_data = pd.read_csv('Lite_highway_Check/Lite_highway_Check_rl_inlane3.csv')

	# Check_xpos: -1520, -3020, -4520
	# Check_ypos: 0(-13.13, right, -15~-11.25) 1(-9.38, -11.25~-7.5) 2(-5.62, -7.5~-3.75) 3(-1.88, left, -3.75~0)
	# Check_xpos: 1500
	# Time_headway
	pass_list = []
	time_headway_total_all = 0
	time_record_num_all = 0
	time_headway_total0 = 0
	time_record_num0 = 0
	time_headway_total1 = 0
	time_record_num1 = 0
	time_headway_total2 = 0
	time_record_num2 = 0
	time_headway_total3 = 0
	time_record_num3 = 0
	# Space_headway
	space_headway_total_all = 0
	space_record_num_all = 0
	space_headway_total0 = 0
	space_record_num0 = 0
	space_headway_total1 = 0
	space_record_num1 = 0
	space_headway_total2 = 0
	space_record_num2 = 0
	space_headway_total3 = 0
	space_record_num3 = 0
	# Speed
	speed_total_all = 0
	speed_record_num_all = 0
	speed_total0 = 0
	speed_record_num0 = 0
	speed_total1 = 0
	speed_record_num1 = 0
	speed_total2 = 0
	speed_record_num2 = 0
	speed_total3 = 0
	speed_record_num3 = 0
	# Magnitude
	magnitude_total_all = 0
	magnitude_total0 = 0
	magnitude_total1 = 0
	magnitude_total2 = 0
	magnitude_total3 = 0
	for find_num in range(0,csv_data.shape[0]):
		if csv_data.at[find_num,'id'] not in pass_list:
			if 1500 <= float(csv_data.at[find_num,'x']) + float(csv_data.at[find_num,'length'])/2 <= 1520:
				pass_list.append(csv_data.at[find_num,'id'])
				type_data = csv_data.at[find_num,'type']
				if -15 <= float(csv_data.at[find_num,'y']) < -11.25:
					speed_total0 += float(csv_data.at[find_num,'speed'])
					speed_record_num0 += 1
					if type_data[0] == 'R' or type_data[0] == 'G' or type_data[0] == 'E':
						magnitude_total0 += 1
					elif type_data[0] == 'B':
						magnitude_total0 += 1.5
					elif type_data[0] == 'T':
						magnitude_total0 += 2
				elif -11.25 <= float(csv_data.at[find_num,'y']) < -7.5:
					speed_total1 += float(csv_data.at[find_num,'speed'])
					speed_record_num1 += 1
					if type_data[0] == 'R' or type_data[0] == 'G' or type_data[0] == 'E':
						magnitude_total1 += 1
					elif type_data[0] == 'B':
						magnitude_total1 += 1.5
					elif type_data[0] == 'T':
						magnitude_total1 += 2
				elif -7.5 <= float(csv_data.at[find_num,'y']) < -3.75:
					speed_total2 += float(csv_data.at[find_num,'speed'])
					speed_record_num2 += 1
					if type_data[0] == 'R' or type_data[0] == 'G' or type_data[0] == 'E':
						magnitude_total2 += 1
					elif type_data[0] == 'B':
						magnitude_total2 += 1.5
					elif type_data[0] == 'T':
						magnitude_total2 += 2
				elif -3.75 <= float(csv_data.at[find_num,'y']) <= 0:
					speed_total3 += float(csv_data.at[find_num,'speed'])
					speed_record_num3 += 1
					if type_data[0] == 'R' or type_data[0] == 'G' or type_data[0] == 'E':
						magnitude_total3 += 1
					elif type_data[0] == 'B':
						magnitude_total3 += 1.5
					elif type_data[0] == 'T':
						magnitude_total3 += 2
				if str(csv_data.at[find_num,'follower_id']) != 'nan':
					for check_num in range(0,csv_data.shape[0]):
						if csv_data.at[check_num,'id'] == csv_data.at[find_num,'follower_id'] and csv_data.at[check_num,'time'] == csv_data.at[find_num,'time']:
							if -15 <= float(csv_data.at[find_num,'y']) < -11.25 and -15 <= float(csv_data.at[check_num,'y']) < -11.25:
								space_headway_total0 += (float(csv_data.at[find_num,'x']) - float(csv_data.at[check_num,'x']))
								space_record_num0 += 1
							elif -11.25 <= float(csv_data.at[find_num,'y']) < -7.5 and -11.25 <= float(csv_data.at[check_num,'y']) < -7.5:
								space_headway_total1 += (float(csv_data.at[find_num,'x']) - float(csv_data.at[check_num,'x']))
								space_record_num1 += 1
							elif -7.5 <= float(csv_data.at[find_num,'y']) < -3.75 and -7.5 <= float(csv_data.at[check_num,'y']) < -3.75:
								space_headway_total2 += (float(csv_data.at[find_num,'x']) - float(csv_data.at[check_num,'x']))
								space_record_num2 += 1
							elif -3.75 <= float(csv_data.at[find_num,'y']) <= 0 and -3.75 <= float(csv_data.at[check_num,'y']) <= 0:
								space_headway_total3 += (float(csv_data.at[find_num,'x']) - float(csv_data.at[check_num,'x']))
								space_record_num3 += 1
						if csv_data.at[check_num,'id'] == csv_data.at[find_num,'follower_id'] and 1500 <= float(csv_data.at[check_num,'x']) + float(csv_data.at[check_num,'length'])/2 <= 1520:
							if -15 <= float(csv_data.at[find_num,'y']) < -11.25 and -15 <= float(csv_data.at[check_num,'y']) < -11.25:
								time_headway_total0 += (float(csv_data.at[check_num,'time']) - float(csv_data.at[find_num,'time']))
								time_record_num0 += 1
								break
							elif -11.25 <= float(csv_data.at[find_num,'y']) < -7.5 and -11.25 <= float(csv_data.at[check_num,'y']) < -7.5:
								time_headway_total1 += (float(csv_data.at[check_num,'time']) - float(csv_data.at[find_num,'time']))
								time_record_num1 += 1
								break
							elif -7.5 <= float(csv_data.at[find_num,'y']) < -3.75 and -7.5 <= float(csv_data.at[check_num,'y']) < -3.75:
								time_headway_total2 += (float(csv_data.at[check_num,'time']) - float(csv_data.at[find_num,'time']))
								time_record_num2 += 1
								break
							elif -3.75 <= float(csv_data.at[find_num,'y']) <= 0 and -3.75 <= float(csv_data.at[check_num,'y']) <= 0:
								time_headway_total3 += (float(csv_data.at[check_num,'time']) - float(csv_data.at[find_num,'time']))
								time_record_num3 += 1
								break
							else:
								break
	time_headway_total_all = time_headway_total0 + time_headway_total1 + time_headway_total2 + time_headway_total3
	time_record_num_all = time_record_num0 + time_record_num1 + time_record_num2 + time_record_num3
	time_headway_total_1500 = time_headway_total_all/time_record_num_all
	time_headway_lane0_1500 = time_headway_total0/time_record_num0
	time_headway_lane1_1500 = time_headway_total1/time_record_num1
	time_headway_lane2_1500 = time_headway_total2/time_record_num2
	time_headway_lane3_1500 = time_headway_total3/time_record_num3
	space_headway_total_all = space_headway_total0 + space_headway_total1 + space_headway_total2 + space_headway_total3
	space_record_num_all = space_record_num0 + space_record_num1 + space_record_num2 + space_record_num3
	space_headway_total_1500 = space_headway_total_all/space_record_num_all
	space_headway_lane0_1500 = space_headway_total0/space_record_num0
	space_headway_lane1_1500 = space_headway_total1/space_record_num1
	space_headway_lane2_1500 = space_headway_total2/space_record_num2
	space_headway_lane3_1500 = space_headway_total3/space_record_num3
	speed_total_all = speed_total0 + speed_total1 + speed_total2 + speed_total3
	speed_record_num_all = speed_record_num0 + speed_record_num1 + speed_record_num2 + speed_record_num3
	speed_total_1500 = speed_total_all/speed_record_num_all
	speed_lane0_1500 = speed_total0/speed_record_num0
	speed_lane1_1500 = speed_total1/speed_record_num1
	speed_lane2_1500 = speed_total2/speed_record_num2
	speed_lane3_1500 = speed_total3/speed_record_num3
	magnitude_total_all = magnitude_total0 + magnitude_total1 + magnitude_total2 + magnitude_total3
	magnitude_total_1500 = magnitude_total_all
	magnitude_lane0_1500 = magnitude_total0
	magnitude_lane1_1500 = magnitude_total1
	magnitude_lane2_1500 = magnitude_total2
	magnitude_lane3_1500 = magnitude_total3
	print("time_headway_lane0_1500:", time_headway_lane0_1500) # 4.228571428571427
	print("time_headway_lane1_1500:", time_headway_lane1_1500) # 3.7103448275862068
	print("time_headway_lane2_1500:", time_headway_lane2_1500) # 3.3106382978723383
	print("time_headway_lane3_1500:", time_headway_lane3_1500) # 3.5049180327868856
	print("time_headway_total_1500:", time_headway_total_1500) # 3.5950464396284825
	print("space_headway_lane0_1500:", space_headway_lane0_1500) # 
	print("space_headway_lane1_1500:", space_headway_lane1_1500) # 
	print("space_headway_lane2_1500:", space_headway_lane2_1500) # 
	print("space_headway_lane3_1500:", space_headway_lane3_1500) # 
	print("space_headway_total_1500:", space_headway_total_1500) #
	print("speed_lane0_1500:", speed_lane0_1500) # 
	print("speed_lane1_1500:", speed_lane1_1500) # 
	print("speed_lane2_1500:", speed_lane2_1500) # 
	print("speed_lane3_1500:", speed_lane3_1500) # 
	print("speed_total_1500:", speed_total_1500) # 
	print("magnitude_lane0_1500:", magnitude_lane0_1500) # 
	print("magnitude_lane1_1500:", magnitude_lane1_1500) # 
	print("magnitude_lane2_1500:", magnitude_lane2_1500) # 
	print("magnitude_lane3_1500:", magnitude_lane3_1500) # 
	print("magnitude_total_1500:", magnitude_total_1500) # 

	if csv_num == 0:
		information0 = ["none", 1500, "0", time_headway_lane0_1500, space_headway_lane0_1500, speed_lane0_1500, magnitude_lane0_1500]
		information1 = ["none", 1500, "1", time_headway_lane1_1500, space_headway_lane1_1500, speed_lane1_1500, magnitude_lane1_1500]
		information2 = ["none", 1500, "2", time_headway_lane2_1500, space_headway_lane2_1500, speed_lane2_1500, magnitude_lane2_1500]
		information3 = ["none", 1500, "3", time_headway_lane3_1500, space_headway_lane3_1500, speed_lane3_1500, magnitude_lane3_1500]
		informationT = ["none", 1500, "T", time_headway_total_1500, space_headway_total_1500, speed_total_1500, magnitude_total_1500]
	elif csv_num == 1:
		information0 = ["0", 1500, "0", time_headway_lane0_1500, space_headway_lane0_1500, speed_lane0_1500, magnitude_lane0_1500]
		information1 = ["0", 1500, "1", time_headway_lane1_1500, space_headway_lane1_1500, speed_lane1_1500, magnitude_lane1_1500]
		information2 = ["0", 1500, "2", time_headway_lane2_1500, space_headway_lane2_1500, speed_lane2_1500, magnitude_lane2_1500]
		information3 = ["0", 1500, "3", time_headway_lane3_1500, space_headway_lane3_1500, speed_lane3_1500, magnitude_lane3_1500]
		informationT = ["0", 1500, "T", time_headway_total_1500, space_headway_total_1500, speed_total_1500, magnitude_total_1500]
	elif csv_num == 2:
		information0 = ["1", 1500, "0", time_headway_lane0_1500, space_headway_lane0_1500, speed_lane0_1500, magnitude_lane0_1500]
		information1 = ["1", 1500, "1", time_headway_lane1_1500, space_headway_lane1_1500, speed_lane1_1500, magnitude_lane1_1500]
		information2 = ["1", 1500, "2", time_headway_lane2_1500, space_headway_lane2_1500, speed_lane2_1500, magnitude_lane2_1500]
		information3 = ["1", 1500, "3", time_headway_lane3_1500, space_headway_lane3_1500, speed_lane3_1500, magnitude_lane3_1500]
		informationT = ["1", 1500, "T", time_headway_total_1500, space_headway_total_1500, speed_total_1500, magnitude_total_1500]
	elif csv_num == 3:
		information0 = ["2", 1500, "0", time_headway_lane0_1500, space_headway_lane0_1500, speed_lane0_1500, magnitude_lane0_1500]
		information1 = ["2", 1500, "1", time_headway_lane1_1500, space_headway_lane1_1500, speed_lane1_1500, magnitude_lane1_1500]
		information2 = ["2", 1500, "2", time_headway_lane2_1500, space_headway_lane2_1500, speed_lane2_1500, magnitude_lane2_1500]
		information3 = ["2", 1500, "3", time_headway_lane3_1500, space_headway_lane3_1500, speed_lane3_1500, magnitude_lane3_1500]
		informationT = ["2", 1500, "T", time_headway_total_1500, space_headway_total_1500, speed_total_1500, magnitude_total_1500]
	elif csv_num == 4:
		information0 = ["3", 1500, "0", time_headway_lane0_1500, space_headway_lane0_1500, speed_lane0_1500, magnitude_lane0_1500]
		information1 = ["3", 1500, "1", time_headway_lane1_1500, space_headway_lane1_1500, speed_lane1_1500, magnitude_lane1_1500]
		information2 = ["3", 1500, "2", time_headway_lane2_1500, space_headway_lane2_1500, speed_lane2_1500, magnitude_lane2_1500]
		information3 = ["3", 1500, "3", time_headway_lane3_1500, space_headway_lane3_1500, speed_lane3_1500, magnitude_lane3_1500]
		informationT = ["3", 1500, "T", time_headway_total_1500, space_headway_total_1500, speed_total_1500, magnitude_total_1500]
	csvwrite.writerow(information0)
	csvwrite.writerow(information1)
	csvwrite.writerow(information2)
	csvwrite.writerow(information3)
	csvwrite.writerow(informationT)

	# Check_xpos: 3000
	# Time_headway
	pass_list = []
	time_headway_total_all = 0
	time_record_num_all = 0
	time_headway_total0 = 0
	time_record_num0 = 0
	time_headway_total1 = 0
	time_record_num1 = 0
	time_headway_total2 = 0
	time_record_num2 = 0
	time_headway_total3 = 0
	time_record_num3 = 0
	# Space_headway
	space_headway_total_all = 0
	space_record_num_all = 0
	space_headway_total0 = 0
	space_record_num0 = 0
	space_headway_total1 = 0
	space_record_num1 = 0
	space_headway_total2 = 0
	space_record_num2 = 0
	space_headway_total3 = 0
	space_record_num3 = 0
	# Speed
	speed_total_all = 0
	speed_record_num_all = 0
	speed_total0 = 0
	speed_record_num0 = 0
	speed_total1 = 0
	speed_record_num1 = 0
	speed_total2 = 0
	speed_record_num2 = 0
	speed_total3 = 0
	speed_record_num3 = 0
	# Magnitude
	magnitude_total_all = 0
	magnitude_total0 = 0
	magnitude_total1 = 0
	magnitude_total2 = 0
	magnitude_total3 = 0
	for find_num in range(0,csv_data.shape[0]):
		if csv_data.at[find_num,'id'] not in pass_list:
			if 3000 <= float(csv_data.at[find_num,'x']) + float(csv_data.at[find_num,'length'])/2 <= 3020:
				pass_list.append(csv_data.at[find_num,'id'])
				type_data = csv_data.at[find_num,'type']
				if -15 <= float(csv_data.at[find_num,'y']) < -11.25:
					speed_total0 += float(csv_data.at[find_num,'speed'])
					speed_record_num0 += 1
					if type_data[0] == 'R' or type_data[0] == 'G' or type_data[0] == 'E':
						magnitude_total0 += 1
					elif type_data[0] == 'B':
						magnitude_total0 += 1.5
					elif type_data[0] == 'T':
						magnitude_total0 += 2
				elif -11.25 <= float(csv_data.at[find_num,'y']) < -7.5:
					speed_total1 += float(csv_data.at[find_num,'speed'])
					speed_record_num1 += 1
					if type_data[0] == 'R' or type_data[0] == 'G' or type_data[0] == 'E':
						magnitude_total1 += 1
					elif type_data[0] == 'B':
						magnitude_total1 += 1.5
					elif type_data[0] == 'T':
						magnitude_total1 += 2
				elif -7.5 <= float(csv_data.at[find_num,'y']) < -3.75:
					speed_total2 += float(csv_data.at[find_num,'speed'])
					speed_record_num2 += 1
					if type_data[0] == 'R' or type_data[0] == 'G' or type_data[0] == 'E':
						magnitude_total2 += 1
					elif type_data[0] == 'B':
						magnitude_total2 += 1.5
					elif type_data[0] == 'T':
						magnitude_total2 += 2
				elif -3.75 <= float(csv_data.at[find_num,'y']) <= 0:
					speed_total3 += float(csv_data.at[find_num,'speed'])
					speed_record_num3 += 1
					if type_data[0] == 'R' or type_data[0] == 'G' or type_data[0] == 'E':
						magnitude_total3 += 1
					elif type_data[0] == 'B':
						magnitude_total3 += 1.5
					elif type_data[0] == 'T':
						magnitude_total3 += 2
				if str(csv_data.at[find_num,'follower_id']) != 'nan':
					for check_num in range(0,csv_data.shape[0]):
						if csv_data.at[check_num,'id'] == csv_data.at[find_num,'follower_id'] and csv_data.at[check_num,'time'] == csv_data.at[find_num,'time']:
							if -15 <= float(csv_data.at[find_num,'y']) < -11.25 and -15 <= float(csv_data.at[check_num,'y']) < -11.25:
								space_headway_total0 += (float(csv_data.at[find_num,'x']) - float(csv_data.at[check_num,'x']))
								space_record_num0 += 1
							elif -11.25 <= float(csv_data.at[find_num,'y']) < -7.5 and -11.25 <= float(csv_data.at[check_num,'y']) < -7.5:
								space_headway_total1 += (float(csv_data.at[find_num,'x']) - float(csv_data.at[check_num,'x']))
								space_record_num1 += 1
							elif -7.5 <= float(csv_data.at[find_num,'y']) < -3.75 and -7.5 <= float(csv_data.at[check_num,'y']) < -3.75:
								space_headway_total2 += (float(csv_data.at[find_num,'x']) - float(csv_data.at[check_num,'x']))
								space_record_num2 += 1
							elif -3.75 <= float(csv_data.at[find_num,'y']) <= 0 and -3.75 <= float(csv_data.at[check_num,'y']) <= 0:
								space_headway_total3 += (float(csv_data.at[find_num,'x']) - float(csv_data.at[check_num,'x']))
								space_record_num3 += 1
						if csv_data.at[check_num,'id'] == csv_data.at[find_num,'follower_id'] and 3000 <= float(csv_data.at[check_num,'x']) + float(csv_data.at[check_num,'length'])/2 <= 3020:
							if -15 <= float(csv_data.at[find_num,'y']) < -11.25 and -15 <= float(csv_data.at[check_num,'y']) < -11.25:
								time_headway_total0 += (float(csv_data.at[check_num,'time']) - float(csv_data.at[find_num,'time']))
								time_record_num0 += 1
								break
							elif -11.25 <= float(csv_data.at[find_num,'y']) < -7.5 and -11.25 <= float(csv_data.at[check_num,'y']) < -7.5:
								time_headway_total1 += (float(csv_data.at[check_num,'time']) - float(csv_data.at[find_num,'time']))
								time_record_num1 += 1
								break
							elif -7.5 <= float(csv_data.at[find_num,'y']) < -3.75 and -7.5 <= float(csv_data.at[check_num,'y']) < -3.75:
								time_headway_total2 += (float(csv_data.at[check_num,'time']) - float(csv_data.at[find_num,'time']))
								time_record_num2 += 1
								break
							elif -3.75 <= float(csv_data.at[find_num,'y']) <= 0 and -3.75 <= float(csv_data.at[check_num,'y']) <= 0:
								time_headway_total3 += (float(csv_data.at[check_num,'time']) - float(csv_data.at[find_num,'time']))
								time_record_num3 += 1
								break
							else:
								break
	time_headway_total_all = time_headway_total0 + time_headway_total1 + time_headway_total2 + time_headway_total3
	time_record_num_all = time_record_num0 + time_record_num1 + time_record_num2 + time_record_num3
	time_headway_total_3000 = time_headway_total_all/time_record_num_all
	time_headway_lane0_3000 = time_headway_total0/time_record_num0
	time_headway_lane1_3000 = time_headway_total1/time_record_num1
	time_headway_lane2_3000 = time_headway_total2/time_record_num2
	time_headway_lane3_3000 = time_headway_total3/time_record_num3
	space_headway_total_all = space_headway_total0 + space_headway_total1 + space_headway_total2 + space_headway_total3
	space_record_num_all = space_record_num0 + space_record_num1 + space_record_num2 + space_record_num3
	space_headway_total_3000 = space_headway_total_all/space_record_num_all
	space_headway_lane0_3000 = space_headway_total0/space_record_num0
	space_headway_lane1_3000 = space_headway_total1/space_record_num1
	space_headway_lane2_3000 = space_headway_total2/space_record_num2
	space_headway_lane3_3000 = space_headway_total3/space_record_num3
	speed_total_all = speed_total0 + speed_total1 + speed_total2 + speed_total3
	speed_record_num_all = speed_record_num0 + speed_record_num1 + speed_record_num2 + speed_record_num3
	speed_total_3000 = speed_total_all/speed_record_num_all
	speed_lane0_3000 = speed_total0/speed_record_num0
	speed_lane1_3000 = speed_total1/speed_record_num1
	speed_lane2_3000 = speed_total2/speed_record_num2
	speed_lane3_3000 = speed_total3/speed_record_num3
	magnitude_total_all = magnitude_total0 + magnitude_total1 + magnitude_total2 + magnitude_total3
	magnitude_total_3000 = magnitude_total_all
	magnitude_lane0_3000 = magnitude_total0
	magnitude_lane1_3000 = magnitude_total1
	magnitude_lane2_3000 = magnitude_total2
	magnitude_lane3_3000 = magnitude_total3
	print("time_headway_lane0_3000:", time_headway_lane0_3000) # 5.381818181818186
	print("time_headway_lane1_3000:", time_headway_lane1_3000) # 3.966666666666665
	print("time_headway_lane2_3000:", time_headway_lane2_3000) # 3.0012987012986994
	print("time_headway_lane3_3000:", time_headway_lane3_3000) # 3.0364406779661004
	print("time_headway_total_3000:", time_headway_total_3000) # 3.3760617760617753
	print("space_headway_lane0_3000:", space_headway_lane0_3000) # 
	print("space_headway_lane1_3000:", space_headway_lane1_3000) # 
	print("space_headway_lane2_3000:", space_headway_lane2_3000) # 
	print("space_headway_lane3_3000:", space_headway_lane3_3000) # 
	print("space_headway_total_3000:", space_headway_total_3000) # 
	print("speed_lane0_3000:", speed_lane0_3000) # 
	print("speed_lane1_3000:", speed_lane1_3000) # 
	print("speed_lane2_3000:", speed_lane2_3000) # 
	print("speed_lane3_3000:", speed_lane3_3000) # 
	print("speed_total_3000:", speed_total_3000) # 
	print("magnitude_lane0_3000:", magnitude_lane0_3000) # 
	print("magnitude_lane1_3000:", magnitude_lane1_3000) # 
	print("magnitude_lane2_3000:", magnitude_lane2_3000) # 
	print("magnitude_lane3_3000:", magnitude_lane3_3000) # 
	print("magnitude_total_3000:", magnitude_total_3000) # 
	
	if csv_num == 0:
		information0 = ["none", 3000, "0", time_headway_lane0_3000, space_headway_lane0_3000, speed_lane0_3000, magnitude_lane0_3000]
		information1 = ["none", 3000, "1", time_headway_lane1_3000, space_headway_lane1_3000, speed_lane1_3000, magnitude_lane1_3000]
		information2 = ["none", 3000, "2", time_headway_lane2_3000, space_headway_lane2_3000, speed_lane2_3000, magnitude_lane2_3000]
		information3 = ["none", 3000, "3", time_headway_lane3_3000, space_headway_lane3_3000, speed_lane3_3000, magnitude_lane3_3000]
		informationT = ["none", 3000, "T", time_headway_total_3000, space_headway_total_3000, speed_total_3000, magnitude_total_3000]
	elif csv_num == 1:
		information0 = ["0", 3000, "0", time_headway_lane0_3000, space_headway_lane0_3000, speed_lane0_3000, magnitude_lane0_3000]
		information1 = ["0", 3000, "1", time_headway_lane1_3000, space_headway_lane1_3000, speed_lane1_3000, magnitude_lane1_3000]
		information2 = ["0", 3000, "2", time_headway_lane2_3000, space_headway_lane2_3000, speed_lane2_3000, magnitude_lane2_3000]
		information3 = ["0", 3000, "3", time_headway_lane3_3000, space_headway_lane3_3000, speed_lane3_3000, magnitude_lane3_3000]
		informationT = ["0", 3000, "T", time_headway_total_3000, space_headway_total_3000, speed_total_3000, magnitude_total_3000]
	elif csv_num == 2:
		information0 = ["1", 3000, "0", time_headway_lane0_3000, space_headway_lane0_3000, speed_lane0_3000, magnitude_lane0_3000]
		information1 = ["1", 3000, "1", time_headway_lane1_3000, space_headway_lane1_3000, speed_lane1_3000, magnitude_lane1_3000]
		information2 = ["1", 3000, "2", time_headway_lane2_3000, space_headway_lane2_3000, speed_lane2_3000, magnitude_lane2_3000]
		information3 = ["1", 3000, "3", time_headway_lane3_3000, space_headway_lane3_3000, speed_lane3_3000, magnitude_lane3_3000]
		informationT = ["1", 3000, "T", time_headway_total_3000, space_headway_total_3000, speed_total_3000, magnitude_total_3000]
	elif csv_num == 3:
		information0 = ["2", 3000, "0", time_headway_lane0_3000, space_headway_lane0_3000, speed_lane0_3000, magnitude_lane0_3000]
		information1 = ["2", 3000, "1", time_headway_lane1_3000, space_headway_lane1_3000, speed_lane1_3000, magnitude_lane1_3000]
		information2 = ["2", 3000, "2", time_headway_lane2_3000, space_headway_lane2_3000, speed_lane2_3000, magnitude_lane2_3000]
		information3 = ["2", 3000, "3", time_headway_lane3_3000, space_headway_lane3_3000, speed_lane3_3000, magnitude_lane3_3000]
		informationT = ["2", 3000, "T", time_headway_total_3000, space_headway_total_3000, speed_total_3000, magnitude_total_3000]
	elif csv_num == 4:
		information0 = ["3", 3000, "0", time_headway_lane0_3000, space_headway_lane0_3000, speed_lane0_3000, magnitude_lane0_3000]
		information1 = ["3", 3000, "1", time_headway_lane1_3000, space_headway_lane1_3000, speed_lane1_3000, magnitude_lane1_3000]
		information2 = ["3", 3000, "2", time_headway_lane2_3000, space_headway_lane2_3000, speed_lane2_3000, magnitude_lane2_3000]
		information3 = ["3", 3000, "3", time_headway_lane3_3000, space_headway_lane3_3000, speed_lane3_3000, magnitude_lane3_3000]
		informationT = ["3", 3000, "T", time_headway_total_3000, space_headway_total_3000, speed_total_3000, magnitude_total_3000]
	csvwrite.writerow(information0)
	csvwrite.writerow(information1)
	csvwrite.writerow(information2)
	csvwrite.writerow(information3)
	csvwrite.writerow(informationT)

	# Check_xpos: 4500
	# Time_headway
	pass_list = []
	time_headway_total_all = 0
	time_record_num_all = 0
	time_headway_total0 = 0
	time_record_num0 = 0
	time_headway_total1 = 0
	time_record_num1 = 0
	time_headway_total2 = 0
	time_record_num2 = 0
	time_headway_total3 = 0
	time_record_num3 = 0
	# Space_headway
	space_headway_total_all = 0
	space_record_num_all = 0
	space_headway_total0 = 0
	space_record_num0 = 0
	space_headway_total1 = 0
	space_record_num1 = 0
	space_headway_total2 = 0
	space_record_num2 = 0
	space_headway_total3 = 0
	space_record_num3 = 0
	# Speed
	speed_total_all = 0
	speed_record_num_all = 0
	speed_total0 = 0
	speed_record_num0 = 0
	speed_total1 = 0
	speed_record_num1 = 0
	speed_total2 = 0
	speed_record_num2 = 0
	speed_total3 = 0
	speed_record_num3 = 0
	# Magnitude
	magnitude_total_all = 0
	magnitude_total0 = 0
	magnitude_total1 = 0
	magnitude_total2 = 0
	magnitude_total3 = 0
	for find_num in range(0,csv_data.shape[0]):
		if csv_data.at[find_num,'id'] not in pass_list:
			if 4500 <= float(csv_data.at[find_num,'x']) + float(csv_data.at[find_num,'length'])/2 <= 4520:
				pass_list.append(csv_data.at[find_num,'id'])
				type_data = csv_data.at[find_num,'type']
				if -15 <= float(csv_data.at[find_num,'y']) < -11.25:
					speed_total0 += float(csv_data.at[find_num,'speed'])
					speed_record_num0 += 1
					if type_data[0] == 'R' or type_data[0] == 'G' or type_data[0] == 'E':
						magnitude_total0 += 1
					elif type_data[0] == 'B':
						magnitude_total0 += 1.5
					elif type_data[0] == 'T':
						magnitude_total0 += 2
				elif -11.25 <= float(csv_data.at[find_num,'y']) < -7.5:
					speed_total1 += float(csv_data.at[find_num,'speed'])
					speed_record_num1 += 1
					if type_data[0] == 'R' or type_data[0] == 'G' or type_data[0] == 'E':
						magnitude_total1 += 1
					elif type_data[0] == 'B':
						magnitude_total1 += 1.5
					elif type_data[0] == 'T':
						magnitude_total1 += 2
				elif -7.5 <= float(csv_data.at[find_num,'y']) < -3.75:
					speed_total2 += float(csv_data.at[find_num,'speed'])
					speed_record_num2 += 1
					if type_data[0] == 'R' or type_data[0] == 'G' or type_data[0] == 'E':
						magnitude_total2 += 1
					elif type_data[0] == 'B':
						magnitude_total2 += 1.5
					elif type_data[0] == 'T':
						magnitude_total2 += 2
				elif -3.75 <= float(csv_data.at[find_num,'y']) <= 0:
					speed_total3 += float(csv_data.at[find_num,'speed'])
					speed_record_num3 += 1
					if type_data[0] == 'R' or type_data[0] == 'G' or type_data[0] == 'E':
						magnitude_total3 += 1
					elif type_data[0] == 'B':
						magnitude_total3 += 1.5
					elif type_data[0] == 'T':
						magnitude_total3 += 2
				if str(csv_data.at[find_num,'follower_id']) != 'nan':
					for check_num in range(0,csv_data.shape[0]):
						if csv_data.at[check_num,'id'] == csv_data.at[find_num,'follower_id'] and csv_data.at[check_num,'time'] == csv_data.at[find_num,'time']:
							if -15 <= float(csv_data.at[find_num,'y']) < -11.25 and -15 <= float(csv_data.at[check_num,'y']) < -11.25:
								space_headway_total0 += (float(csv_data.at[find_num,'x']) - float(csv_data.at[check_num,'x']))
								space_record_num0 += 1
							elif -11.25 <= float(csv_data.at[find_num,'y']) < -7.5 and -11.25 <= float(csv_data.at[check_num,'y']) < -7.5:
								space_headway_total1 += (float(csv_data.at[find_num,'x']) - float(csv_data.at[check_num,'x']))
								space_record_num1 += 1
							elif -7.5 <= float(csv_data.at[find_num,'y']) < -3.75 and -7.5 <= float(csv_data.at[check_num,'y']) < -3.75:
								space_headway_total2 += (float(csv_data.at[find_num,'x']) - float(csv_data.at[check_num,'x']))
								space_record_num2 += 1
							elif -3.75 <= float(csv_data.at[find_num,'y']) <= 0 and -3.75 <= float(csv_data.at[check_num,'y']) <= 0:
								space_headway_total3 += (float(csv_data.at[find_num,'x']) - float(csv_data.at[check_num,'x']))
								space_record_num3 += 1
						if csv_data.at[check_num,'id'] == csv_data.at[find_num,'follower_id'] and 4500 <= float(csv_data.at[check_num,'x']) + float(csv_data.at[check_num,'length'])/2 <= 4520:
							if -15 <= float(csv_data.at[find_num,'y']) < -11.25 and -15 <= float(csv_data.at[check_num,'y']) < -11.25:
								time_headway_total0 += (float(csv_data.at[check_num,'time']) - float(csv_data.at[find_num,'time']))
								time_record_num0 += 1
								break
							elif -11.25 <= float(csv_data.at[find_num,'y']) < -7.5 and -11.25 <= float(csv_data.at[check_num,'y']) < -7.5:
								time_headway_total1 += (float(csv_data.at[check_num,'time']) - float(csv_data.at[find_num,'time']))
								time_record_num1 += 1
								break
							elif -7.5 <= float(csv_data.at[find_num,'y']) < -3.75 and -7.5 <= float(csv_data.at[check_num,'y']) < -3.75:
								time_headway_total2 += (float(csv_data.at[check_num,'time']) - float(csv_data.at[find_num,'time']))
								time_record_num2 += 1
								break
							elif -3.75 <= float(csv_data.at[find_num,'y']) <= 0 and -3.75 <= float(csv_data.at[check_num,'y']) <= 0:
								time_headway_total3 += (float(csv_data.at[check_num,'time']) - float(csv_data.at[find_num,'time']))
								time_record_num3 += 1
								break
							else:
								break
	time_headway_total_all = time_headway_total0 + time_headway_total1 + time_headway_total2 + time_headway_total3
	time_record_num_all = time_record_num0 + time_record_num1 + time_record_num2 + time_record_num3
	time_headway_total_4500 = time_headway_total_all/time_record_num_all
	time_headway_lane0_4500 = time_headway_total0/time_record_num0
	time_headway_lane1_4500 = time_headway_total1/time_record_num1
	time_headway_lane2_4500 = time_headway_total2/time_record_num2
	time_headway_lane3_4500 = time_headway_total3/time_record_num3
	space_headway_total_all = space_headway_total0 + space_headway_total1 + space_headway_total2 + space_headway_total3
	space_record_num_all = space_record_num0 + space_record_num1 + space_record_num2 + space_record_num3
	space_headway_total_4500 = space_headway_total_all/space_record_num_all
	space_headway_lane0_4500 = space_headway_total0/space_record_num0
	space_headway_lane1_4500 = space_headway_total1/space_record_num1
	space_headway_lane2_4500 = space_headway_total2/space_record_num2
	space_headway_lane3_4500 = space_headway_total3/space_record_num3
	speed_total_all = speed_total0 + speed_total1 + speed_total2 + speed_total3
	speed_record_num_all = speed_record_num0 + speed_record_num1 + speed_record_num2 + speed_record_num3
	speed_total_4500 = speed_total_all/speed_record_num_all
	speed_lane0_4500 = speed_total0/speed_record_num0
	speed_lane1_4500 = speed_total1/speed_record_num1
	speed_lane2_4500 = speed_total2/speed_record_num2
	speed_lane3_4500 = speed_total3/speed_record_num3
	magnitude_total_all = magnitude_total0 + magnitude_total1 + magnitude_total2 + magnitude_total3
	magnitude_total_4500 = magnitude_total_all
	magnitude_lane0_4500 = magnitude_total0
	magnitude_lane1_4500 = magnitude_total1
	magnitude_lane2_4500 = magnitude_total2
	magnitude_lane3_4500 = magnitude_total3
	print("time_headway_lane0_4500:", time_headway_lane0_4500) # 6.826666666666665
	print("time_headway_lane1_4500:", time_headway_lane1_4500) # 4.019047619047618
	print("time_headway_lane2_4500:", time_headway_lane2_4500) # 3.134722222222221
	print("time_headway_lane3_4500:", time_headway_lane3_4500) # 3.027358490566037
	print("time_headway_total_4500:", time_headway_total_4500) # 3.4799999999999986
	print("space_headway_lane0_4500:", space_headway_lane0_4500) # 
	print("space_headway_lane1_4500:", space_headway_lane1_4500) # 
	print("space_headway_lane2_4500:", space_headway_lane2_4500) # 
	print("space_headway_lane3_4500:", space_headway_lane3_4500) # 
	print("space_headway_total_4500:", space_headway_total_4500) # 
	print("speed_lane0_4500:", speed_lane0_4500) # 
	print("speed_lane1_4500:", speed_lane1_4500) # 
	print("speed_lane2_4500:", speed_lane2_4500) # 
	print("speed_lane3_4500:", speed_lane3_4500) # 
	print("speed_total_4500:", speed_total_4500) # 
	print("magnitude_lane0_4500:", magnitude_lane0_4500) # 
	print("magnitude_lane1_4500:", magnitude_lane1_4500) # 
	print("magnitude_lane2_4500:", magnitude_lane2_4500) # 
	print("magnitude_lane3_4500:", magnitude_lane3_4500) # 
	print("magnitude_total_4500:", magnitude_total_4500) # 

	if csv_num == 0:
		information0 = ["none", 4500, "0", time_headway_lane0_4500, space_headway_lane0_4500, speed_lane0_4500, magnitude_lane0_4500]
		information1 = ["none", 4500, "1", time_headway_lane1_4500, space_headway_lane1_4500, speed_lane1_4500, magnitude_lane1_4500]
		information2 = ["none", 4500, "2", time_headway_lane2_4500, space_headway_lane2_4500, speed_lane2_4500, magnitude_lane2_4500]
		information3 = ["none", 4500, "3", time_headway_lane3_4500, space_headway_lane3_4500, speed_lane3_4500, magnitude_lane3_4500]
		informationT = ["none", 4500, "T", time_headway_total_4500, space_headway_total_4500, speed_total_4500, magnitude_total_4500]
	elif csv_num == 1:
		information0 = ["0", 4500, "0", time_headway_lane0_4500, space_headway_lane0_4500, speed_lane0_4500, magnitude_lane0_4500]
		information1 = ["0", 4500, "1", time_headway_lane1_4500, space_headway_lane1_4500, speed_lane1_4500, magnitude_lane1_4500]
		information2 = ["0", 4500, "2", time_headway_lane2_4500, space_headway_lane2_4500, speed_lane2_4500, magnitude_lane2_4500]
		information3 = ["0", 4500, "3", time_headway_lane3_4500, space_headway_lane3_4500, speed_lane3_4500, magnitude_lane3_4500]
		informationT = ["0", 4500, "T", time_headway_total_4500, space_headway_total_4500, speed_total_4500, magnitude_total_4500]
	elif csv_num == 2:
		information0 = ["1", 4500, "0", time_headway_lane0_4500, space_headway_lane0_4500, speed_lane0_4500, magnitude_lane0_4500]
		information1 = ["1", 4500, "1", time_headway_lane1_4500, space_headway_lane1_4500, speed_lane1_4500, magnitude_lane1_4500]
		information2 = ["1", 4500, "2", time_headway_lane2_4500, space_headway_lane2_4500, speed_lane2_4500, magnitude_lane2_4500]
		information3 = ["1", 4500, "3", time_headway_lane3_4500, space_headway_lane3_4500, speed_lane3_4500, magnitude_lane3_4500]
		informationT = ["1", 4500, "T", time_headway_total_4500, space_headway_total_4500, speed_total_4500, magnitude_total_4500]
	elif csv_num == 3:
		information0 = ["2", 4500, "0", time_headway_lane0_4500, space_headway_lane0_4500, speed_lane0_4500, magnitude_lane0_4500]
		information1 = ["2", 4500, "1", time_headway_lane1_4500, space_headway_lane1_4500, speed_lane1_4500, magnitude_lane1_4500]
		information2 = ["2", 4500, "2", time_headway_lane2_4500, space_headway_lane2_4500, speed_lane2_4500, magnitude_lane2_4500]
		information3 = ["2", 4500, "3", time_headway_lane3_4500, space_headway_lane3_4500, speed_lane3_4500, magnitude_lane3_4500]
		informationT = ["2", 4500, "T", time_headway_total_4500, space_headway_total_4500, speed_total_4500, magnitude_total_4500]
	elif csv_num == 4:
		information0 = ["3", 4500, "0", time_headway_lane0_4500, space_headway_lane0_4500, speed_lane0_4500, magnitude_lane0_4500]
		information1 = ["3", 4500, "1", time_headway_lane1_4500, space_headway_lane1_4500, speed_lane1_4500, magnitude_lane1_4500]
		information2 = ["3", 4500, "2", time_headway_lane2_4500, space_headway_lane2_4500, speed_lane2_4500, magnitude_lane2_4500]
		information3 = ["3", 4500, "3", time_headway_lane3_4500, space_headway_lane3_4500, speed_lane3_4500, magnitude_lane3_4500]
		informationT = ["3", 4500, "T", time_headway_total_4500, space_headway_total_4500, speed_total_4500, magnitude_total_4500]
	csvwrite.writerow(information0)
	csvwrite.writerow(information1)
	csvwrite.writerow(information2)
	csvwrite.writerow(information3)
	csvwrite.writerow(informationT)

csvfile.close()