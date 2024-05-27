import pandas as pd
from concurrent.futures import ThreadPoolExecutor

def process_data_chunk(data_chunk):
    # Processa um pedaço dos dados (ex: calculando a média de uma coluna)
    return data_chunk['valor'].mean()

def parallel_data_processing(data_path, num_threads):
    data = pd.read_csv(data_path)
    
    chunk_size = len(data) // num_threads
    chunks = [data[i*chunk_size:(i+1)*chunk_size] for i in range(num_threads)]
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(process_data_chunk, chunks))
    
    return sum(results) / len(results)

# Exemplo de uso
average_value = parallel_data_processing('dados_exemplo.csv', 4)
print("Valor médio processado:", average_value)
