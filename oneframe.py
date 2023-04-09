import open3d as o3d
import numpy as np
import yaml
DATA=yaml.safe_load(open('./label_mapping/semantic-kitti_11class.yaml','r'))
def vis_oneframe(pointfile,labelfile):
    bin_pcd = np.fromfile(pointfile, dtype=np.float32)
    points = bin_pcd.reshape((-1, 4))[:, 0:3]
    o3d_pcd = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(points))
    label=np.fromfile(labelfile, dtype=np.int32)
    sem_label = label & 0xFFFF
    color_label=[DATA['color_map'][i] for i in sem_label]
    color_label_rgb=(np.array(color_label)[:,[2,1,0]]/255).tolist()
    # unique1,counts1=np.unique(color_label_rgb,axis=0,return_counts=True)
    # print(unique1)
    # print(counts1)
    o3d_pcd.colors = o3d.utility.Vector3dVector(color_label_rgb)
    o3d.visualization.draw_geometries([o3d_pcd])
pointfile="./08/velodyne/000000.bin"
originlabelfile="./08/labels/000000.label"

vis_oneframe(pointfile,originlabelfile)

