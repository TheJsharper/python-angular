from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Project 03",
    description="FastAPI sample project with simple dev/prod scripts",
    version="1.0.0",
)


@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "ok"})
