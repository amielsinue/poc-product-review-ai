from pydantic import BaseModel


class ReviewRequest(BaseModel):
    content: str
