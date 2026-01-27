from fastapi import FastAPI
from routers import metrics

app = FastAPI(
    title="Internal DevOps Utilities API",
    description="This is an Internal API Utilities App for Monitoring metrics, AWS Usage, Log Analysis, etc",
    version="1.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)   

@app.get("/")
def hello():
    return {"message": "Hello Dosto, This is Devops utilites API"}


app.include_router(metrics.router)