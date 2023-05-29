from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_async_session
from schemas.user import User 
from repository.user import create_user as create_user_rep

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("/")
async def create_user(username: str, session: AsyncSession = Depends(get_async_session)) -> User:
    ''' 
        Router to create user
    '''
    user = await create_user_rep(username, session)
    return user