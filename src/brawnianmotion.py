import os
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
output_folder = os.path.join(parent_dir, "out")
# フォルダが存在しない場合は作成する
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


T, N = 1, 500
dt = T/N
t = np.arange(0, 1, dt)
B = np.zeros(N)
B[1:] = np.cumsum(np.sqrt(dt)*np.random.randn(N-1))

plt.title(f"{os.path.basename(__file__).split('.')[0]}")
plt.plot(t, B, color="b", label="path")
plt.xlabel("")
plt.ylabel("")
plt.legend()
plt.savefig(output_folder + f"\{os.path.basename(__file__).split('.')[0]}.png")
