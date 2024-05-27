import numpy as np
from concurrent.futures import ThreadPoolExecutor

def simulate_particle(particle_data):
    # Simula a trajetória de uma partícula
    return np.sum(particle_data ** 2)

def parallel_simulation(num_particles, num_threads):
    particles = np.random.rand(num_particles, 3)
    
    chunk_size = num_particles // num_threads
    chunks = [particles[i*chunk_size:(i+1)*chunk_size, :] for i in range(num_threads)]
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(simulate_particle, chunks))
    
    return np.sum(results)

# Exemplo de uso
result = parallel_simulation(10000, 4)
print("Resultado da simulação:", result)
