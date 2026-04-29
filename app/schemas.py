from pydantic import BaseModel

class PolishRequest(BaseModel):
    text: str

class PolishResponse(BaseModel):
    formal: str
    neutral: str
    friendly: str
