import csv
import os
import numpy as np
import random
import pandas as pd

csv_data = pd.read_csv('highway_rl_inlane3.csv')
print(csv_data.shape[0])

print((csv_data[['id']].values[0])[0])#(train_batch_data.values[rows_num])[0]
print((csv_data[['type']].values[0])[0])
print((csv_data[['time']].values[0])[0])
print((csv_data[['x']].values[0])[0])
print((csv_data[['y']].values[0])[0])
print((csv_data[['length']].values[0])[0])
print((csv_data[['speed']].values[0])[0])
print((csv_data[['follower_id']].values[0])[0])

print(csv_data.at[0,'id'])

fileHeader = ["id","type","time","x","y","length","speed","follower_id"]

csvfile = open("Lite_highway/Lite_highway_rl_inlane3.csv", 'w')
csvwrite = csv.writer(csvfile)
csvwrite.writerow(fileHeader)

csvfile2 = open("Lite_highway_Check/Lite_highway_Check_rl_inlane3.csv", 'w')
csvwrite2 = csv.writer(csvfile2)
csvwrite2.writerow(fileHeader)

for copy_num in range(0,csv_data.shape[0]):
	id_data = csv_data.at[copy_num,'id'] # Rlcar Gashumancar Elehumancar Bushuman Truckhuman
	type_data = csv_data.at[copy_num,'type']
	time_data = float(csv_data.at[copy_num,'time'])
	x_data = float(csv_data.at[copy_num,'x'])
	y_data = float(csv_data.at[copy_num,'y'])
	length_data = float(csv_data.at[copy_num,'length'])
	speed_data = float(csv_data.at[copy_num,'speed'])
	follower_id_data = csv_data.at[copy_num,'follower_id']
	
	information = [id_data, type_data, time_data, x_data, y_data, length_data, speed_data, follower_id_data]
	
	if 2880 <= x_data <= 4650: #$ 4730-(4850,5850) 2880-(3000,4650)
		csvwrite.writerow(information)
	if x_data <= 4520: # 1330-1520,2830-3020,4330-4520,4730-6000
		csvwrite2.writerow(information)

csvfile.close()
csvfile2.close()
