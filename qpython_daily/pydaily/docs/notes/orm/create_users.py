from main import Session, User, engine

# session = Session(bind=engine)

users = [
    {
        'username': 'jerry',
        'email': 'jerry@gmail.com'
    },
    {
        'username': 'tom',
        'email': 'tom@gmail.com'
    },
    {
        'username': 'oggy',
        'email': 'oggy@gmail.com'
    },
    {
        'username': 'jack',
        'email': 'jack@gmail.com'
    },
]


# add multiple users


def add_users(users):
    session = Session(bind=engine)
    for user in users:
        session.add(User(**user))
    session.commit()
    session.close()


add_users(users)
# local_session = Session(bind=engine)
# # new_user = User(username='jona',email='jona@gmail.com')

# # local_session.add(new_user)

# # local_session.commit()

# for user in users:
#     new_user = User(username=user['username'],email=user['email'])
#     local_session.add(new_user)
#     print(new_user)
#     local_session.commit()
#     print(f"user {user['username']} created")
