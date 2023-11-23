import numpy as np

def compute_iou(x, y):
    x = (x > 0).astype(int)
    y = y.astype(int)
    
    true_positives = np.sum(np.logical_and(y, x))
    false_positives = np.sum(np.logical_and(np.logical_not(y), x))
    
    precision = true_positives / (true_positives + false_positives)
    
    return precision

def precision(maps, gts):
    precisions = []
    num = maps.shape[0]
    
    for i in range(num):
        map, gt = maps[i], gts[i]
        if gt.sum() != 0:
            precision = compute_iou(map, gt)
            precisions.append(precision)
            
    precision = np.mean(precisions)    

    return precision