from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100))
    content = db.Column(db.String(500))

@app.route('/')
def index():
    messages = Message.query.all()
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

