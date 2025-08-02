from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session


class DatabaseConnection:

    def __init__(
        self,
        db_connection_string: str
    ):
        self.db_connection_string = db_connection_string

        self.engine = create_engine(url=self.db_connection_string, pool_size=10)
        self.SessionLocal = scoped_session(sessionmaker(bind=self.engine))
        self._session: Session | None = None


    def connect(self) -> Session:
        if self._session is None:
            self._session = self.SessionLocal()

        return self._session
    
    def close(self):
        if self._session:
            self._session.close()
            self._session = None
    

    def __enter__(self):
        return self.connect()
    
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.close()


        