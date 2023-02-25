import time
import jwt
from typing import Dict

from config import JWT_SECRET, JWT_ALGORITHM


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
