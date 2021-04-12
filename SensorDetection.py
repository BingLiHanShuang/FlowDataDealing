import csv
import os
import numpy as np
#import math
import random
import pandas as pd

PI = 3.1415
rl_car = {'length': 4.552, 'width': 1.864, 'height': 1.654}# Lincoln MKC 4552*1864*1654
human_carGas = {'length': 4.670, 'width': 1.806, 'height': 1.474}# Volkswagen LAVIDA 4670*1806*1474 max:120km/h
human_carEle = {'length': 4.694, 'width': 1.850, 'height': 1.443}# Tesla Model3(CN) 4694*1850*1443 max:120km/h
human_bus = {'length': 7.148, 'width': 2.075, 'height': 2.770}# YUTONG T7 7148*2075*2770 max:120km/h
human_truck = {'length': 11.600, 'width': 2.550, 'height': 3.400}# SINOTRUK HOWO-A7-8*4 11600*2550*3400 max:100km/h
InAreaPointPos = [[-0.5,-0.5],[0,-0.5],[-0.5,0.5],[-0.167,0.5],[0.167,0.5],[0.5,0.5],[0.5,0],[0.5,-0.5],[0.167,-0.5],[-0.167,-0.5]]
small_CarPointPosition = [[-0.5,-0.5,0.5],[-0.5,0.5,0.5],[0,0.5,1],[0.5,0.5,0.5],[0.5,-0.5,0.5],[0,-0.5,1],[-0.5,-0.5,0],[-0.5,0.5,0],[0,0.5,0],[0.5,0.5,0],[0.5,-0.5,0],[0,-0.5,0]]
large_CarPointPosition = [[-0.5,-0.5,1],[-0.5,0.5,1],[0,0.5,1],[0.5,0.5,1],[0.5,-0.5,1],[0,-0.5,1],[-0.5,-0.5,0],[-0.5,0.5,0],[0,0.5,0],[0.5,0.5,0],[0.5,-0.5,0],[0,-0.5,0]]

