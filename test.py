import numpy as np
from bvh import Bvh
import math

with open('take003_chr00.bvh','r') as f:
    mocap=Bvh(f.read())
    joints_name = mocap.get_joints_names()
    borns_length=list()
    joint_position=list()

    for item in joints_name:
        if item=='Hips':
            borns_length.append(0)
            print("Hips")
        else:
            #mocap.joint_parent(item).name
            #print(mocap.joint_offset(item)[0])
            a=(mocap.joint_offset(item)[0])**2+(mocap.joint_offset(item)[1])**2+(mocap.joint_offset(item)[2])**2
            borns_length.append(math.sqrt(a))
    item='RightHandThumb3'

    for frame in range(400,450):
        joint_position.append([
                    mocap.frame_joint_channel(frame, item, 'Xrotation'),
                    mocap.frame_joint_channel(frame, item, 'Yrotation'),
                    mocap.frame_joint_channel(frame, item, 'Zrotation')
                    # mocap.frame_joint_channel(frame, item, 'Xposition'),
                    # mocap.frame_joint_channel(frame, item, 'Yposition'),
                    # mocap.frame_joint_channel(frame, item, 'Zposition')
                ])
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
    print(joint_position)

