from fastapi import FastAPI
from app.agent import PolishAgent
from app.schemas import PolishRequest, PolishResponse

app = FastAPI()

agent = PolishAgent()

@app.post("/polish", response_model=PolishResponse)
def polish(req: PolishRequest):
    return agent.polish(req.text)
