from fastapi import APIRouter

api  = APIRouter()

@api.get('/')
async def start_api():
    return {
        'start': 'hello world'
    }