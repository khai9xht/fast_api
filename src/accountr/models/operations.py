from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class BaseOperation(BaseModel):
    date: date
    kind: str
    amount: int


class OperationCreate(BaseOperation):
    pass


class OperationUpdate(BaseOperation):
    pass


class Operation(BaseOperation):
    ids: int

    class Config:
        orm_mode = True
