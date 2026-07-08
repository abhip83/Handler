from fastapi import FastAPI

from app.api.v1.emails import router as emails_router


app = FastAPI(
    title="Handler API",
    description="AI-powered email operations platform for logistics companies",
    version="0.1.0",
)

app.include_router(
    emails_router,
    prefix="/api/v1"
)


@app.get("/")
def root():
    return {"message": "Welcome to Handler API"}


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "handler-api",
        "version": "0.1.0"
    }