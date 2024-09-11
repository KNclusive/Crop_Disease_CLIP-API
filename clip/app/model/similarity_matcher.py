import nmslib
from pathlib import Path
from app.model.config import embeddings, current_dir, image_paths

def embedding_index():
    index = nmslib.init(method='hnsw', space='cosinesimil')
    index.addDataPointBatch(embeddings)
    index.createIndex({'post': 2}, print_progress=True)
    return index

def similarity(index, query_embedding, k):
    indices, _ = index.knnQuery(query_embedding, k=k)
    return [image_paths[idx] for idx in indices]