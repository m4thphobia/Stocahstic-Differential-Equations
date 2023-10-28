import os
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
output_folder = os.path.join(parent_dir, "out")
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


T, N = 1, 500
dt = T/N
dW = np.sqrt(dt)*np.random.randn(N)
B = np.zeros(N)
B[1:] = np.cumsum(np.sqrt(dt)*np.random.randn(N-1))

# Calculate Itô integral
ito = np.sum(np.mul(B, dW))
# Calculate Stratonovich integral
strat = np.sum(np.mul(0.5*(np.roll(B, 1) + B)
                            + 0.5*np.sqrt(dt)*np.random.randn(N), dW))

# Calculate errors
itoerr = abs(ito - 0.5 * (B[-1] ** 2 - T))
straterr = abs(strat - 0.5 * (B[-1] ** 2))

print("Itô integral error:", itoerr)
print("Stratonovich integral error:", straterr)
