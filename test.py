import numpy as np
from bvh import Bvh
import math
import matplotlib.pyplot as plt
import csv

with open('take004_point_tired_chr00_frame90.bvh','r') as f:
    mocap = Bvh(f.read())
    
    frame_num=list(range(mocap.nframes))

    joint_position_x = list()
    joint_position_y = list()
    joint_position_z = list()
    
    item='RightArm'
    print(item)
    for frame in range(0,mocap.nframes):#0,mocap.nframes
        #join_position_x
        
        if frame==0:
            joint_position_x.append(mocap.frame_joint_channel(frame, item, 'Xrotation'))
        else:
            if (mocap.frame_joint_channel(frame, item, 'Xrotation')-joint_position_x[frame-1])>70:
                joint_position_x.append(180-mocap.frame_joint_channel(frame, item, 'Xrotation'))    
            elif (mocap.frame_joint_channel(frame, item, 'Xrotation')-joint_position_x[frame-1])<-70:
                joint_position_x.append(180+mocap.frame_joint_channel(frame, item, 'Xrotation'))
            else:
                joint_position_x.append(mocap.frame_joint_channel(frame, item, 'Xrotation'))
        
        if frame==0:
            joint_position_y.append(mocap.frame_joint_channel(frame, item, 'Yrotation'))
        else:
            if (mocap.frame_joint_channel(frame, item, 'Yrotation')-joint_position_y[frame-1])>90:
                joint_position_y.append(180-mocap.frame_joint_channel(frame, item, 'Yrotation'))    
            elif (mocap.frame_joint_channel(frame, item, 'Yrotation')-joint_position_y[frame-1])<-90:
                joint_position_y.append(180+mocap.frame_joint_channel(frame, item, 'Yrotation'))
            else:
                joint_position_y.append(mocap.frame_joint_channel(frame, item, 'Yrotation'))
        
        if frame==0:
            joint_position_z.append(mocap.frame_joint_channel(frame, item, 'Zrotation'))
        else:
            if (mocap.frame_joint_channel(frame, item, 'Zrotation')-joint_position_z[frame-1])>90:
                joint_position_z.append(180-mocap.frame_joint_channel(frame, item, 'Zrotation'))    
            elif (mocap.frame_joint_channel(frame, item, 'Zrotation')-joint_position_z[frame-1])<-90:
                joint_position_z.append(180+mocap.frame_joint_channel(frame, item, 'Zrotation'))
            else:
                joint_position_z.append(mocap.frame_joint_channel(frame, item, 'Zrotation'))
    

        
    print("hahaha")

file = open('take4.csv', 'w',newline="")    #既存でないファイル名を作成してください
w = csv.writer(file)

for frame in range(0,mocap.nframes):
    w.writerow([
        frame,joint_position_x[frame],mocap.frame_joint_channel(frame,item,'Xrotation'),
        joint_position_y[frame],mocap.frame_joint_channel(frame,item,'Yrotation'),
        joint_position_z[frame],mocap.frame_joint_channel(frame,item,'Zrotation'),])

 
file.close()

fig = plt.figure()

ax = fig.add_subplot(3, 1, 1)
ax.plot(frame_num, joint_position_x, marker="o", color = "red", linestyle = "--")
#plt.savefig("hogex.png")
ay = fig.add_subplot(3, 1, 2)
ay.plot(frame_num, joint_position_y, marker="v", color = "blue", linestyle = ":")
#plt.savefig("hogey.png")
az = fig.add_subplot(3, 1, 3)
az.plot(frame_num, joint_position_z, marker="v", color = "green", linestyle = ":")
#plt.savefig("hogez.png")
'''
fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)
ax.plot(frame_num, joint_position_x, marker="o", color = "red", linestyle = "--")
'''
plt.savefig("filter2.png")
