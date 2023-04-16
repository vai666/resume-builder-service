from functools import wraps
from flask import request, abort
from pyrebase import pyrebase

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print(kwargs)
        id_token = request.headers.get('Authorization', None)
        auth: pyrebase.Auth = kwargs.get('auth')
        if not id_token:
            abort(401, 'Authorization header is required')
        try:
            auth_token = id_token.split('Bearer ')[1]
            auth.get_account_info(auth_token.strip())
        except:
            abort(401, 'Invalid token')
        return f(*args, **kwargs)
    return decorated