from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the library management system!"}


@app.get("/books/all-isbn")
async def get_isbn():
    return {"isbn_list": [111, 123, 333, 543]}


# Multiple paths can be used with same root
# Paths are executed in sequence, so if the above paths are not matched, this function is executed
@app.get("/books/{isbn}")
async def get_isbn(isbn: int):
    return {"isbn": isbn}


class AuthorName(str, Enum):
    abercrombie = "abercrombie"
    rowling = "rowling"
    backman = "backman"


# ENUMs can be used to restrict the possible values for path parameters
@app.get("/authors/{author_name}")
async def get_author(author_name: AuthorName):
    if author_name is AuthorName.abercrombie:
        return {
            "author_name": author_name,
            "message": "I write the best fantasy fiction!",
        }

    if author_name.value == "backman":
        return {
            "author_name": author_name,
            "message": "I can move you through my words",
        }

    return {
        "author_name": author_name,
        "message": "I'm just another author who got famous somehow",
    }


# Query parameters can be defined by passing any parameters to the route handler that isn't part of the path parameters
books_by_author = {
    AuthorName.abercrombie: [
        "The Blade Itself",
        "Before They Are Hanged",
        "Last Argument of Kings",
    ],
    AuthorName.rowling: [
        "The Sorcerer's Stone",
        "The Chamber of Secrets",
        "The Prizoner of Azkaban",
        "The Goblet of Fire",
        "The Order of the Phoenix",
        "The Half-Blood Prince",
        "The Deathly Hallows",
    ],
    AuthorName.backman: [
        "A Man Called Ove",
        "Anxious People",
        "Beartown",
        "Us Against You",
        "The Winners",
    ],
}
print(books_by_author)


@app.get("/authors/{author_name}/books")
async def get_books_of_author(author_name: AuthorName, skip: int = 0, limit: int = 10):
    return {
        "author_name": author_name,
        "books": books_by_author[author_name][skip : skip + limit],
        "skip": skip,
        "limit": limit,
    }
