from pydantic import BaseModel, Field


class MovieModel(BaseModel):
    id: int = Field(gt=0)
    title: str = Field(max_length=120)
    director: str = Field(max_length=120)
    category: str = Field(max_length=120)
    rating: int = Field(gt=0, lt=6)
    release_year: int = Field(gt=1900)

    class Config:
        json_schema_extra = {
            'example': {
                "id": 1,
                "title": "Las Vegas Parano",
                "director": "Steve Buscemi",
                "category": "horror",
                "rating": 5,
                "release_year": 2024
            }
        }
