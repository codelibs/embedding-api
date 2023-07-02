import time
from typing import List

from fastapi import APIRouter, Depends

import embedding_api
from embedding_api.models import Docs

from .services import EmbeddingService, get_embedding_service

api_router = APIRouter()


@api_router.get("/")
async def index(embedding_service: EmbeddingService = Depends(get_embedding_service)):
    return {
        "version": embedding_api.__version__,
        "model_name": embedding_service.get_model_name(),
    }


@api_router.get("/ping")
async def ping(embedding_service: EmbeddingService = Depends(get_embedding_service)):
    return {
        "status": "ok"
        if embedding_service.get_sentence_embedding_dimension() is not None
        else "fail"
    }


@api_router.post("/encode")
async def encode(
    docs: Docs, embedding_service: EmbeddingService = Depends(get_embedding_service)
):
    start: float = time.time()
    embeddings: List[List[float]] = embedding_service.encode(docs)
    return {
        "took": time.time() - start,
        "embeddings": embeddings,
    }
