import numpy as np
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

def apply_filter(image_chunk):
    # Aplica um filtro simples a um pedaço da imagem
    return np.where(image_chunk < 128, 0, 255)

def parallel_image_processing(image_path, num_threads):
    image = Image.open(image_path).convert('L')
    image_array = np.array(image)
    height, width = image_array.shape

    chunk_size = height // num_threads
    chunks = [image_array[i*chunk_size:(i+1)*chunk_size, :] for i in range(num_threads)]
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        processed_chunks = list(executor.map(apply_filter, chunks))
    
    processed_image = np.vstack(processed_chunks)
    return Image.fromarray(processed_image)

# Exemplo de uso
processed_image = parallel_image_processing('imagem_exemplo.jpg', 4)
processed_image.show()
