
import numpy as np

def aureo_state(layers, noise):
    if layers < 1:
        return [0.5, 0.5]
    a, b = 1.0, 1.0
    for _ in range(layers):
        a, b = b, a + b
    ratio = b / a + np.random.normal(0, noise)
    phi_approx = ratio
    state0 = 1 / phi_approx
    state1 = 1 - state0
    return [round(state0, 2), round(state1, 2)]

# Exemplo: print(aureo_state(9, 0.2))
