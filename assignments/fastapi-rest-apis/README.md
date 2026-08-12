# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework to manage a collection of resources. Students will learn how to define routes, validate request data, and return JSON responses with appropriate HTTP status codes.

## 📝 Tasks

### 🛠️ Create a FastAPI App

#### Description
Create a new FastAPI application that runs locally and exposes a basic API for managing a list of books or tasks.

#### Requirements
Completed program should:

- Import and initialize a `FastAPI` application.
- Define a root endpoint that returns a welcome message.
- Start the app using Uvicorn or the development server command.
- Confirm the app responds with JSON data in the browser or through a local HTTP request.

### 🛠️ Add CRUD Endpoints

#### Description
Implement routes to create, read, update, and delete items from an in-memory collection.

#### Requirements
Completed program should:

- Create a `GET /items` endpoint that returns all items.
- Create a `POST /items` endpoint that adds a new item.
- Create a `GET /items/{item_id}` endpoint that returns a single item by ID.
- Create a `PUT /items/{item_id}` endpoint that updates an existing item.
- Create a `DELETE /items/{item_id}` endpoint that removes an item.
- Return JSON responses using valid Python dictionaries.

### 🛠️ Validate Data and Handle Errors

#### Description
Improve the API by validating user input and returning useful error responses for invalid requests.

#### Requirements
Completed program should:

- Use `pydantic` models to validate request payloads.
- Require fields such as `title`, `description`, or similar values.
- Return a `404` status code when an item is not found.
- Return a `400` or `422` status code for invalid input data.
- Add at least one example request and response in the project documentation.
