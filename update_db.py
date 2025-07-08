from app import app, db, Message

with app.app_context():
    msg1 = Message(sender="Azure VM", content="🎉 App is now running on Azure VM with migrated database!")
    msg2 = Message(sender="Migration Log", content="✅ Migration from AWS EC2 to Azure VM was successful.")
    db.session.add(msg1)
    db.session.add(msg2)
    db.session.commit()
    print("Azure messages inserted into database.")

