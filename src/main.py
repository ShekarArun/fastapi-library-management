from fastapi import FastAPI

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
