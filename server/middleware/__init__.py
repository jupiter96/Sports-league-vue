import bcrypt
import jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv('APP_SECRET')


def create_token(payload):
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def read_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.InvalidSignatureError:
        return "Signature Invalid"
    except jwt.InvalidTokenError:
        return "Token Invalid"


def gen_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def compare_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())


def strip_token(req):
    try:
        token = req.headers['Authorization']
        return token
    except:
        return None
