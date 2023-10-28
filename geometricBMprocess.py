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
t = np.arange(0, 1, dt)
M = 1000
B = np.cumsum(np.sqrt(dt)*np.random.randn(M, N), axis=1)

Y = np.exp(t)
U = np.exp(np.tile(t, (M, 1))+0.5*B)
Umean = np.mean(U, axis=0)

plt.title(f"{os.path.basename(__file__).split('.')[0]}")
for i in range(10):
    plt.plot(t, U[i, :], linestyle='--', color="m", linewidth=0.5)
plt.plot(t, Umean, color="r", label="mean")
plt.plot(t, Y, color="b", label="trend")
plt.xlabel("")
plt.ylabel("")
plt.legend()
plt.savefig(output_folder+f"\{os.path.basename(__file__).split('.')[0]}.png")