#100m Round and 150m long-focus 50 degree ahead; height:1.8m
def VisionDetector(csv_data, rl_x, rl_y, target_id, target_type, target_x, target_y, target_length, target_width, target_height, quadrant, block_id, block_type, block_x, block_y, block_length, block_width, block_height):
	block_Angle2Ahead_group = []
	block_Distance_group = []
	block_Distance_Proportion_group = []
	target_Angle2Ahead_group = []
	target_Distance_Proportion_group = []
	target_DistanceDirect_group = []
	target_Distance_group = []
	for i in range(12):
		if block_type[0] == 'R':# Rlcar
			point_x = block_x + small_CarPointPosition[i][0]*block_length
			point_y = block_y + small_CarPointPosition[i][1]*block_width
			point_z = small_CarPointPosition[i][2]*block_height
		elif block_type[0] == 'G':# Gashumancar
			point_x = block_x + small_CarPointPosition[i][0]*block_length
			point_y = block_y + small_CarPointPosition[i][1]*block_width
			point_z = small_CarPointPosition[i][2]*block_height
		elif block_type[0] == 'E':# Elehumancar
			point_x = block_x + small_CarPointPosition[i][0]*block_length
			point_y = block_y + small_CarPointPosition[i][1]*block_width
			point_z = small_CarPointPosition[i][2]*block_height
		elif block_type[0] == 'B':# Bushuman
			point_x = block_x + large_CarPointPosition[i][0]*block_length
			point_y = block_y + large_CarPointPosition[i][1]*block_width
			point_z = large_CarPointPosition[i][2]*block_height
		elif block_type[0] == 'T':# Truckhuman
			point_x = block_x + large_CarPointPosition[i][0]*block_length
			point_y = block_y + large_CarPointPosition[i][1]*block_width
			point_z = large_CarPointPosition[i][2]*block_height
		distance = pow(pow((rl_x - point_x),2) + pow((rl_y - point_y),2), 0.5)
		if rl_y == point_y and rl_x > point_x:#rl ahead
			block_Angle2Ahead = PI
		elif rl_y == point_y and rl_x < point_x:#rl behind
			block_Angle2Ahead = 0
		elif rl_y > point_y and rl_x <= point_x:#target I Quadrant
			block_Angle2Ahead = 0.00 + np.arcsin(float(abs(point_y - rl_y))/distance)
		elif rl_y > point_y and rl_x > point_x:#target II Quadrant
			block_Angle2Ahead = PI - np.arcsin(float(abs(point_y - rl_y))/distance)
		elif rl_y < point_y and rl_x >= point_x:#target III Quadrant
			block_Angle2Ahead = PI + np.arcsin(float(abs(point_y - rl_y))/distance)
		elif rl_y < point_y and rl_x < point_x:#target IV Quadrant
			block_Angle2Ahead = 2*PI - np.arcsin(float(abs(point_y - rl_y))/distance)
		block_Distance = distance
		block_Distance_Proportion = (point_z - 1.8)/distance
		block_Angle2Ahead_group.append(block_Angle2Ahead)
		block_Distance_group.append(block_Distance)
		block_Distance_Proportion_group.append(block_Distance_Proportion)
	
	for i in range(12):
		if target_type[0] == 'R':# Rlcar
			point_x = target_x + small_CarPointPosition[i][0]*target_length
			point_y = target_y + small_CarPointPosition[i][1]*target_width
			point_z = small_CarPointPosition[i][2]*target_height
		elif target_type[0] == 'G':# Gashumancar
			point_x = target_x + small_CarPointPosition[i][0]*target_length
			point_y = target_y + small_CarPointPosition[i][1]*target_width
			point_z = small_CarPointPosition[i][2]*target_height
		elif target_type[0] == 'E':# Elehumancar
			point_x = target_x + small_CarPointPosition[i][0]*target_length
			point_y = target_y + small_CarPointPosition[i][1]*target_width
			point_z = small_CarPointPosition[i][2]*target_height
		elif target_type[0] == 'B':# Bushuman
			point_x = target_x + large_CarPointPosition[i][0]*target_length
			point_y = target_y + large_CarPointPosition[i][1]*target_width
			point_z = large_CarPointPosition[i][2]*target_height
		elif target_type[0] == 'T':# Truckhuman
			point_x = target_x + large_CarPointPosition[i][0]*target_length
			point_y = target_y + large_CarPointPosition[i][1]*target_width
			point_z = large_CarPointPosition[i][2]*target_height
		distance = pow(pow((rl_x - point_x),2) + pow((rl_y - point_y),2), 0.5)
		distance_direct = pow(pow((rl_x - point_x),2) + pow((rl_y - point_y),2) + pow((1.8 - point_z),2), 0.5)
		if rl_y == point_y and rl_x > point_x:#rl ahead
			target_Angle2Ahead = PI
		elif rl_y == point_y and rl_x < point_x:#rl behind
			target_Angle2Ahead = 0
		elif rl_y > point_y and rl_x <= point_x:#target I Quadrant
			target_Angle2Ahead = 0.00 + np.arcsin(float(abs(point_y - rl_y))/distance)
		elif rl_y > point_y and rl_x > point_x:#target II Quadrant
			target_Angle2Ahead = PI - np.arcsin(float(abs(point_y - rl_y))/distance)
		elif rl_y < point_y and rl_x >= point_x:#target III Quadrant
			target_Angle2Ahead = PI + np.arcsin(float(abs(point_y - rl_y))/distance)
		elif rl_y < point_y and rl_x < point_x:#target IV Quadrant
			target_Angle2Ahead = 2*PI - np.arcsin(float(abs(point_y - rl_y))/distance)
		target_Distance_Proportion = (point_z - 1.8)/distance
		target_Angle2Ahead_group.append(target_Angle2Ahead)
		target_Distance_Proportion_group.append(target_Distance_Proportion)
		target_DistanceDirect_group.append(distance_direct)
		target_Distance_group.append(distance)
	
	#BLocked by own point? Angle2Ahead inside(a,b) + distance far than a,b
	detected_point_blockcar = []
	for i in range(12):
		be_blocked = 0
		for j in range(12):
			if i == j:
				continue
			for k in range(12):
				if i == k or j == k:
					continue
				if block_Angle2Ahead_group[i] > block_Angle2Ahead_group[j] and block_Angle2Ahead_group[i] < block_Angle2Ahead_group[k] and block_Distance_group[i] > block_Distance_group[j] and block_Distance_group[i] > block_Distance_group[k]:
					be_blocked = 1
		if be_blocked == 0:
			detected_point_blockcar.append(i)
	
	detected_point_targetcar_ori = []
	for i in range(12):
		be_blocked = 0
		for j in range(12):
			if i == j:
				continue
			for k in range(12):
				if i == k or j == k:
					continue
				if target_Angle2Ahead_group[i] > target_Angle2Ahead_group[j] and target_Angle2Ahead_group[i] < target_Angle2Ahead_group[k] and target_Distance_group[i] > target_Distance_group[j] and target_Distance_group[i] > target_Distance_group[k]:
					be_blocked = 1
		if be_blocked == 0:
			detected_point_targetcar_ori.append(i)
	
	#Blocked by blockcar point?
	detected_point_targetcar = []
	for i in range(len(detected_point_targetcar_ori)):
		be_blocked = 0
		for j in range(len(detected_point_blockcar)):
			for k in range(len(detected_point_blockcar)):
				if j == k:
					continue
				if target_Angle2Ahead_group[detected_point_targetcar_ori[i]] >= block_Angle2Ahead_group[detected_point_blockcar[j]] and target_Angle2Ahead_group[detected_point_targetcar_ori[i]] <= block_Angle2Ahead_group[detected_point_blockcar[k]] and target_Distance_Proportion_group[detected_point_targetcar_ori[i]] <= block_Distance_Proportion_group[detected_point_blockcar[j]] and target_Distance_Proportion_group[detected_point_targetcar_ori[i]] <= block_Distance_Proportion_group[detected_point_blockcar[k]]:
					be_blocked = 1
		#if be_blocked == 0 and target_id == "flow_1.118" and block_id == "flow_3.4":
			#print("here")
		if be_blocked == 0 and (target_DistanceDirect_group[detected_point_targetcar_ori[i]] <= 100 or (target_DistanceDirect_group[detected_point_targetcar_ori[i]] <= 150 and (target_Angle2Ahead_group[detected_point_targetcar_ori[i]] <= 25/180*PI or target_Angle2Ahead_group[detected_point_targetcar_ori[i]] >= (2*PI-25/180*PI)))):
			detected_point_targetcar.append(detected_point_targetcar_ori[i])
	
	#if len(detected_point_targetcar)>=4:
		#print(len(detected_point_targetcar))
	'''
	if target_id == "flow_1.118" and block_id == "flow_3.4":# Use for test
		print(target_Angle2Ahead_group)
		print(block_Angle2Ahead_group)
		print(target_DistanceDirect_group)
		print(len(detected_point_blockcar))
		print(len(detected_point_targetcar_ori))
		print(len(detected_point_targetcar))
	'''
	
	return len(detected_point_targetcar)

