import os
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)


drift, diffusion = 2, 1
Xzero = 1
T, N = 1, 2**8
dt = T/N
t = np.arange(0, 1, dt)
dW = np.sqrt(dt)*np.random.randn(N-1)
B = np.zeros(N)
B[1:] = np.cumsum(dW)

Xtrue = Xzero*np.exp((drift - 0.5*diffusion**2)*t + diffusion*B)


R = 4
Dt = R*dt
L = N//R
t_em = np.arange(0, T + Dt, Dt)
Xem = [Xzero]*(L+1)
Xtemp = Xzero

for i in range(L):
    Winc = np.sum(dW[R*i:R*(i+1)])
    Xtemp += Dt * drift * Xtemp + diffusion * Xtemp * Winc
    Xem[i+1] = Xtemp


emerr = abs(Xem[-1] - Xtrue[-1])
print("EM error:", emerr)


# make folder for pics
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
output_folder = os.path.join(parent_dir, "out")
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# plot
plt.title(f"{os.path.basename(__file__).split('.')[0]}")
plt.plot(t, Xtrue, color="r", label="true path", linewidth=0.5)
plt.plot(t_em, Xem, color="m", label="EM path", linewidth=0.5)
plt.xlabel("")
plt.ylabel("")
plt.legend()
plt.savefig(output_folder+f"\{os.path.basename(__file__).split('.')[0]}.png")
