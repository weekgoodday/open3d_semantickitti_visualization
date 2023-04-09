## 网上不太有open3d打开SemanticKITTI数据集的API，尝试边学边记录一个。
### 一个单帧点云可视化的最精简文件oneframe.py 
just run:
```
python oneframe.py
```

### simplified.py来自于以下repository 精简了一下文件结构，并且视角变成全局
* [Open3d+KITTI site](https://github.com/Jiang-Muyun/Open3D-Semantic-KITTI-Vis)

The directory is organized in the following format:
```
├── 00/
│   ├── labels/
│   │     ├ 000000.label
│   │     └ 000001.label
│   └── velodyne/
│         ├ 000000.bin
│         └ 000001.bin
├── 08/
        .
        .
        .
├── config/
        .
        .
        .
        └semantic-kitti.yaml
├── src/
        └kitti_base.py
.
.
.
└── simplified.py

├── label_mapping/
        └semantic-kitti_11class.yaml

```
just run:
```
python simplified.py
```