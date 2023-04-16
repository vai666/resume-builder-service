# pylint: disable=missing-docstring
# pylint: disable=bare-except

from functools import wraps
from flask import request, abort
from pyrebase import pyrebase


def requires_auth(function):
    @wraps(function)
    def decorated(*args, **kwargs):
        id_token = request.headers.get('Authorization', None)
        auth: pyrebase.Auth = kwargs.get('auth')
        if not id_token:
            abort(401, 'Authorization header is required')
        try:
            auth_token = id_token.split('Bearer ')[1]
            user = auth.get_account_info(auth_token.strip())
            kwargs["email"] = user["users"][0]["email"]
        except:
            abort(401, 'Invalid token')
        return function(*args, **kwargs)
    return decorated