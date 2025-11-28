

import ast
import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, field_validator

class Product(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    product_id: str
    product_name: str
    description: str
    type: str
    status: str
    audience: str
    products_types: str  
    installation: str

    embedding: Optional[list[float]] = None

    @field_validator("embedding", mode="before")
    def validate_embedding(cls, v):
        if isinstance(v, str):
            try:

                v = ast.literal_eval(v)
                v = [float(f) for f in v]
            except (ValueError, SyntaxError):
                return None
        return v