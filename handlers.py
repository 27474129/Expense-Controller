import logging

from fastapi import APIRouter, Response, Request

from config import BASE_API_PREFIX
from schemas import Users, Categories
from auth import get_token, decode_token, get_decoded_token
from constants import (
    WARN_INCORRECT_EMAIL_OR_PASSWORD, BAD_REQUEST, NOT_AUTHORIZED,
    ERR_NOT_AUTHORIZED, ERR_CANT_UPDATE_OBJECT, WARN_CANT_FIND_OBJECT,
    WARN_OBJECT_ALREADY_EXISTS
)
from utils import convert_fields_for_update

logger = logging.getLogger(__name__)


router = APIRouter(prefix=f'/{BASE_API_PREFIX}')


@router.post('/users/regist')
async def regist(user: Users):
    Users.create_user(user.email, user.password)
    logger.info('Successfully created user')
    return {'success': True}


@router.post('/users/auth')
async def auth(user: Users, response: Response):
    user_id = Users.check_user_data(user.email, user.password)
    if not user_id:
        response.status_code = BAD_REQUEST
        logger.info(f'Warning: {WARN_INCORRECT_EMAIL_OR_PASSWORD}')
        return {'success': False, 'warnings': WARN_INCORRECT_EMAIL_OR_PASSWORD}
    else:
        logger.info('Successfully authorized')
        return {'success': True, 'token': get_token(user_id=user_id, email=user.email)}


@router.post('/users/is_auth')
async def is_auth(token: str, response: Response):
    if not decode_token(token):
        response.status_code = NOT_AUTHORIZED
        return {'success': False, 'errors': ERR_NOT_AUTHORIZED}

    logger.info('Successfully authorized')
    return {'success': True}


@router.get('/categories')
async def get_categories(response: Response, request: Request):
    """Getting all categories for current user."""

    decoded_token = get_decoded_token(request, response)
    if decoded_token.get('errors'):
        return decoded_token

    categories = Categories.get_categories(decoded_token['user_id'])

    serialized_categories = [Categories(
        name=category[0],
        amount_limit=category[1],
        current_amount=category[2],
        time_distance=category[3]
    ) for category in categories]

    return {'success': True, 'categories': serialized_categories}


@router.get('/categories/{name}')
async def get_category(name: str, response: Response, request: Request):
    """Getting category for current user."""

    decoded_token = get_decoded_token(request, response)
    if decoded_token.get('errors'):
        return decoded_token

    category = Categories.get_category(name)

    serialized_category = Categories(
        name=category[0],
        amount_limit=category[1],
        current_amount=category[2],
        time_distance=category[3]
    )

    return {'success': True, 'category': serialized_category}


@router.post('/categories')
async def create_category(
    category: Categories, request: Request, response: Response
):
    decoded_token = get_decoded_token(request, response)
    if decoded_token.get('errors'):
        return decoded_token

    if Categories.check_if_category_exists(
        user_id=decoded_token['user_id'], name=category.name
    ):
        return {'success': False, 'warnings': WARN_OBJECT_ALREADY_EXISTS}

    Categories.create_category(
        user_id=decoded_token['user_id'], name=category.name,
        amount_limit=category.amount_limit, time_distance=category.time_distance
    )

    logger.info('Successfully created category')
    return {'success': True}


@router.put('/categories/{name}')
async def update_category(
    name: str, fields: dict, request: Request, response: Response
):
    decoded_token = get_decoded_token(request, response)
    if decoded_token.get('errors'):
        return decoded_token

    updatable_fields = ['name', 'amount_limit', 'current_amount', 'time_distance']
    fields_for_update = convert_fields_for_update(fields, updatable_fields)

    if Categories.update_category(
        fields_for_update, decoded_token['user_id'], name
    ):
        logger.info('Successfully updated category')
        return {'success': True}
    else:
        response.status_code = BAD_REQUEST
        return {'success': False, 'errors': ERR_CANT_UPDATE_OBJECT}


@router.delete('/categories/{name}')
async def delete_category(name: str, request: Request, response: Response):
    decoded_token = get_decoded_token(request, response)
    if decoded_token.get('errors'):
        return decoded_token

    category_id = Categories.check_if_category_exists(
        name, decoded_token['user_id']
    )
    if not category_id:
        return {'success': False, 'warnings': WARN_CANT_FIND_OBJECT}

    Categories.delete_category(category_id)
    return {'success': True}
