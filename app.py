from flask import Flask, render_template, request, redirect, session, url_for
from flask_socketio import SocketIO, emit
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'
socketio = SocketIO(app)

# Initialize Database
def init_db():
    conn = sqlite3.connect('chatroom.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        password TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password'].encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    conn = sqlite3.connect('chatroom.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
        conn.commit()
        return "User registered successfully."
    except sqlite3.IntegrityError:
        return "Username already exists."
    finally:
        conn.close()

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password'].encode('utf-8')

    conn = sqlite3.connect('chatroom.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()

    if row and bcrypt.checkpw(password, row[0]):
        session['username'] = username
        return redirect(url_for('chat'))
    return "Invalid credentials."

@app.route('/chat')
def chat():
    if 'username' in session:
        return render_template('chat.html', username=session['username'])
    return redirect(url_for('index'))

@socketio.on('send_message')
def handle_message(data):
    # Send plain text message without encryption
    emit('receive_message', {'msg': data['msg'], 'username': data['username']}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
