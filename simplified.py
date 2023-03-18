import open3d
import os
import numpy as np
from PIL import Image
import glob
import argparse
import json

from src.kitti_base import PointCloud_Vis, Semantic_KITTI_Utils

def init_params():
    parser = argparse.ArgumentParser('vis_velo.py')
    parser.add_argument('--cfg', default = 'config/ego_view.json', type=str)
    parser.add_argument('--root', default = '.', type=str)
    parser.add_argument('--part', default = '00', type=str , help='KITTI part number')
    parser.add_argument('--index', default = 0, type=int, help='start index')
    parser.add_argument('--voxel', default = 0.1, type=float, help='voxel size for down sampleing')
    parser.add_argument('--modify', action = 'store_true', default = False, help='modify an existing view')
    args = parser.parse_args()

    assert os.path.exists(args.root),'Root directory does not exist '+ args.root
    assert os.path.exists(args.cfg), 'Config file does not exist '+ args.cfg

    cfg_data = json.load(open(args.cfg))
    h_fov = cfg_data['h_fov']
    v_fov = cfg_data['v_fov']
    x_range = cfg_data['x_range']
    y_range = cfg_data['y_range']
    z_range = cfg_data['z_range']
    d_range = cfg_data['d_range']

    handle = Semantic_KITTI_Utils(root = args.root)
    handle.set_part(part = args.part)
    handle.set_filter(h_fov, v_fov, x_range, y_range, z_range, d_range)
    vis_handle = PointCloud_Vis(args.cfg, new_config = args.modify)

    return args, handle, vis_handle

if __name__ == "__main__":
    args, handle, vis_handle = init_params()
    for index in range(args.index, handle.get_max_index()):
        # Load image, velodyne points and semantic labels
        handle.load(index)
        pcd,sem_label = handle.extract_points(voxel_size = args.voxel)
        pts_3d = np.asarray(pcd.points).astype(np.float32)
        print(index,'/',handle.get_max_index(), 'n_pts',pts_3d.shape[0])
        vis_handle.update(pcd)

