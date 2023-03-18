import open3d as o3d
import numpy as np
from src.kitti_base import Semantic_KITTI_Utils
bin_pcd = np.fromfile("./00/velodyne/000000.bin", dtype=np.float32)
points = bin_pcd.reshape((-1, 4))[:, 0:3]
o3d_pcd = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(points))

o3d.visualization.draw_geometries([o3d_pcd])
root="./00"
handle = Semantic_KITTI_Utils(root = root)