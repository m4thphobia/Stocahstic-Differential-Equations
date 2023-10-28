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
B = np.cumsum(np.sqrt(dt)*np.random.randn(N))

