from typing import Any, Dict, List, Optional

from fess_text_vectorizer.models import Docs
from fess_text_vectorizer.vectorizer import TransformerVectorizer, Vectorizer

_DEFAULT_LANG: str = "en"


class EmbeddingService:
    def __init__(self) -> None:
        self._vectorizers: Dict[str, Vectorizer] = {}

        self._vectorizers["en"] = TransformerVectorizer("en_core_web_trf")
        self._vectorizers["ja"] = TransformerVectorizer("ja_ginza_electra")

    def get_languages(self) -> List[str]:
        return list(self._vectorizers.keys())

    def vectorize(self, docs: Docs) -> List[Dict[str, Any]]:
        results: List[Dict[str, Any]] = []
        # TODO bulk
        for doc in docs.data:
            content: Optional[str] = doc.content
            if content is None:
                results.append({
                    "content": None
                })
                continue
            lang: Optional[str] = doc.lang
            if lang not in self._vectorizers:
                lang = _DEFAULT_LANG
            vectorizer: Vectorizer = self._vectorizers.get(lang)
            vectors: List[List[float]] = vectorizer.vectorize([content])
            results.append({
                "content": vectors[0]
            })
        return results


embedding_service: EmbeddingService = EmbeddingService()


async def get_embedding_service() -> EmbeddingService:
    return embedding_service
