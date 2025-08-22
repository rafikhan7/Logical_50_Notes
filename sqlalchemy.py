import email
from sqlalchemy import create_engine, column, Integer, String, Sequence
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__="User"
    id=column(Integer, unique=True, primary_key=True)
    name=column(String, nullable=False)
    email=column(String, unique=True, nullable=False)


engine = create_engine("sqlite:///users.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ADD
user_one = User(name="rafi", email="rafiahmadkhan7@gmail.com")
session.add(user_one)
session.commit()
