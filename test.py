import numpy as np
from bvh import Bvh
import math
import matplotlib.pyplot as plt
import csv

with open('take001_lock_chr00_frame90.bvh','r') as f:
    mocap = Bvh(f.read())
    
    frame_num=list(range(mocap.nframes))

    joint_position_x = list()
    joint_position_y = list()
    joint_position_z = list()
    
    item='Hips'#RightArm Hips Spine LeftArm
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
'''
file = open('take1.csv', 'w',newline="")    #既存でないファイル名を作成してください
w = csv.writer(file)

for frame in range(0,mocap.nframes):
    w.writerow([
        frame,joint_position_x[frame],mocap.frame_joint_channel(frame,item,'Xrotation'),
        joint_position_y[frame],mocap.frame_joint_channel(frame,item,'Yrotation'),
        joint_position_z[frame],mocap.frame_joint_channel(frame,item,'Zrotation'),])

 
file.close()
'''
routine_x = list()
routine_y = list()
routine_z = list()
routine_num = list(range(25))
frame_count = 0
stop_frame = list()
for i in range(0,((mocap.nframes-1390)//100)-3):
    fig = plt.figure()
    for j in range(0,25):
        if i==0:
            #routine_x.append(joint_position_x[j+1390+63])
            #routine_y.append(joint_position_y[j+1390+63])
            routine_z.append(joint_position_z[j+1390+63])
        else:
            #routine_x[j]=joint_position_x[j+1390+63+i*100]
            #routine_y[j]=joint_position_y[j+1390+63+i*100]
            routine_z[j]=joint_position_z[j+1390+63+i*100]
            if abs(routine_z[j]-routine_z[j-1])<1.5:
                frame_count+=1
    stop_frame.append(frame_count)
    frame_count = 0
        
    
    '''
    ax = fig.add_subplot(3, 1, 1)
    ax.plot(routine_num, routine_x, marker="o", color = "red", linestyle = "--")
    ay = fig.add_subplot(3, 1, 2)
    ay.plot(routine_num, routine_y, marker="v", color = "blue", linestyle = ":")
    az = fig.add_subplot(3, 1, 3)
    az.plot(routine_num, routine_z, marker="v", color = "green", linestyle = ":")
    #plt.savefig("take1/{}/routine{}.png".format(item,i))
    '''
    #plt.savefig("hoge{}.png".format(i))
print("平均静止フレームは{}".format(sum(stop_frame)/len(stop_frame)))
'''
    ax = fig.add_subplot(3, 1, 1)
    ax.plot(frame_num, joint_position_x, marker="o", color = "red", linestyle = "--")
    #plt.savefig("hogex.png")
    ay = fig.add_subplot(3, 1, 2)
    ay.plot(frame_num, joint_position_y, marker="v", color = "blue", linestyle = ":")
    #plt.savefig("hogey.png")
    az = fig.add_subplot(3, 1, 3)
    az.plot(frame_num, joint_position_z, marker="v", color = "green", linestyle = ":")
    #plt.savefig("hogez.png")
    
    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1)
    ax.plot(frame_num, joint_position_x, marker="o", color = "red", linestyle = "--")
    '''
   #plt.savefig("filter.png")
