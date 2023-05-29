from pydub import AudioSegment
from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import uuid4
from models.record import Record
from sqlalchemy import select
from models.user import User
from fastapi.responses import FileResponse


async def save_record(login: str, token:str, record: UploadFile, session: AsyncSession ):
    if not record.filename.lower().endswith(".wav"):
        raise TypeError("File must be a .wav file")
    
    user = await session.execute(select(User).where(User.login == login and User.token == token))
    user = user.scalars().first()

    if not user:
        raise ValueError("User with this login and token not found")
    
    username = user.username
    audio = AudioSegment.from_wav(record.file, format="wav")
    name = str(uuid4())
    audio.export(f"record/{name}.mp3", format="mp3")
    record = Record(uuid=name, user=login)
    session.add(record)
    await session.commit()

    return {"message": f"http://localhost:8000/record?id={name}&user={username}"}

async def get_record(id: str, user: str, session: AsyncSession):
    record = await session.execute(select(Record).where(Record.uuid == id and Record.user == user))
    record = record.scalars().first()

    if not record:
        raise ValueError("Record not found")
    
    return FileResponse(f"record/{id}.mp3")
