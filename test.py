import numpy as np
from bvh import Bvh
import math
import matplotlib.pyplot as plt

with open('take004_copy_copy_chr00_lock.bvh','r') as f:
    mocap=Bvh(f.read())
    joints_name = mocap.get_joints_names()
    borns_length=list()
    joint_position_x=list()
    joint_position_y=list()
    joint_position_z=list()
    frame_num=list(range(mocap.nframes))
    for item in joints_name:
        if item=='Hips':
            borns_length.append(0)
           # print("Hips")
        else:
            #mocap.joint_parent(item).name
            #print(mocap.joint_offset(item)[0])
            a=(mocap.joint_offset(item)[0])**2+(mocap.joint_offset(item)[1])**2+(mocap.joint_offset(item)[2])**2
            borns_length.append(math.sqrt(a))
    item='RightArm'
    print(item)
    for frame in range(0,mocap.nframes):
        joint_position_x.append(mocap.frame_joint_channel(frame, item, 'Xrotation'))
        joint_position_y.append(mocap.frame_joint_channel(frame, item, 'Yrotation'))
        joint_position_z.append(mocap.frame_joint_channel(frame, item, 'Zrotation'))
        # joint_position.append([
        #             mocap.frame_joint_channel(frame, item, 'Xrotation'),
        #             mocap.frame_joint_channel(frame, item, 'Yrotation'),
        #             mocap.frame_joint_channel(frame, item, 'Zrotation')
        #             # mocap.frame_joint_channel(frame, item, 'Xposition'),
        #             # mocap.frame_joint_channel(frame, item, 'Yposition'),
        #             # mocap.frame_joint_channel(frame, item, 'Zposition')
        #         ])
    # for item in joints_name:
    #     if item=='Hips':
    #         joint_position.append([
    #             mocap.frame_joint_channel(0, item, 'Xposition'),
    #             mocap.frame_joint_channel(0, item, 'Yposition'),
    #             mocap.frame_joint_channel(0, item, 'Zposition')
    #         ])
    #     else:
    #         joint_position.append([
    #                 (mocap.frame_joint_channel(0, item, 'Xrotation')),
    #                 mocap.frame_joint_channel(0, item, 'Yrotation'),
    #                 mocap.frame_joint_channel(0, item, 'Zrotation')
    #                 ])
    print("hahaha")
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
plt.savefig("hoge.png")
