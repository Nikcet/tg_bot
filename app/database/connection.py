from typing import Optional, List
from sqlmodel import SQLModel, Session, create_engine, select
from datetime import datetime

from app import logger
from app.database.models import User


class DatabaseConnection:

    def __init__(self, db_path: str = "bot_database.db"):
        self.db_path = db_path
        self.engine = create_engine(f"sqlite:///{db_path}", echo=False)
        self._init_database()

    def _init_database(self):
        try:
            SQLModel.metadata.create_all(self.engine)
            logger.info("База данных инициализирована")
        except Exception as e:
            logger.error(f"Ошибка при инициализации базы данных: {e}")
            raise

    def get_session(self) -> Session:
        return Session(self.engine)

    def create_user(
        self,
        user_id: int,
        first_name: str,
        last_name: Optional[str] = None,
        username: Optional[str] = None,
    ) -> Optional[User]:
        try:
            with self.get_session() as session:
                user = User(
                    id=user_id,
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                )
                session.add(user)
                session.commit()
                session.refresh(user)
                logger.info(f"Создан пользователь: {user_id}")
                return user
        except Exception as e:
            logger.error(f"Ошибка при создании пользователя: {e}")
            return None

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        try:
            with self.get_session() as session:
                statement = select(User).where(User.id == user_id)
                user = session.exec(statement).first()
                return user
        except Exception as e:
            logger.error(f"Ошибка при получении пользователя: {e}")
            return None

    def update_user_activity(self, user_id: int) -> bool:
        try:
            with self.get_session() as session:
                statement = select(User).where(User.id == user_id)
                user = session.exec(statement).first()
                if user:
                    user.last_activity = datetime.now()
                    session.add(user)
                    session.commit()
                    return True
                return False
        except Exception as e:
            logger.error(f"Ошибка при обновлении активности пользователя: {e}")
            return False

    def get_all_users(self) -> List[User]:
        try:
            with self.get_session() as session:
                statement = select(User)
                users = list(session.exec(statement).all())
                return users
        except Exception as e:
            logger.error(f"Ошибка при получении пользователей: {e}")
            return []

    def delete_user(self, user_id: int) -> bool:
        try:
            with self.get_session() as session:
                statement = select(User).where(User.id == user_id)
                user = session.exec(statement).first()
                if user:
                    session.delete(user)
                    session.commit()
                    logger.info(f"Удален пользователь: {user_id}")
                    return True
                return False
        except Exception as e:
            logger.error(f"Ошибка при удалении пользователя: {e}")
            return False
