from posixpath import join
from main import User, Session, engine


local_session = Session(bind=engine)

# Users = local_session.query(User).all()


#return one user
# Users = local_session.query(User).filter_by(id=1).first()  

# for user in Users:
#     print(user.username)
#     # print(user.password)
#     print(user.email)
#     print(user.id)
#     print("\n")

jone = local_session.query(User).filter(User.username == 'jack').first()

print(jone)
