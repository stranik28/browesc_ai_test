from fastapi import APIRouter, Depends, HTTPException
from schemas.quize import Quize
from repository.quize import add_questions_r
from database.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Union

router = APIRouter(
    prefix="/questions",
    tags=["quize"]
)

@router.post("/")
async def add_questions(questions_num: int , session: AsyncSession = Depends(get_async_session)) -> Union[Quize,None]:
    '''
        Function fo adding questions to database
    '''
    if questions_num < 1:
        raise HTTPException(status_code=422, detail="Number of questions must be greater than 0")
    try:
        response = await add_questions_r(questions_num, session)
        return response
    except ValueError as e:
        raise HTTPException(status_code=404, detail=e.args[0])