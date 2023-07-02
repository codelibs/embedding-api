import logging
import os
from typing import Any, List, Optional

from embedding_api.models import Docs
from numpy import ndarray
from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)


class EmbeddingService:
    def __init__(self) -> None:
        self._model_name: str = os.getenv("MODEL_NAME", "all-MiniLM-L6-v2")
        logger.info(f"Loading {self._model_name}")
        cache_dir: str = os.getenv("MODEL_CACHE_DIR", "/code/model")
        self._model = SentenceTransformer(self._model_name, cache_folder=cache_dir)

    def get_model_name(self) -> str:
        return self._model_name

    def get_sentence_embedding_dimension(self) -> Optional[Any]:
        return self._model.get_sentence_embedding_dimension()

    def encode(self, docs: Docs) -> List[List[float]]:
        embeddings: ndarray = self._model.encode(docs.sentences)
        return embeddings.tolist()


embedding_service: EmbeddingService = EmbeddingService()


async def get_embedding_service() -> EmbeddingService:
    return embedding_service
