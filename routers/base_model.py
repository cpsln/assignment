from pydantic import BaseModel

class ChapterRating(BaseModel):
    name: str
    rating: int
    