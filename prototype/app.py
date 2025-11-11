# app.py — Protótipo 1 do infiniteOS (simulador local)
# Requer: pip install flask numpy matplotlib scipy

from flask import Flask, request, jsonify, send_file
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
import io

app = Flask(__name__)

# ---- Funções de processamento ----------------------------------------------

def normalize(arr):
    arr = arr - np.min(arr)
    if np.max(arr) > 0:
        arr = arr / np.max(arr)
    return arr

def evolve_layer(layer, rules):
    """Aplica um conjunto de transformações sobre o padrão numérico."""
    result = layer.copy()
    for rule in rules:
        op = rule.get("op")
        if op == "scale":
            result *= rule.get("factor", 1.0)
        elif op == "convolve":
            kernel = np.array(rule.get("kernel", [[0,1,0],[1,1,1],[0,1,0]]))
            result = convolve2d(result, kernel, mode="same", boundary="wrap")
        elif op == "threshold":
            thr = rule.get("value", 0.5)
            result = (result > thr).astype(float)
        elif op == "normalize":
            result = normalize(result)
    return result

def render_heightmap(matrix):
    """Gera um gráfico 3D e retorna como arquivo PNG."""
    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(111, projection='3d')

    x = np.arange(matrix.shape[0])
    y = np.arange(matrix.shape[1])
    X, Y = np.meshgrid(x, y)

    ax.plot_surface(X, Y, matrix, cmap='viridis', linewidth=0.2)
    ax.set_title("infiniteOS – Heightmap Evolution")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Altura")

    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    return buf

# ---- Rotas da API ----------------------------------------------------------

@app.route('/simulate', methods=['POST'])
def simulate():
    """
    Corpo esperado (JSON):
    {
      "pattern": [[0,1,0],[1,1,1],[0,1,0]],
      "rules": [
         {"op":"convolve"},
         {"op":"scale","factor":1.2},
         {"op":"normalize"}
      ]
    }
    """
    data = request.get_json(force=True)
    pattern = np.array(data.get("pattern"))
    rules = data.get("rules", [{"op": "normalize"}])

    evolved = evolve_layer(pattern, rules)
    buf = render_heightmap(evolved)
    return send_file(buf, mimetype='image/png')

@app.route('/')
def index():
    return jsonify({
        "message": "infiniteOS protótipo ativo",
        "endpoints": {
            "POST /simulate": "Envia pattern + regras e retorna heightmap PNG"
        }
    })

# ---- Execução --------------------------------------------------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
