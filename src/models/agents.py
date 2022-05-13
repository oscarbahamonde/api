from sqlmodel import SQLModel, Field
from typing import List, Dict, Optional
from pydantic impowt EmailStr, HttpUrl
from src.interfaces import Default

default = Default()

class Agent(SQLModel):
    displayName: str = Field(...)
    email: EmailStr = Field(...)

class Contact(Agent):
    message: str = Field(...)
    
class User(Agent):
    id:str = Field(..., primary_key=True)
    photoURL: Optional[HttpUrl] = Field(...)

class Account(User):
    role: str = Field(default="staff")

class Contacts(Contact, table=True)
    id: str = Field(primary_key=True, default_factory=default.get_id)
    updatedAt: str = Field(default_factory=default.get_datetime)
    
class Users(User, table=True)
    updatedAt: str = Field(default_factory=default.get_datetime)
    
class Accounts(Account, table=True)
    updatedAt: str = Field(default_factory=default.get_datetime)