from sqlalchemy import create_engine, Column, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/voice_assistant"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Question(Base):
    __tablename__ = "questions"

    id = Column(String, primary_key=True, index=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)

def init_db():
    Base.metadata.create_all(bind=engine)

def save_question(question, answer):
    session = SessionLocal()
    new_question = Question(question=question, answer=answer)
    session.add(new_question)
    session.commit()
    session.close()














