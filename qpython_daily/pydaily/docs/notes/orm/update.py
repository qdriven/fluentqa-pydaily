from main import User, Session, engine

local_session = Session(bind=engine)

user_to_update = local_session.query(
    User).filter(User.username == 'jack').first()


user_to_update.username='jackathone'
user_to_update.email='jackathione@gmail.com'

local_session.commit()