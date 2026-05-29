from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import posts, snippets

app = FastAPI(title="DevShare API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

app.include_router(posts.router)
app.include_router(snippets.router)


@app.get("/")
def root():
    return {"message": "Welcome to DevShare API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