#120m Velodyne HDL-64E; height:2m
def LidarDetector(csv_data, rl_x, rl_y, target_id, target_type, target_x, target_y, target_length, target_width, target_height, quadrant, block_id, block_type, block_x, block_y, block_length, block_width, block_height):
	block_Angle2Ahead_group = []
	block_Distance_group = []
	block_Distance_Proportion_group = []
	target_Angle2Ahead_group = []
	target_Distance_Proportion_group = []
	target_DistanceDirect_group = []
	target_Distance_group = []
	for i in range(12):
		if block_type[0] == 'R':# Rlcar
			point_x = block_x + small_CarPointPosition[i][0]*block_length
			point_y = block_y + small_CarPointPosition[i][1]*block_width
			point_z = small_CarPointPosition[i][2]*block_height
		elif block_type[0] == 'G':# Gashumancar
			point_x = block_x + small_CarPointPosition[i][0]*block_length
			point_y = block_y + small_CarPointPosition[i][1]*block_width
			point_z = small_CarPointPosition[i][2]*block_height
		elif block_type[0] == 'E':# Elehumancar
			point_x = block_x + small_CarPointPosition[i][0]*block_length
			point_y = block_y + small_CarPointPosition[i][1]*block_width
			point_z = small_CarPointPosition[i][2]*block_height
		elif block_type[0] == 'B':# Bushuman
			point_x = block_x + large_CarPointPosition[i][0]*block_length
			point_y = block_y + large_CarPointPosition[i][1]*block_width
			point_z = large_CarPointPosition[i][2]*block_height
		elif block_type[0] == 'T':# Truckhuman
			point_x = block_x + large_CarPointPosition[i][0]*block_length
			point_y = block_y + large_CarPointPosition[i][1]*block_width
			point_z = large_CarPointPosition[i][2]*block_height
		distance = pow(pow((rl_x - point_x),2) + pow((rl_y - point_y),2), 0.5)
		if rl_y == point_y and rl_x > point_x:#rl ahead
			block_Angle2Ahead = PI
		elif rl_y == point_y and rl_x < point_x:#rl behind
			block_Angle2Ahead = 0
		elif rl_y > point_y and rl_x <= point_x:#target I Quadrant
			block_Angle2Ahead = 0.00 + np.arcsin(float(abs(point_y - rl_y))/distance)
		elif rl_y > point_y and rl_x > point_x:#target II Quadrant
			block_Angle2Ahead = PI - np.arcsin(float(abs(point_y - rl_y))/distance)
		elif rl_y < point_y and rl_x >= point_x:#target III Quadrant
			block_Angle2Ahead = PI + np.arcsin(float(abs(point_y - rl_y))/distance)
		elif rl_y < point_y and rl_x < point_x:#target IV Quadrant
			block_Angle2Ahead = 2*PI - np.arcsin(float(abs(point_y - rl_y))/distance)
		block_Distance = distance
		block_Distance_Proportion = (point_z - 1.8)/distance
		block_Angle2Ahead_group.append(block_Angle2Ahead)
		block_Distance_group.append(block_Distance)
		block_Distance_Proportion_group.append(block_Distance_Proportion)
	
	for i in range(12):
		if target_type[0] == 'R':# Rlcar
			point_x = target_x + small_CarPointPosition[i][0]*target_length
			point_y = target_y + small_CarPointPosition[i][1]*target_width
			#point_z = small_CarPointPosition[i][2]*target_height
		elif target_type[0] == 'G':# Gashumancar
			point_x = target_x + small_CarPointPosition[i][0]*target_length
			point_y = target_y + small_CarPointPosition[i][1]*target_width
			#point_z = small_CarPointPosition[i][2]*target_height
		elif target_type[0] == 'E':# Elehumancar
			point_x = target_x + small_CarPointPosition[i][0]*target_length
			point_y = target_y + small_CarPointPosition[i][1]*target_width
			#point_z = small_CarPointPosition[i][2]*target_height
		elif target_type[0] == 'B':# Bushuman
			point_x = target_x + large_CarPointPosition[i][0]*target_length
			point_y = target_y + large_CarPointPosition[i][1]*target_width
			#point_z = large_CarPointPosition[i][2]*target_height
		elif target_type[0] == 'T':# Truckhuman
			point_x = target_x + large_CarPointPosition[i][0]*target_length
			point_y = target_y + large_CarPointPosition[i][1]*target_width
			#point_z = large_CarPointPosition[i][2]*target_height
		distance = pow(pow((rl_x - point_x),2) + pow((rl_y - point_y),2), 0.5)
		
		if target_type[0] == 'R' or target_type[0] == 'G' or target_type[0] == 'E':# Rlcar Gashumancar Elehumancar
			if (small_CarPointPosition[i][2]*target_height-2.0)/distance > 1 or (small_CarPointPosition[i][2]*target_height-2.0)/distance < -1:
				print(small_CarPointPosition[i][2]*target_height-2.0)
				print(distance)
			if np.arcsin((small_CarPointPosition[i][2]*target_height-2.0)/distance) > 2/180*PI:
				point_z = distance*np.arctan(2/180*PI) + 2.0
			if np.arcsin((small_CarPointPosition[i][2]*target_height-2.0)/distance) < -24.9/180*PI:
				point_z = 2.0 - distance*np.arctan(24.9/180*PI)
		elif target_type[0] == 'B' or target_type[0] == 'T':# Bushuman Truckhuman
			if np.arcsin((large_CarPointPosition[i][2]*target_height-2.0)/distance) > 2/180*PI:
				point_z = distance*np.arctan(2/180*PI) + 2.0
			if np.arcsin((large_CarPointPosition[i][2]*target_height-2.0)/distance) < -24.9/180*PI:
				point_z = 2.0 - distance*np.arctan(24.9/180*PI)
			#point_z = large_CarPointPosition[i][2]*target_height
		
		distance_direct = pow(pow((rl_x - point_x),2) + pow((rl_y - point_y),2) + pow((2.0 - point_z),2), 0.5)
		if rl_y == point_y and rl_x > point_x:#rl ahead
			target_Angle2Ahead = PI
		elif rl_y == point_y and rl_x < point_x:#rl behind
			target_Angle2Ahead = 0
		elif rl_y > point_y and rl_x <= point_x:#target I Quadrant
			target_Angle2Ahead = 0.00 + np.arcsin(float(abs(point_y - rl_y))/distance)
		elif rl_y > point_y and rl_x > point_x:#target II Quadrant
			target_Angle2Ahead = PI - np.arcsin(float(abs(point_y - rl_y))/distance)
		elif rl_y < point_y and rl_x >= point_x:#target III Quadrant
			target_Angle2Ahead = PI + np.arcsin(float(abs(point_y - rl_y))/distance)
		elif rl_y < point_y and rl_x < point_x:#target IV Quadrant
			target_Angle2Ahead = 2*PI - np.arcsin(float(abs(point_y - rl_y))/distance)
		target_Distance_Proportion = (point_z - 1.8)/distance
		target_Angle2Ahead_group.append(target_Angle2Ahead)
		target_Distance_Proportion_group.append(target_Distance_Proportion)
		target_DistanceDirect_group.append(distance_direct)
		target_Distance_group.append(distance)
	
	#BLocked by own point? Angle2Ahead inside(a,b) + distance far than a,b
	detected_point_blockcar = []
	for i in range(12):
		be_blocked = 0
		for j in range(12):
			if i == j:
				continue
			for k in range(12):
				if i == k or j == k:
					continue
				if block_Angle2Ahead_group[i] > block_Angle2Ahead_group[j] and block_Angle2Ahead_group[i] < block_Angle2Ahead_group[k] and block_Distance_group[i] > block_Distance_group[j] and block_Distance_group[i] > block_Distance_group[k]:
					be_blocked = 1
		if be_blocked == 0:
			detected_point_blockcar.append(i)
	
	detected_point_targetcar_ori = []
	for i in range(12):
		be_blocked = 0
		for j in range(12):
			if i == j:
				continue
			for k in range(12):
				if i == k or j == k:
					continue
				if target_Angle2Ahead_group[i] > target_Angle2Ahead_group[j] and target_Angle2Ahead_group[i] < target_Angle2Ahead_group[k] and target_Distance_group[i] > target_Distance_group[j] and target_Distance_group[i] > target_Distance_group[k]:
					be_blocked = 1
		if be_blocked == 0:
			detected_point_targetcar_ori.append(i)
	
	#Blocked by blockcar point?
	detected_point_targetcar = []
	for i in range(len(detected_point_targetcar_ori)):
		be_blocked = 0
		for j in range(len(detected_point_blockcar)):
			for k in range(len(detected_point_blockcar)):
				if j == k:
					continue
				if target_Angle2Ahead_group[detected_point_targetcar_ori[i]] >= block_Angle2Ahead_group[detected_point_blockcar[j]] and target_Angle2Ahead_group[detected_point_targetcar_ori[i]] <= block_Angle2Ahead_group[detected_point_blockcar[k]] and target_Distance_Proportion_group[detected_point_targetcar_ori[i]] <= block_Distance_Proportion_group[detected_point_blockcar[j]] and target_Distance_Proportion_group[detected_point_targetcar_ori[i]] <= block_Distance_Proportion_group[detected_point_blockcar[k]]:
					be_blocked = 1
		if be_blocked == 0 and (target_DistanceDirect_group[detected_point_targetcar_ori[i]] <= 120):
			detected_point_targetcar.append(detected_point_targetcar_ori[i])
	
	return len(detected_point_targetcar)


