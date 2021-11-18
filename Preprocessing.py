import numpy as np
import os
import multiprocessing

folders = []
# os.listdir() method in python is used to get the list of all files and directories in the specified directory.
for folder in os.listdir(src):
    # only process folders
    if not os.path.isdir(os.path.join(src, folder)):
        continue
    folders.append(folder)
    
 pool=multiprocessing.Pool(processes=n_processes)
_=pool.map(_preprocess_data, [(os.path.join(src, folder), 
                                      os.path.join(dst, folder), 
                                      src_meta) for folder in sorted(folders)])
