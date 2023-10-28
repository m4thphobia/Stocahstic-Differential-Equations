import os
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)


# get folder path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
output_folder = os.path.join(parent_dir, "out")
# make folder if not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
