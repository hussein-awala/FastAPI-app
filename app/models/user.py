from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    firstname: str = Field(...)
    lastname: str = Field(...)
    email: EmailStr = Field(...)
    birth_year: int = Field(..., gt=1900, lt=2100)

    class Config:
        schema_extra = {
            "example": {
                "firstname": "Hussein",
                "lastname": "Awala",
                "email": "houssein.awala.96@gmail.com",
                "birth_year": 1996,
            }
        }


class UpdateUserModel(BaseModel):
    firstname: Optional[str]
    lastname: Optional[str]
    email: Optional[EmailStr]
    birth_year: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "firstname": "Hussein",
                "lastname": "Awala",
                "email": "houssein.awala.96@gmail.com",
                "birth_year": 1996,
            }
        }
