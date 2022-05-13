from uuid import UUID, uuid4
from datetime import datetime
from dotenv import load_dotenv
from boto3 import client, resource
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from fastapi import APIRouter, Depends, HTTPException
from 
from os import getenv
load_dotenv()


class Default:
    def get_id():
        return str(uuid4())
    def get_date():
        return datetime.now().strftime("%Y-%m-%d")
    def get_time():
        return datetime.now().strftime("%H:%M:%S")
    def get_datetime():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def get_timestamp():
        return datetime.now().timestamp()
    
class env:
    AWS_ACCESS_KEY_ID = getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = getenv("AWS_REGION")
    AWS_S3_BUCKET_NAME = getenv("AWS_S3_BUCKET_NAME")
    AWS_COGNITO_USER_POOL_ID = getenv("AWS_COGNITO_USER_POOL_ID")
    AWS_COGNITO_CLIENT_ID = getenv("AWS_COGNITO_CLIENT_ID")
    AWS_COGNITO_CLIENT_SECRET = getenv("AWS_COGNITO_CLIENT_SECRET")
    AWS_SES_MAIL_FROM = getenv("AWS_SES_MAIL_FROM")
    AWS_SES_MAIL_TO = getenv("AWS_SES_MAIL_TO")
    APP_PORT = getenv("APP_PORT")
    AWS_COGNITO_REDIRECT_URI = getenv("AWS_COGNITO_REDIRECT_URI")
    AWS_COGNITO_TOKEN_URL = getenv("AWS_COGNITO_TOKEN_URL") 
    AWS_COGNITO_ISSUER = getenv("AWS_COGNITO_ISSUER")
    AWS_COGNITO_JWKS_URL = getenv("AWS_COGNITO_JWKS_URL")
    AWS_COGNITO_HOSTED_UI = getenv("AWS_COGNITO_HOSTED_UI")
    AWS_FRONTEND_URL = getenv("AWS_FRONTEND_URL")
    
class AWS:
    def __init__(self, service: str):
        self.env = env()
        self.resource = resource(service,
                                    aws_access_key_id=self.env.AWS_ACCESS_KEY_ID,
                                    aws_secret_access_key=self.env.AWS_SECRET_ACCESS_KEY,
                                    region_name=self.env.AWS_REGION)
        self.client = client(service,
                                aws_access_key_id=self.env.AWS_ACCESS_KEY_ID,
                                aws_secret_access_key=self.env.AWS_SECRET_ACCESS_KEY,
                                region_name=self.env.AWS_REGION)
    def get_resource(self, service: str):
        return resource(service 
                            , aws_access_key_id=self.env.AWS_ACCESS_KEY_ID
                            , aws_secret_access_key=self.env.AWS_SECRET_ACCESS_KEY
                            , region_name=self.env.AWS_REGION)
    def get_client(self, service: str):
        return client(service
                            , aws_access_key_id=self.env.AWS_ACCESS_KEY_ID
                            , aws_secret_access_key=self.env.AWS_SECRET_ACCESS_KEY
                            , region_name=self.env.AWS_REGION)
