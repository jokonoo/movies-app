from fastapi import FastAPI, HTTPException
import uvicorn
from models import MovieModel

app = FastAPI()

movies = [
    {"id": 1, "title": "Title first", "director": "Director first", "category": "Category first", "rating": 4,
     "release_year": 2017},
    {"id": 2, "title": "Title second", "director": "Director second", "category": "Category second", "rating": 3,
     "release_year": 2019},
    {"id": 3, "title": "Title third", "director": "Director third", "category": "Category third", "rating": 5,
     "release_year": 2022}
]


@app.get("/movies")
def get_movies():
    return movies


@app.get("/movies/{movie_id}")
def get_movie_by_id(movie_id: int):
    for movie in movies:
        if movie.get("id") == movie_id:
            return movie
        raise HTTPException(status_code=404, detail=f"Movie with id: {movie_id} does not exist")


@app.post("/movies/create")
def post_movies(movie: MovieModel):
    movie_data = movie.model_dump()
    movies.append(movie_data)
    return movie_data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
