import numpy as np

def compute_iou(x, y):
    x = (x > 0.5).astype(int)
    y = y.astype(int)
    
    true_positives = np.sum(np.logical_and(y, x))
    false_negatives = np.sum(np.logical_and(y, np.logical_not(x)))
    
    if true_positives + false_negatives != 0:
        recall = true_positives / (true_positives + false_negatives)
    else:
        recall = 0.0

    return recall

def recall(maps, gts):
    recalls = []
    num = maps.shape[0]
    
    for i in range(num):
        map, gt = maps[i], gts[i]
        if gt.sum() != 0:
            recall = compute_iou(map, gt)
            recalls.append(recall)
    
    recall = np.mean(recalls)  
    
    return recall