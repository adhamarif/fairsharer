# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 20:37:52 2022

@author: Adham
"""
def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    Args
    values:
    1D array of values (list or numpy array)
    num_iteration:
    Integer to set the number of iterations
    """
    for _ in range(num_iterations):
        #max_value = max(values)
        idx_max = values.index(max(values)) 
        residue = int(max(values) * share)
        
        if idx_max == len(values) - 1:
            values[0] += residue    
        else:    
            values[idx_max + 1] += residue
                
        values[idx_max - 1] += residue
        values[idx_max] -= residue * 2             
                
    return values


print(fair_sharer([0, 1000, 800, 0], 1))
print(fair_sharer([0, 1000, 800, 0], 2))
print(fair_sharer([0, 0, 800, 1000], 1))
print(fair_sharer([1000, 0, 800, 0], 1))