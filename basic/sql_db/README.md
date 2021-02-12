## sql_db

- SQLAlchemy를 통해 지원하는 db는 아래와 같다.
  - PostgreSQL
  - MySQL
  - SQLite
  - Oracle
  - Microsoft SQL Server
  
- ORM 이란?
  - ORM은 Object-Releational Mapping으로 코드 내 object와 db table을 매핑해준다.
  - 여기선 SQLAlchemy ORM을 통해 어떻게 구현하는지 알아본다.
  
- 기본 구조
  - crud.py
  - database.py
  - main.py
  - moedls.py
  - schemas.py
  
- 세부 내용
  - database.py
    - SQLAlchemy을 생성한다.
    - SQLAlchemy를 통해 db connection을 위한 session을 생성한다.
  
  - models.py
    - DB model을 위한 class를 생성한다.
  
  - schemas.py
    - Pydantic model을 생성한다.
    - schema 관련된 코드를 생성한다.
  
  - crud.py
    - crud 기능에 관한 코드를 생성한다.
  
- Alembic
  - SQLAlchemy에서 DB Migration을 위한 툴 (https://alembic.sqlalchemy.org/en/latest/)
  
 