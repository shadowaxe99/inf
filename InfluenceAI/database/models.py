```python
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Influencer(Base):
    __tablename__ = 'influencers'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    social_media_handle = Column(String)
    follower_count = Column(Integer)
    engagement_rate = Column(Float)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Brand(Base):
    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    name = Column(String)
    industry = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Contract(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, primary_key=True)
    influencer_id = Column(Integer)
    brand_id = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    payment_amount = Column(Float)
    payment_currency = Column(String)
    is_signed = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    contract_id = Column(Integer)
    transaction_hash = Column(String)
    status = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Content(Base):
    __tablename__ = 'contents'

    id = Column(Integer, primary_key=True)
    influencer_id = Column(Integer)
    title = Column(String)
    description = Column(String)
    scheduled_date = Column(DateTime)
    keywords = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
```