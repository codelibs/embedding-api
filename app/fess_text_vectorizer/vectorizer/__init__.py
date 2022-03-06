from abc import ABC, abstractmethod
from typing import List

import spacy


class Vectorizer(ABC):

    @abstractmethod
    def vectorize(self, texts: List[str]) -> List[List[float]]:
        pass


class TransformerVectorizer(Vectorizer):
    def __init__(self, name: str) -> None:
        self._nlp = spacy.load(name)

    def vectorize(self, texts: List[str]) -> List[List[float]]:
        return [self._nlp(x)._.trf_data.tensors[0][0, 0, :].tolist() for x in texts]
