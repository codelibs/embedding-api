import time
from typing import Any, Dict, List

from fastapi import APIRouter, Depends

import fess_text_vectorizer
from fess_text_vectorizer.models import Docs

from .services import EmbeddingService, get_embedding_service

api_router = APIRouter()


@api_router.get('/')
async def index():
    return {"version": fess_text_vectorizer.__version__}


@api_router.get('/ping')
async def ping(embedding_service: EmbeddingService = Depends(get_embedding_service)):
    results: List[Dict[str, Any]] = embedding_service.vectorize(
        [{"lang": "en", "content": "test"}])
    return {"status": "ok" if results[0].get("content") is not None else "fail"}


@api_router.post('/vectorize')
async def vectorize(docs: Docs, embedding_service: EmbeddingService = Depends(get_embedding_service)):
    start: float = time.time()
    results: List[Dict[str, Any]] = embedding_service.vectorize(docs)
    return {
        "took": time.time()-start,
        "results": results,
    }
