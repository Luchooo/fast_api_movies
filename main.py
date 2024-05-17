""" Example fast api """
import json
from typing import Annotated

from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import HTMLResponse, JSONResponse

from data import movies
from models import Category, MovieIn, MovieOut

app = FastAPI()
app.title = "Movies CRUD"
app.version = "0.0.1"

@app.get("/", tags=["home"])
def message():
    """ Show home """
    html_content = """
    <html>
        <head>
            <title>FastAPI Movies</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                }
                h1 {
                    color: #333;
                }
                .button {
                    padding: 10px 20px;
                    background-color: #007bff;
                    color: #fff;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to the FastAPI Movies Page!</h1>
            <p>Click the button below to test the API</p>
            <form action="/docs">
                <input type="submit" class="button" value="Test API">
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/movies", tags=["movies"], response_model=list[MovieOut])
def get_movies():
    """ Return all movies """
    return movies


@app.get("/movies/{movie_id}", tags=["movies"], response_model=MovieOut)
def get_movie(movie_id: int = Path(ge=1, le=2000)):
    """ Return a movie by id """
    for movie in movies:
        if movie["id"] == movie_id:
            return MovieOut(**movie)
    raise HTTPException(status_code=404, detail="Movie not found")

@app.get("/movies/", tags=["movies"], response_model=list[MovieOut])
def get_movie_by_category(movie_category: Category):
    """ Return a movie by category """
    return [
        movie for movie in movies
        if movie["category"] == movie_category.value
    ]


@app.post("/movies", tags=["movies"], response_model=dict, status_code=201)
def create_movie(movie: MovieIn):
    """ Create a movie """
    movie_in = json.loads(movie.model_dump_json())
    movie_id = len(movies) + 1
    movie_new = {"id":movie_id, **movie_in}
    movies.append(movie_new)
    return {"message": "Movie created", "movie": movie_new}


@app.put("/movies/{movie_id}", tags=["movies"], response_model=dict)
def update_movie(movie_id: Annotated[int, Path(ge=1)], updated_movie: MovieIn):
    """ Update a movie by id """
    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(json.loads(updated_movie.model_dump_json()))
            return JSONResponse(content={"message": "Movie updated", "movie": movie})
    raise HTTPException(status_code=404, detail="Movie not found")

@app.delete("/movies/{movie_id}", tags=["movies"], response_model=dict)
def delete_movie(movie_id: int):
    """ Delete a movie by id """
    for movie in movies.copy():
        if movie["id"] == movie_id:
            movies.remove(movie)
            return JSONResponse(content={"message": "Movie deleted"})
    raise HTTPException(status_code=404, detail="Movie not found")
