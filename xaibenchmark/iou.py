import numpy as np

def compute_iou(x, y):
    x = (x > 0).astype(int)
    y = y.astype(int)
    # Compute the intersection
    intersection = np.logical_and(x, y)
    # Compute the union
    union = np.logical_or(x, y)
    # Compute the IoU
    iou = np.sum(intersection) / np.sum(union)

    return iou

def iou(maps, gts):
    ious = []
    num = maps.shape[0]
    
    for i in range(num):
        map, gt = maps[i], gts[i]
        if gt.sum() != 0:
            iou = compute_iou(map, gt)
            ious.append(iou)
        
    iou = np.mean(ious)
    
    return iou