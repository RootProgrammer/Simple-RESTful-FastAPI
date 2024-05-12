# Entry point for the application
from fastapi import FastAPI
from routes.item_routes import router as item_router
import uvicorn

app = FastAPI()
app.include_router(item_router)

if __name__ == "__main__":
    config = uvicorn.Config(
        "main:app",  # Application import string
        host="127.0.0.1",  # Host to bind the server
        port=8000,  # Port to listen on
        log_level="info",  # Logging level
        reload=True,  # Enable automatic reload on code changes
    )
    server = uvicorn.Server(config)
    server.run()
