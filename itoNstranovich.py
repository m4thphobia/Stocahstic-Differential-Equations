import os
import numpy as np
import matplotlib.pyplot as plt
random.seed(42)
np.random.seed(42)
# 出力先のフォルダパスを作成
output_folder = os.path.join(os.path.dirname(__file__), "out")
# フォルダが存在しない場合は作成する
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


T, N = 1, 500
dt = T/N
dW = np.sqrt(dt)*np.random.randn(N)
B = np.cumsum(dW)

# Calculate Itô integral
ito = np.sum(np.mul(np.roll(B, 1), dW))
# Calculate Stratonovich integral
strat = np.sum(np.multiply(0.5*(np.roll(B, 1) + B)
                            + 0.5*np.sqrt(dt)*np.random.randn(N), dW))

# Calculate errors
itoerr = abs(ito - 0.5 * (B[-1] ** 2 - T))
straterr = abs(strat - 0.5 * (B[-1] ** 2))

print("Itô integral error:", itoerr)
print("Stratonovich integral error:", straterr)
