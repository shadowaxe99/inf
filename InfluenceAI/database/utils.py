```python
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, User, Influencer, Brand, Contract, Transaction, Content

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user(db, user_id):
    return db.query(User).filter(User.id == user_id).first()

def get_influencer(db, influencer_id):
    return db.query(Influencer).filter(Influencer.id == influencer_id).first()

def get_brand(db, brand_id):
    return db.query(Brand).filter(Brand.id == brand_id).first()

def get_contract(db, contract_id):
    return db.query(Contract).filter(Contract.id == contract_id).first()

def get_transaction(db, transaction_id):
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()

def get_content(db, content_id):
    return db.query(Content).filter(Content.id == content_id).first()
```