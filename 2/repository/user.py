from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User as UserModel
from schemas.user import User as UserSchema
from uuid import uuid4

async def generate_unique_login(username:str) -> str:
    unique_id = uuid4().hex
    return f"{username}-{unique_id[:15]}"

async def create_user(username: str, session: AsyncSession) -> UserSchema:
    token = str(uuid4())
    login = await generate_unique_login(username)
    user = UserModel(token=token, login=login, username=username)
    session.add(user)
    await session.commit()
    return UserSchema(**user.__dict__)
