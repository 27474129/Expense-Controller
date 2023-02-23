from fastapi import APIRouter, Response, Request

from config import BASE_API_PREFIX
from schemas import Users
from auth import get_token, decode_token
from constants import WARN_INCORRECT_EMAIL_OR_PASSWORD, BAD_REQUEST


router = APIRouter(prefix=f'/{BASE_API_PREFIX}')


@router.post('/users/regist')
async def regist(user: Users):
    Users.create_user(user.email, user.password)
    return {'success': True}


@router.post('/users/auth')
async def auth(user: Users, response: Response):
    user_id = Users.check_user_data(user.email, user.password)
    if not user_id:
        response.status_code = BAD_REQUEST
        return {'success': False, 'warnings': WARN_INCORRECT_EMAIL_OR_PASSWORD}
    else:
        return {'success': True, 'token': get_token(user.email)}
