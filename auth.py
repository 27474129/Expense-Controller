import time
import jwt
from typing import Dict

from fastapi import Request, Response

from config import JWT_SECRET, JWT_ALGORITHM
from constants import NOT_AUTHORIZED, ERR_NOT_AUTHORIZED


def get_token(user_id: int, email: str) -> Dict[str, str]:
    payload = {
        'user_id': user_id,
        'email': email,
        'expires': time.time() + 3600 * 48
    }

    return jwt.encode(
        payload, JWT_SECRET, algorithm=JWT_ALGORITHM
    )


def decode_token(token: str) -> dict or None:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        ...


def get_decoded_token(request: Request, response: Response):
    token = request.headers.get('Authorization')
    if token:
        decoded_token = decode_token(token.split()[1])
    else:
        response.status_code = NOT_AUTHORIZED
        return {'success': False, 'errors': ERR_NOT_AUTHORIZED}

    if not decoded_token:
        response.status_code = NOT_AUTHORIZED
        return {'success': False, 'errors': ERR_NOT_AUTHORIZED}

    return decoded_token
