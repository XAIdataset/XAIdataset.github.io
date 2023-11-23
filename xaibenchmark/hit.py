import numpy as np

def pointing_game(array1, array2):
    assert array1.shape == array2.shape, "Arrays must have the same shape"

    # Find the coordinates of the largest elements in array1
    coords = np.argwhere(array1 == np.amax(array1))

    # Check if any of the coordinates have positive values in array2
    for coord in coords:
        if array2[coord[0], coord[1]] > 0:
            return 1

    return 0

def hit(maps, gts):
    hits = []
    num = maps.shape[0]
    
    for i in range(num):
        map, gt = maps[i], gts[i]
        if gt.sum() != 0:
            hit = pointing_game(map, gt)
            hits.append(hit)
     
    hit = np.mean(hits)
    
    return hit