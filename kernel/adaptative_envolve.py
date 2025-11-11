def evolve_adaptive(layer, kernel, step):
    # 1. Evolui com o kernel atual
    from scipy.signal import convolve2d
    evolved = convolve2d(layer, kernel, mode='same', boundary='wrap')

    # 2. Normaliza o resultado
    evolved = evolved - np.min(evolved)
    evolved /= np.max(evolved)

    # 3. Calcula métricas locais
    avg = np.mean(evolved)
    variance = np.var(evolved)

    # 4. Adapta o kernel conforme a resposta
    adapt_factor = 1 + (avg - 0.5) * 0.3
    kernel = kernel * adapt_factor

    # 5. Introduz ruído controlado (para não estabilizar cedo)
    noise = np.random.normal(0, variance * 0.05, kernel.shape)
    kernel = kernel + noise

    # 6. Re-normaliza o kernel
    kernel /= np.max(np.abs(kernel))

    return evolved, kernel
