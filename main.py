import uvicorn
from fastapi import FastAPI
from routers import book_router, user_router, order_router

app = FastAPI()

# Gắn router
app.include_router(book_router.router, prefix="/api/books", tags=["Books"])
app.include_router(user_router.router, prefix="/api/users", tags=["Users"])
app.include_router(order_router.router, prefix="/api/order", tags=["Order"])

@app.get("/")
def root():
    return {"message": "Welcome to Bookstore API with Firebase"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
