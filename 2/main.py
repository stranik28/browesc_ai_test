from fastapi import FastAPI
from routers.record import router as record
from routers.user import router as user
from database.database import create_tables

app = FastAPI(
    title="bewise ai Second task"
)

@app.on_event("startup")
async def startup():
    await create_tables()

app.include_router(record)
app.include_router(user)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

