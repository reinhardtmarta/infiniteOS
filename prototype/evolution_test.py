import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
import imageio
import os

# --- Funções base ----------------------------------------------------------

def normalize(arr):
    arr = arr - np.min(arr)
    if np.max(arr) > 0:
        arr = arr / np.max(arr)
    return arr

def evolve_layer(layer):
    """Regra de evolução: convolução + escala + normalização."""
    kernel = np.array([[0.5, 1.0, 0.5],
                       [1.0, 2.0, 1.0],
                       [0.5, 1.0, 0.5]])
    evolved = convolve2d(layer, kernel, mode='same', boundary='wrap')
    evolved = normalize(evolved * 1.2)
    return evolved

def render_heightmap(matrix, step, folder):
    """Renderiza uma camada 3D e salva como imagem."""
    fig = plt.figure(figsize=(5,4))
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(range(matrix.shape[0]), range(matrix.shape[1]))
    ax.plot_surface(X, Y, matrix, cmap='viridis', linewidth=0.2)
    ax.set_title(f"Evolution Step {step}")
    plt.tight_layout()
    path = os.path.join(folder, f"layer_{step:02d}.png")
    plt.savefig(path)
    plt.close(fig)
    return path

# --- Simulação -------------------------------------------------------------

def run_evolution(steps=10):
    output_dir = "layers_output"
    os.makedirs(output_dir, exist_ok=True)

    # padrão inicial (inspirado no seu: modo 1 6 1 8)
    pattern = np.array([
        [0,1,0,0,1],
        [1,1,1,1,0],
        [0,1,0,1,1],
        [1,0,1,0,1],
        [0,1,1,0,1]
    ], dtype=float)

    current = pattern
    frames = []

    for i in range(steps):
        path = render_heightmap(current, i, output_dir)
        frames.append(imageio.imread(path))
        current = evolve_layer(current)

    gif_path = os.path.join(output_dir, "evolution.gif")
    imageio.mimsave(gif_path, frames, duration=0.6)
    print(f"Evolução concluída ✅\nImagens em: {output_dir}\nGIF final: {gif_path}")

# --- Execução --------------------------------------------------------------

if __name__ == "__main__":
    run_evolution(steps=10)
