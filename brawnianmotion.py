import numpy as np
import os
import matplotlib.pyplot as plt

np.random.seed(42)


T, N = 1, 500
dt, dW, B = T/N, np.zeros(N), np.zeros(N)


dW[0] = np.sqrt(dt)*np.random.randn()
B[0] = dW[0]
for i in range(1, N):
    dW[i] = np.sqrt(dt)*np.random.randn()
    B[i] = B[i-1] + dW[i]


# 出力先のフォルダパスを作成
output_folder = os.path.join(os.path.dirname(__file__), "out")
# フォルダが存在しない場合は作成する
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

plt.title("brawnian_motion")
plt.plot(np.arange(0, 1, dt), B, color="b", label="")
plt.xlabel("")
plt.ylabel("")
plt.savefig(output_folder+"/brawnianmotion.png")