def WillVehicleBlock(csv_data, rl_x, rl_y, target_id, target_type, target_x, target_y, quadrant, block_id, block_type, block_x, block_y):
	if block_type[0] == 'R':# Rlcar
		block_length = rl_car['length']
		block_width = rl_car['width']
		block_height = rl_car['height']
	elif block_type[0] == 'G':# Gashumancar
		block_length = human_carGas['length']
		block_width = human_carGas['width']
		block_height = human_carGas['height']
	elif block_type[0] == 'E':# Elehumancar
		block_length = human_carEle['length']
		block_width = human_carEle['width']
		block_height = human_carEle['height']
	elif block_type[0] == 'B':# Bushuman
		block_length = human_bus['length']
		block_width = human_bus['width']
		block_height = human_bus['height']
	elif block_type[0] == 'T':# Truckhuman
		block_length = human_truck['length']
		block_width = human_truck['width']
		block_height = human_truck['height']
		
	if target_type[0] == 'R':# Rlcar
		target_length = rl_car['length']
		target_width = rl_car['width']
		target_height = rl_car['height']
	elif target_type[0] == 'G':# Gashumancar
		target_length = human_carGas['length']
		target_width = human_carGas['width']
		target_height = human_carGas['height']
	elif target_type[0] == 'E':# Elehumancar
		target_length = human_carEle['length']
		target_width = human_carEle['width']
		target_height = human_carEle['height']
	elif target_type[0] == 'B':# Bushuman
		target_length = human_bus['length']
		target_width = human_bus['width']
		target_height = human_bus['height']
	elif target_type[0] == 'T':# Truckhuman
		target_length = human_truck['length']
		target_width = human_truck['width']
		target_height = human_truck['height']
	
	vision_point = VisionDetector(csv_data, rl_x, rl_y, target_id, target_type, target_x, target_y, target_length, target_width, target_height, quadrant, block_id, block_type, block_x, block_y, block_length, block_width, block_height)
	lidar_point = LidarDetector(csv_data, rl_x, rl_y, target_id, target_type, target_x, target_y, target_length, target_width, target_height, quadrant, block_id, block_type, block_x, block_y, block_length, block_width, block_height)
	
	
	
	if vision_point >= 4 or lidar_point >= 4 or (vision_point >= 3 and lidar_point >= 3):
		return 1, vision_point, lidar_point
	elif vision_point == 3 or lidar_point == 3 or (vision_point == 2 and lidar_point == 2):
		return 0, vision_point, lidar_point
	else:
		#if target_id == "flow_1.118":
			#print(block_id)
			#print(block_type, block_x, block_y)
		return -1, vision_point, lidar_point


