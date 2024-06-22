from sqlalchemy.orm import Session
from typing import List

from app.db import models, schemas

class UserService:
    @staticmethod
    def create_user(db: Session, user: schemas.UserCreate) -> models.User:
        db_user = models.User(name=user.name, email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def get_user(db: Session, user_id: int) -> models.User:
        return db.query(models.User).filter(models.User.id == user_id).first()

    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 10) -> List[models.User]:
        return db.query(models.User).offset(skip).limit(limit).all()

    @staticmethod
    def update_user(db: Session, user_id: int, user: schemas.UserCreate) -> models.User:
        db_user = db.query(models.User).filter(models.User.id == user_id).first()
        if db_user is None:
            return None
        db_user.name = user.name
        db_user.email = user.email
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def delete_user(db: Session, user_id: int) -> models.User:
        db_user = db.query(models.User).filter(models.User.id == user_id).first()
        if db_user is None:
            return None
        db.delete(db_user)
        db.commit()
        return db_user
