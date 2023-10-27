import numpy as np
import random


def fix_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    return 0


seed = 42
fix_seed(seed)


T = 1
N = 500
dt = T/N
