from typing import List, Optional

from pydantic import BaseModel


class Doc(BaseModel):
    lang: Optional[str] = None
    content: Optional[str] = None


class Docs(BaseModel):
    data: List[Doc]
