from pydantic import BaseModel,Field
from typing import Annotated

class Ollama_driving(BaseModel):
    age : Annotated[int,Field(...,description="Enter the Age.",examples=[21])]

    