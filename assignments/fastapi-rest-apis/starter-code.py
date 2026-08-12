from fastapi import FastAPI

app = FastAPI(title="Task API")

# In-memory storage for tasks
items = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build a REST API", "done": True},
]


@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}


# TODO: Add endpoints for GET /items, POST /items, GET /items/{item_id}
# TODO: Add PUT /items/{item_id} and DELETE /items/{item_id}
# TODO: Add validation and error handling for invalid requests
