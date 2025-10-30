from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Python Microservice",
    description="A FastAPI microservice created from IDP template",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """
    Root endpoint - returns a simple hello world message.
    """
    return {"message": "Hello World", "status": "healthy"}


@app.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring.
    """
    return {
        "status": "healthy",
        "service": "python-microservice",
        "version": "1.0.0"
    }


@app.get("/api/v1/status")
async def api_status():
    """
    API status endpoint.
    """
    return {
        "api": "v1",
        "status": "operational",
        "version": "1.0.0"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

