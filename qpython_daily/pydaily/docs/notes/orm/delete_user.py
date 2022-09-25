from sqlalchemy.orm import session
from main import Session, engine, User

session = Session(bind=engine)
# # delete user from database


def delete_user(session):
    # user = session.query(User).filter(us).first()
    user = session.query(User).all()
    session.delete(user)
    session.commit()
    return "User deleted"


# delete_user(session)

# delete all users from database
def delete_all_users(session):
    # user = session.query(User).filter(us).first()
    Users = session.query(User).all()
    for user in Users:
        session.delete(user)
        session.commit()
    return "All users deleted"


# delete_all_users(session)

# local_session = Session(bind=engine)


# user_to_del = local_session.query(User).filter(User.username == 'oggy').first()


# local_session.delete(user_to_del)

# local_session.commit()
