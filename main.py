import uvicorn
from fastapi import FastAPI
from routers import book_router, user_router, cart_router

app = FastAPI()

# Gắn router
app.include_router(book_router.router, prefix="/api/books", tags=["Books"])
app.include_router(user_router.router, prefix="/api/users", tags=["Users"])
app.include_router(cart_router.router, prefix="/api/cart", tags=["Cart"])

@app.get("/")
def root():
    return {"message": "Welcome to Bookstore API with Firebase"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
