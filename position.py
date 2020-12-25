import numpy as np
from bvh import Bvh
import math
import matplotlib.pyplot as plt
import csv

with open('take004_point_tired_chr00_frame90.bvh','r') as f:
    mocap = Bvh(f.read())
    
    frame_num = list(range(mocap.nframes))

    joint_position = list()

    joint_position_x = list()
    joint_position_y = list()
    joint_position_z = list()
    
    item = 'LeftForeArm'
    print(item)
    for frame in range(0,mocap.nframes):#0,mocap.nframes
        x = mocap.frame_joint_channel(frame, item, 'Xposition')
        y = mocap.frame_joint_channel(frame, item, 'Yposition')
        z = mocap.frame_joint_channel(frame, item, 'Zposition')

        joint_position_x.append(x)
        joint_position_y.append(y)
        joint_position_z.append(z)
        joint_position.append(((x**2)+(y**2)+(z**2))**(1/2))

#fig = plt.figure()

routine_x = list()
routine_y = list()
routine_z = list()
routine = list()
routine_num = list(range(100))
#frame_count = 0
#stop_frame = list()
for i in range(0,((mocap.nframes-1390)//100)-3):
    fig = plt.figure()
    for j in range(0,100):
        if i==0:
            #routine_x.append(joint_position_x[j+1390])
            #routine_y.append(joint_position_y[j+1390])
            #routine_z.append(joint_position_z[j+1390])
            routine.append(joint_position[j+1390])
        else:
            #routine_x[j]=(joint_position_x[j+1390+i*100])
            #routine_y[j]=(joint_position_y[j+1390+i*100])
            #routine_z[j]=(joint_position_z[j+1390+i*100])
            routine[j]=joint_position[j+1390+i*100]
            #if abs(routine_z[j]-routine_z[j-1])<1.5:
                #frame_count+=1
    #stop_frame.append(frame_count)
    #frame_count = 0
    '''
    ax = fig.add_subplot(3, 1, 1)
    ax.plot(routine_num, routine_x, marker="o", color = "red", linestyle = "--")
    ay = fig.add_subplot(3, 1, 2)
    ay.plot(routine_num, routine_y, marker="v", color = "blue", linestyle = ":")
    az = fig.add_subplot(3, 1, 3)
    az.plot(routine_num, routine_z, marker="v", color = "green", linestyle = ":")
    '''
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(routine_num, routine, marker="o", color = "red", linestyle = "--")
    plt.savefig("position/position{}.png".format(i))
