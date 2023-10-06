from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Accounts(BaseModel, Base):
    __tablename__ = 'accounts'
    user_id = Column(String(255), ForeignKey('users.id'), nullable=False)
    account_number = Column(String(255), nullable=False, unique=True)
    Total_funds = Column(Integer, nullable=False)
    incomming_funds = Column(Integer, nullable=False)
    outgoing_funds = Column(Integer, nullable=False)

    user = relationship("User", back_populates="accounts")

    def __init__(self, *args, **kwargs):
        """Initialize the account"""
        super().__init__(*args, **kwargs)
