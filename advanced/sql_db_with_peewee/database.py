
"""
Peewee를 통해 Relational DB를 생성한다.
Peewee란?
  - simple and small ORM (Object-Releational Mapping)
Peewee 특징
  - Peewee는 async 처리를 위해 디자인되지 않았음.
  - non-async 기반으로 어플리케이션을 간단하게 개발하고 싶다면 사용할것.

"""
from contextvars import ContextVar

import peewee

DATABASE_NAME = "test.db"
db_state_default = {"closed": None, "conn": None, "ctx": None, "Transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())

class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]

# db 생성 코드 (sqlite db를 생성)
db = peewee.SqliteDatabase(DATABASE_NAME, check_same_thread=False)

db._state = PeeweeConnectionState()
