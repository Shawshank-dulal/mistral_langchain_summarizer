from fastapi import FastAPI
from pydantic import BaseModel
from utils import get_processed_transcript
from summarizer import get_summary


class Item(BaseModel):
    url: str


app = FastAPI()


@app.post("/summary/")
async def create_item(item: Item):
    transcript = get_processed_transcript(item.url)

    response = get_summary(transcript)
    return response
