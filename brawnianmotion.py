import os
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)


# 出力先のフォルダパスを作成
output_folder = os.path.join(os.path.dirname(__file__), "out")
# フォルダが存在しない場合は作成する
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


T, N = 1, 500
dt, dW, B = T/N, np.zeros(N), np.zeros(N)


for i in range(1, N):
    dW[i] = np.sqrt(dt)*np.random.randn()
    B[i] = B[i-1] + dW[i]


plt.title(f"{os.path.basename(__file__).split('.')[0]}")
plt.plot(np.arange(0, 1, dt), B, color="b", label="path")
plt.xlabel("")
plt.ylabel("")
plt.savefig(output_folder + f"\{os.path.basename(__file__).split('.')[0]}.png")
