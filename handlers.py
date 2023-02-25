from fastapi import APIRouter, Response, Request

from config import BASE_API_PREFIX
from schemas import Users, Categories
from auth import get_token, decode_token
from constants import (
    WARN_INCORRECT_EMAIL_OR_PASSWORD, BAD_REQUEST, NOT_AUTHORIZED,
    ERR_NOT_AUTHORIZED
)


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
        return {'success': True, 'token': get_token(user_id=user_id, email=user.email)}


@router.post('/users/is_auth')
async def is_auth(token: str, response: Response):
    if not decode_token(token):
        response.status_code = NOT_AUTHORIZED
        return {'success': False, 'errors': ERR_NOT_AUTHORIZED}
    return {'success': True}


@router.post('/categories')
async def create_category(
    category: Categories, request: Request, response: Response
):
    decoded_token = decode_token(
        request.headers.get('Authorization').split()[1]
    )

    if not decoded_token:
        response.status_code = NOT_AUTHORIZED
        return {'success': False, 'errors': ERR_NOT_AUTHORIZED}

    Categories.create_category(
        user_id=decoded_token['user_id'], name=category.name,
        amount_limit=category.amount_limit, time_distance=category.time_distance
    )

    return {'success': True}


@router.put('/categories')
async def update_category(
    name: str, request: Request, response: Response
):
    decoded_token = decode_token(
        request.headers.get('Authorization').split()[1]
    )
    if not decoded_token:
        response.status_code = NOT_AUTHORIZED
        return {'success': False, 'errors': ERR_NOT_AUTHORIZED}

    return Categories.find_category_by_name(name, decoded_token['user_id'])
