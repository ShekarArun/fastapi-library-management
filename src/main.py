from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the library management system!"}


@app.get("/books/{isbn}")
async def get_isbn(isbn: int):
    return {"isbn": isbn}
