# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['foo', 'Person']

# %% ../nbs/00_core.ipynb 3
import pydantic
from datetime import datetime

# %% ../nbs/00_core.ipynb 4
def foo(): pass

# %% ../nbs/00_core.ipynb 5
class Person(pydantic.BaseModel):
    id: int
    name: str 
    email: str
    phone: str
    met_ts: datetime
