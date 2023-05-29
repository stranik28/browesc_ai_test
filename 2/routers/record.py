from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Query
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_async_session
from repository.record import save_record as save_record_rep
from repository.record import get_record as get_record_rep
from fastapi.responses import FileResponse

router = APIRouter(
    tags=["record"]
)

@router.post("/record")
async def save_record(login: str, token:str, record: UploadFile = File(...),  session: AsyncSession = Depends(get_async_session)):
    '''
        Save wav record to mp3
    '''
    try:
        print("Validate")
        return await save_record_rep(login, token, record, session)
    except ValueError as e:
        raise HTTPException(status_code=404 , detail=e.args[0])
    except TypeError as e:
        raise HTTPException(status_code=400 , detail=e.args[0])

@router.get("/record")
async def get_record(id: str = Query(..., description="Record ID"), user: str = Query(..., description="User ID"), session: AsyncSession = Depends(get_async_session))-> FileResponse:
    try:
        return await get_record_rep(id, user, session)
    except ValueError as e:
        raise HTTPException(status_code=404 , detail=e.args[0])

