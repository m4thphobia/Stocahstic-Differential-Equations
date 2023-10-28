import os
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)


# get folder path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
output_folder = os.path.join(parent_dir, "out")

print(output_folder)
print(output_folder+f"\{os.path.basename(__file__).split('.')[0]}.png")
