from pydantic import BaseModel


class ErrorSchema(BaseModel):
    '''Eschema que representa como um erro será retornado pela API Store'''
    error_msg: str