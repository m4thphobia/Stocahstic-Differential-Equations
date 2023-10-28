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
dt = T/N
B = np.cumsum(np.sqrt(dt)*np.random.randn(N))


plt.title(f"{os.path.basename(__file__).split('.')[0]}")
plt.plot(np.arange(0, 1, dt), B, color="b", label="path")
plt.xlabel("")
plt.ylabel("")
plt.savefig(output_folder + f"\{os.path.basename(__file__).split('.')[0]}.png")
