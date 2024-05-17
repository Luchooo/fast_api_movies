""" Movies data """

from models import Category, MovieOut

movies: list[MovieOut] = [
    {
        "id": 1,
        "title": "Avatar",
        "year": 2009,
        "category": Category.ACTION.value
	  },
    {
        "id": 2,
        "title": "Spiderman",
        "year": 2009,
        "category": Category.ACTION.value
    },
    {
        "id": 3,
        "title": "Futbol mas",
        "year": 2009,
        "category": Category.SPORTS.value
    }
]
