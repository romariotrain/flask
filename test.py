from models import Session, User, Post

with Session() as session:
    users = session.query(User).all()
    for i in users:
        for u in i.posts:
            print(u.owner)