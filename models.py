""" Define Movie Model """
from enum import Enum

from pydantic import BaseModel, Field

class Category(str, Enum):
    """ Category class """
    ACTION = "Acción"
    SPORTS = "Deportes"
    LOVE = "Romance"


class MovieIn(BaseModel):
    """ Class Movie int """   
    title: str = Field(min_length=5, max_length=15)
    year: int = Field(le=2022, ge=2000)
    category: Category

    class Config:
        """ Config values to docs """
        json_schema_extra = {
            "example": {
                "title": "Mi pelicula",
                "year": 2022,
		        "category": "Acción"
            }
        }

        extra = "forbid"

class MovieOut(MovieIn):
    """ Class Movie out """   
    id: int

    class Config:
        """ Config values to docs """
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi pelicula",
                "year": 2022,
		        "category": "Acción"
            }
        }
