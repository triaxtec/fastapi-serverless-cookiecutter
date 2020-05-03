from pathlib import Path
from typing import Iterator, Optional

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

Base = declarative_base()
SessionLocal: Optional[sessionmaker] = None
engine: Optional[Engine] = None


def init_db() -> None:
    """ Initialize database connections based on config """
    from .config import get_config

    global SessionLocal, engine

    _config = get_config()
    sqlalchemy_database_url = _config["database_url"]

    connect_args = {}
    if get_config()["env"] != "local":  # pragma: no cover
        # Use SSL to connect to databases
        _ca_pem_path = Path(__file__).parent / "rds-ca-2019-root.pem"
        connect_args = {"ssl": {"ca": str(_ca_pem_path.absolute())}}

    engine = create_engine(sqlalchemy_database_url, connect_args=connect_args, pool_pre_ping=True)
    Base.metadata.bind = engine
    SessionLocal = sessionmaker(autoflush=False, bind=engine)

    if _config.get("scout"):  # pragma: no cover
        from scout_apm.sqlalchemy import instrument_sqlalchemy

        instrument_sqlalchemy(engine)


def get_session() -> Iterator[Session]:
    """ Injectable database session """
    if SessionLocal is None:
        raise ImportError("You need to call init_db before this function!")
    session = None
    try:
        session = SessionLocal()
        yield session
    finally:
        if session:
            session.close()
