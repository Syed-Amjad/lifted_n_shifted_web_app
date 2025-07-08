from app import db, Message

db.create_all()
msg1 = Message(sender="AWS Server", content="Welcome! This is your cloud-hosted app.")
msg2 = Message(sender="Migration Bot", content="Prepare to lift and shift to Azure!")
db.session.add(msg1)
db.session.add(msg2)
db.session.commit()
print("Database initialized.")

