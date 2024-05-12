# Simple-RESTful-FastAPI

This repository contains a simple RESTful API built with FastAPI that manages a database of items, demonstrating basic CRUD (Create, Read, Update, Delete) operations. It showcases best practices in API development with FastAPI along with SQLAlchemy for ORM, providing a practical example for those learning how to build scalable and efficient APIs.

## Features

- **CRUD Operations**: Supports creating, reading, updating, and deleting items.
- **Interactive API Documentation**: Utilizes Swagger UI for automatic interactive documentation accessible through FastAPI.
- **Validation with Pydantic**: Ensures that the API receives and processes only valid data through Pydantic models.

## Installation

### Prerequisites

- Ensure you have Python 3.6+ installed on your machine. You can download Python from [here](https://www.python.org/downloads/).
- `pip` should be available to install necessary packages.

### Setting up a Virtual Environment

It's recommended to use a virtual environment to handle the project dependencies. You can set one up by executing the following commands in your terminal:

**On Unix or MacOS**:

```bash
python -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### Installing Dependencies

Install all required dependencies by running the following command in your virtual environment:

```bash
pip install -r requirements.txt
```

### Running the Application

To start the FastAPI server, execute the following command:

```bash
python main.py
```

This command starts the FastAPI server on `http://127.0.0.1:8000`. You can access the API and see the automatic interactive documentation provided by Swagger UI at `http://127.0.0.1:8000/docs`.

## API Endpoints

Here are the API endpoints provided by this application and their respective HTTP methods:

- **POST /items/**: Creates a new item in the database.
- **GET /items/**: Retrieves a list of all items.
- **GET /items/{item_id}**: Retrieves a specific item by its ID.
- **PUT /items/{item_id}**: Updates an existing item by its ID.
- **DELETE /items/{item_id}**: Deletes an item by its ID.

## Usage Examples

You can interact with the API using any HTTP client. Below are examples of how to call each endpoint using `curl`:

### Create an Item

```bash
curl -X POST http://127.0.0.1:8000/items/ -H 'Content-Type: application/json' -d '{"name": "Item Name", "price": 10.99}'
```

### Retrieve All Items

```bash
curl http://127.0.0.1:8000/items/
```

### Retrieve an Item by ID

```bash
curl http://127.0.0.1:8000/items/{item_id}
```

### Update an Item

```bash
curl -X PUT http://127.0.0.1:8000/items/{item_id} -H 'Content-Type: application/json' -d '{"name": "New Item Name", "price": 11.99}'
```

### Delete an Item

```bash
curl -X DELETE http://127.0.0.1:8000/items/{item_id}
```

This README should provide all the necessary information to get the API up and running quickly and begin interacting with it.