def IsVehicleInsideArea(csv_data, runtime, rl_x, rl_y, angle_to_ahead, target_id, target_type, target_x, target_y, target_length, quadrant):#rl_x:3000m-4500m target_x:4730m-6000m
	block_result = 1
	vision_point = 99
	lidar_point = 99
	for find_num in range(0,csv_data.shape[0]):
		block_happen = 0
		find_id = csv_data[find_num][0]
		find_type = csv_data[find_num][1]
		if find_type[0] == 'R':# Rlcar
			find_length = rl_car['length']
			find_width = rl_car['width']
			#find_height = rl_car['height']
		elif find_type[0] == 'G':# Gashumancar
			find_length = human_carGas['length']
			find_width = human_carGas['width']
			#find_height = human_carGas['height']
		elif find_type[0] == 'E':# Elehumancar
			find_length = human_carEle['length']
			find_width = human_carEle['width']
			#find_height = human_carEle['height']
		elif find_type[0] == 'B':# Bushuman
			find_length = human_bus['length']
			find_width = human_bus['width']
			#find_height = human_bus['height']
		elif find_type[0] == 'T':# Truckhuman
			find_length = human_truck['length']
			find_width = human_truck['width']
			#find_height = human_truck['height']
		find_x = float(csv_data[find_num][3]) - 0.5*find_length
		find_y = float(csv_data[find_num][4])
		if csv_data[find_num][0] != target_id:
			if quadrant == 1: 
				for i in range(10):
					point_x = find_x + InAreaPointPos[i][0]*find_length
					point_y = find_y + InAreaPointPos[i][1]*find_width
					if point_y <= rl_y and point_y >= target_y and point_x >= min(rl_x,target_x-0.5*target_length) and point_x <= target_x+0.5*target_length:
						block_happen = 1
			elif quadrant == 2:
				for i in range(10):
					point_x = find_x + InAreaPointPos[i][0]*find_length
					point_y = find_y + InAreaPointPos[i][1]*find_width
					if point_y <= rl_y and point_y >= target_y and point_x >= target_x-0.5*target_length and point_x <= max(rl_x,target_x+0.5*target_length):
						block_happen = 1
			elif quadrant == 3:
				for i in range(10):
					point_x = find_x + InAreaPointPos[i][0]*find_length
					point_y = find_y + InAreaPointPos[i][1]*find_width
					if point_y >= rl_y and point_y <= target_y and point_x >= target_x-0.5*target_length and point_x <= max(rl_x,target_x+0.5*target_length):
						block_happen = 1
			elif quadrant == 4:
				for i in range(10):
					point_x = find_x + InAreaPointPos[i][0]*find_length
					point_y = find_y + InAreaPointPos[i][1]*find_width
					if point_y >= rl_y and point_y <= target_y and point_x >= min(rl_x,target_x-0.5*target_length) and point_x <= target_x+0.5*target_length:
						block_happen = 1
			if block_happen == 1:
				block_id = find_id
				block_type = find_type
				block_x = find_x
				block_y = find_y
				block_result_part, vision_point_part, lidar_point_part = WillVehicleBlock(csv_data, rl_x, rl_y, target_id, target_type, target_x, target_y, quadrant, block_id, block_type, block_x, block_y)
				if block_result_part == -1:
					block_result = -1#no recognize
					vision_point = vision_point_part
					lidar_point = lidar_point_part
				elif block_result != -1 and block_result_part == 0:
					block_result = 0# recognzie, but no id
					vision_point = vision_point_part
					lidar_point = lidar_point_part
				elif block_result != -1 and block_result != 0 and block_result_part == 1:
					#block_result = 1
					vision_point = vision_point_part
					lidar_point = lidar_point_part
	return block_result, vision_point, lidar_point


