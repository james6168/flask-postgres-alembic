from pydantic import BaseModel, field_validator
from typing import Optional, ClassVar
from re import fullmatch


class UserScheme(BaseModel):

    USERNAME_REGEX: ClassVar[str] = r"^(?=.*[A-Za-z0-9]).{3,30}$"
    PASSWORD_REGEX: ClassVar[str] = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    EMAIL_REGEX: ClassVar[str] = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    model_config = {
        "extra": "forbid"
    }


    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None



    @field_validator("username")
    def validate_username(cls, v):

        if v is None:
            raise ValueError("Username cannot be none")

        if not fullmatch(cls.USERNAME_REGEX, v):
            raise ValueError("Username must be 3–30 characters long, alphanumeric only")
        
        return v
    

    @field_validator("email")
    def validate_email(cls, v):

        if v is None:
            raise ValueError("Email cannot be none")
        
        if not fullmatch(cls.EMAIL_REGEX, v):
            raise ValueError("Invalid email")
        
        return v
    

    @field_validator("password")
    def validate_password(cls, v):
        
        if v is None:
            raise ValueError("Password cannot be none")
        
        if not fullmatch(cls.PASSWORD_REGEX, v):
            raise ValueError("Invalid password, password should be minimum eight characters, at least one letter and one number")
        
        return v
    


class RegisterUserScheme(UserScheme):


    username: str
    email: str
    password: str
    

    
    





