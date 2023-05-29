import requests
from models.quize import Quize
from schemas.quize import Quize as QuizeSchema
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def make_request(number_of_questions: int) -> list:
    '''
        Function for making request to https://jservice.io/api/random?count={number_of_questions}
        :param number_of_questions: int 
        :return: list of questions
    '''
    body = f"https://jservice.io/api/random?count={number_of_questions}"
    req = requests.get(body)
    if req.status_code == 200:
        return req.json()
    else: 
        raise ValueError("Error in request")
    
async def save_quize(session: AsyncSession, req) -> int:
    '''
        Function for saving questions to database
        :param session: AsyncSession
        :param req: list of questions
        :return: number of dublicate questions
    '''
    dublicate = 0
    for i in req:
        in_db = await session.execute(select(Quize).where(Quize.id == i["id"]))
        in_db = in_db.scalars().first()
        if in_db:
            dublicate += 1
            continue
        quize = QuizeSchema(**i)
        quize = Quize(**quize.__dict__)
        session.add(quize)
    return dublicate

async def add_questions_r(number_of_questions: int, session: AsyncSession) -> QuizeSchema :
    '''
        Function for saving questions 
        :param number_of_questions: int
        :param session: AsyncSession
        :return: QuizeSchema object
    '''
    dublicate = number_of_questions
    while dublicate != 0:
        req = await make_request(dublicate)
        dublicate = await save_quize(session, req)
    await session.commit()
    return QuizeSchema(**req[-1])