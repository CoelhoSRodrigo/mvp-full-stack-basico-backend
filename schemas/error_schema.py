from pydantic import BaseModel


class ErrorSchema(BaseModel):
    '''Eschema que representa como um erro será retornado pela API Tarefa'''
    error_msg: str