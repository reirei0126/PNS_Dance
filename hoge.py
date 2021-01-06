import numpy as np
from bvh import Bvh
import math
import matplotlib.pyplot as plt

def rotM(p):
    # 回転行列を計算する
    px = p[0]
    py = p[1]
    pz = p[2]

    # # 物体座標系の 1->2->3 軸で回転させる
    # Rx = np.array([[1, 0, 0],
    #                [0, np.cos(px), np.sin(px)],
    #                [0, -np.sin(px), np.cos(px)]])
    # Ry = np.array([[np.cos(py), 0, -np.sin(py)],
    #                [0, 1, 0],
    #                [np.sin(py), 0, np.cos(py)]])
    # Rz = np.array([[np.cos(pz), np.sin(pz), 0],
    #                [-np.sin(pz), np.cos(pz), 0],
    #                [0, 0, 1]])
    # #R = Rz.dot(Ry).dot(Rx)

    #物体座標系の 3->2->1 軸で回転させるkorepoi
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(px), np.sin(px)],
                   [0, -np.sin(px), np.cos(px)]])
    Ry = np.array([[np.cos(py), 0, -np.sin(py)],
                   [0, 1, 0],
                   [np.sin(py), 0, np.cos(py)]])
    Rz = np.array([[np.cos(pz), np.sin(pz), 0],
                   [-np.sin(pz), np.cos(pz), 0],
                   [0, 0, 1]])
    R = Rx.dot(Ry).dot(Rz)       

    #空間座標系の 1->2->3 軸で回転させる
    # Rx = np.array([[1, 0, 0],
    #                [0, np.cos(px), -np.sin(px)],
    #                [0, np.sin(px), np.cos(px)]])
    # Ry = np.array([[np.cos(py), 0, -np.sin(py)],
    #                [0, 1, 0],
    #                [np.sin(py), 0, np.cos(py)]])
    # Rz = np.array([[np.cos(pz), np.sin(pz), 0],
    #                [-np.sin(pz), np.cos(pz), 0],
    #                [0, 0, 1]])
    # R = Rx.dot(Ry).dot(Rz)

    # 空間座標系の 3->2->1 軸で回転させる
    # Rx = np.array([[1, 0, 0],
    #                [0, np.cos(px), -np.sin(px)],
    #                [0, np.sin(px), np.cos(px)]])
    # Ry = np.array([[np.cos(py), 0, -np.sin(py)],
    #                [0, 1, 0],
    #                [np.sin(py), 0, np.cos(py)]])
    # Rz = np.array([[np.cos(pz), np.sin(pz), 0],
    #                [-np.sin(pz), np.cos(pz), 0],
    #                [0, 0, 1]])
    # R = Rz.dot(Ry).dot(Rx)
    return R
"""
def get_position(item,frame):

    if(item=="Hips"):
        px = mocap.frame_joint_channel(frame, mocap.joint_parent(item).name, 'Xposition')
        py = mocap.frame_joint_channel(frame, mocap.joint_parent(item).name, 'Yposition')
        pz = mocap.frame_joint_channel(frame, mocap.joint_parent(item).name, 'Zposition')
        return [px,py,pz]
    x = mocap.frame_joint_channel(frame, item, 'Xrotation')
    y = mocap.frame_joint_channel(frame, item, 'Yrotation')
    z = mocap.frame_joint_channel(frame, item, 'Zrotation')
    return get_position(mocap.joint_parent(item).name)+rotM([x,y,z]).dot(list(mocap.joint_offset(item)))
"""
with open('lock6.bvh','r') as f:
    mocap = Bvh(f.read())

    def get_position(item,frame,mocap):
    
        if(item=="Hips"):
            px = mocap.frame_joint_channel(frame, item, 'Xposition')
            py = mocap.frame_joint_channel(frame, item, 'Yposition')
            pz = mocap.frame_joint_channel(frame, item, 'Zposition')
            return [px,py,pz]
        x = mocap.frame_joint_channel(frame, item, 'Xrotation')
        y = mocap.frame_joint_channel(frame, item, 'Yrotation')
        z = mocap.frame_joint_channel(frame, item, 'Zrotation')
        return get_position(mocap.joint_parent(item).name,frame,mocap)+rotM([x,y,z]).dot(list(mocap.joint_offset(item)))

    frame_num = list(range(mocap.nframes-1))

    position_list = list()
    disp_list = list()
    stop_conut = 0
    item = "RightForeArm"
    print(item)
    for frame in range(0,mocap.nframes):#0,mocap.nframes
        position_list.append(
            get_position(item,frame,mocap)
        )
        print(position_list[frame])
        if(frame!=0):
            disp_list.append(
                ((position_list[frame][0]-position_list[frame-1][0])**2+
                (position_list[frame][1]-position_list[frame-1][1])**2+
                (position_list[frame][2]-position_list[frame-1][2])**2)**(1/2)
            ) 
            if(disp_list[frame-1]<5):
                    stop_conut +=1
            #print(rotM([x,y,z]).dot(list(mocap.joint_offset(item))))
    """
    item_list = mocap.get_joints_names()
    print(item_list)
    for item in item_list:
        for frame in range(0,mocap.nframes):#0,mocap.nframes
            x = mocap.frame_joint_channel(frame, item, 'Xrotation')
            y = mocap.frame_joint_channel(frame, item, 'Yrotation')
            z = mocap.frame_joint_channel(frame, item, 'Zrotation')

            position_list.append(
                rotM([x,y,z]).dot(list(mocap.joint_offset(item)))
            )
            #print((position[0]**2+position[1]**2+position[2]**2)**(1/2))
    """

routine = list()
routine_num = list(range(100))
frame_count = 0
stop_frame = list()
for i in range(0,((mocap.nframes)//100)):
    fig = plt.figure()
    for j in range(0,100):
        routine.append(disp_list[j+i*100])
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(routine_num, routine, marker="o", color = "red", linestyle = "--")
    plt.savefig("position/{}/routine{}.png".format(item,i))
    routine.clear()

print(stop_conut)