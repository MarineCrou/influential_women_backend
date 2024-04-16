from http import HTTPStatus
from functools import wraps

import jwt
from flask import g, request
from config.environment import SECRET

from app import db
from models.user_model import UserModel


def secure_route_contributor(route_func):
    
    @wraps(route_func)
    def wrapper(*args, **kwargs):

        raw_token = request.headers.get('Authorization') # check if token exists 
        print(raw_token) # Should print the token

        if not raw_token: #if no token, return an unauthorized message
            print("missing token 😢😢😢😢😢")
            return { "message" : "Unauthorized"}, HTTPStatus.UNAUTHORIZED

        token = raw_token.replace('Bearer ', '') # Delete the bearer word in front of the token
        print(token)
        
        try:
            payload = jwt.decode(token, SECRET, "HS256")
            print('token is valid 🎉🎉🎉🎉', payload)

            #getting the user :
            user_id = payload['sub'] # If we want to have a user later to do things like check permissions, we should get the user from the token.
            user = db.session.query(UserModel).get(user_id) # Get the user with this ID
            g.current_user = user  # Attach this user to the request, so we can use it later.
            if user.role == 'contributor':
                return route_func(*args, **kwargs)
            else:
                return {"message": "You do not have permission to access this resource"}, 403
        

        except jwt.ExpiredSignatureError:
            print("Expired")
            return {"message": "Token has expired"}, HTTPStatus.UNAUTHORIZED
        except Exception:
            print("Issue with token")
            return {"message": "Unauthorized 🎉"}, HTTPStatus.UNAUTHORIZED

        
    return wrapper