def SearchTargetCar(id_data, csv_data, runtime, rl_x, rl_y):
	rl_x = rl_x - 0.5*rl_car['length']
	touchID_group = []
	touchResult_group = []
	type_group = []
	x_group = []
	y_group = []
	speed_group = []
	vision_point_group = []
	lidar_point_group = []
	for find_num in range(0,csv_data.shape[0]):
		if id_data != csv_data[find_num][0]:
			#print(find_num)
			block_result = 99
			target_id = csv_data[find_num][0]
			target_type = csv_data[find_num][1]
			if target_type[0] == 'R':# Rlcar
				target_length = rl_car['length']
				#print("rlcar in detection?")
			elif target_type[0] == 'G':# Gashumancar
				target_length = human_carGas['length']
			elif target_type[0] == 'E':# Elehumancar
				target_length = human_carEle['length']
			elif target_type[0] == 'B':# Bushuman
				target_length = human_bus['length']
			elif target_type[0] == 'T':# Truckhuman
				target_length = human_truck['length']
			target_x = float(csv_data[find_num][3]) - 0.5*target_length
			target_y = float(csv_data[find_num][4])
			distance = pow(pow((rl_x - target_x),2) + pow((rl_y - target_y),2), 0.5)
			if rl_y == target_y and rl_x > target_x and distance <= 120+0.5*target_length:#rl ahead
				angle_to_ahead = PI
				quadrant = 2
				block_result, vision_point, lidar_point = IsVehicleInsideArea(csv_data, runtime, rl_x, rl_y, angle_to_ahead, target_id, target_type, target_x, target_y, target_length, quadrant)
			elif rl_y == target_y and rl_x < target_x and distance <= 150+0.5*target_length:#rl behind
				angle_to_ahead = 0
				quadrant = 4
				block_result, vision_point, lidar_point = IsVehicleInsideArea(csv_data, runtime, rl_x, rl_y, angle_to_ahead, target_id, target_type, target_x, target_y, target_length, quadrant)
			elif rl_y > target_y and rl_x <= target_x:#target I Quadrant
				angle_to_ahead = 0.0 + np.arcsin(float(abs(target_y - rl_y))/distance)
				quadrant = 1
				if (angle_to_ahead <= 25/180*PI and distance <= 150+0.5*target_length) or (angle_to_ahead > 25/180*PI and distance <= 120+0.5*target_length):
					block_result, vision_point, lidar_point = IsVehicleInsideArea(csv_data, runtime, rl_x, rl_y, angle_to_ahead, target_id, target_type, target_x, target_y, target_length, quadrant)
			elif rl_y > target_y and rl_x > target_x and distance <= 120+0.5*target_length:#target II Quadrant
				angle_to_ahead = PI - np.arcsin(float(abs(target_y - rl_y))/distance)
				quadrant = 2
				block_result, vision_point, lidar_point = IsVehicleInsideArea(csv_data, runtime, rl_x, rl_y, angle_to_ahead, target_id, target_type, target_x, target_y, target_length, quadrant)
			elif rl_y < target_y and rl_x >= target_x and distance <= 120+0.5*target_length:#target III Quadrant
				angle_to_ahead = PI + np.arcsin(float(abs(target_y - rl_y))/distance)
				quadrant = 3
				block_result, vision_point, lidar_point = IsVehicleInsideArea(csv_data, runtime, rl_x, rl_y, angle_to_ahead, target_id, target_type, target_x, target_y, target_length, quadrant)
			elif rl_y < target_y and rl_x < target_x:#target IV Quadrant
				angle_to_ahead = 2*PI - np.arcsin(float(abs(target_y - rl_y))/distance)
				quadrant = 4
				if (angle_to_ahead >= 2*PI-25/180*PI and distance <= 150+0.5*target_length) or (angle_to_ahead < 2*PI-25/180*PI and distance <= 120+0.5*target_length):
					block_result, vision_point, lidar_point = IsVehicleInsideArea(csv_data, runtime, rl_x, rl_y, angle_to_ahead, target_id, target_type, target_x, target_y, target_length, quadrant)
			#if block_result != 99 and block_result != -1:
			if block_result != 99:
				touchID_group.append(target_id)
				touchResult_group.append(block_result)
				type_group.append(csv_data[find_num][1])
				x_group.append(target_x)
				y_group.append(target_y)
				speed_group.append(csv_data[find_num][6])
				vision_point_group.append(vision_point)
				lidar_point_group.append(lidar_point)
	
	#Add rl_car itself??
	
	return touchID_group, touchResult_group, type_group, x_group, y_group, speed_group, vision_point_group, lidar_point_group
