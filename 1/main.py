from fastapi import FastAPI
from routers.quize import router as quize
from database.database import create_tables

app = FastAPI(
    title="bewise ai First task"
)

@app.on_event("startup")
async def startup():
    await create_tables()

app.include_router(quize)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

