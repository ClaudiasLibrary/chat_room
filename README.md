# Chat Application with Flask and SocketIO

This is a simple real-time chat application built with Flask, Flask-SocketIO, and SQLite. It allows users to register, log in, and join a chat room where they can send and receive messages in real-time.

## Features

- **User Registration**: Users can register by creating a unique username and password. Passwords are hashed using `bcrypt` for security.
- **User Login**: Users can log in using their credentials. The application compares the hashed password stored in the database with the entered password.
- **Real-Time Chat**: Users can chat with each other in real-time using `SocketIO`. Messages are broadcast to all connected clients.
- **Session Management**: User sessions are managed using Flask’s built-in session system to keep track of logged-in users.

## Technologies Used

- **Flask**: Web framework for building the application.
- **Flask-SocketIO**: Real-time communication library for Flask that enables WebSocket support.
- **SQLite**: Lightweight database for storing user credentials.
- **bcrypt**: Password hashing library used to securely store user passwords.

## Installation

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Run the Application

After installing the dependencies, you can start the application by running:

```bash
python app.py
```

By default, the application will be accessible at `http://localhost:5000/`.

## Database

The application uses SQLite to store user data. The database file `chatroom.db` will be created automatically when the application runs for the first time. If the database does not exist, the application will create it with the following schema:

- **users** table:
  - `id`: Integer, Primary Key, Auto Increment
  - `username`: Text, Unique (used for user login)
  - `password`: Text (hashed password)

## Routes

- `/` (GET): Displays the registration and login form.
- `/register` (POST): Registers a new user. It accepts `username` and `password` from the form, hashes the password, and stores it in the database.
- `/login` (POST): Logs in an existing user. It accepts `username` and `password`, verifies the password using bcrypt, and redirects to the chat room if the login is successful.
- `/chat` (GET): Displays the chat room where logged-in users can send and receive messages.

## Real-Time Chat with SocketIO

- **`send_message`**: Emitted from the client when a user sends a message. This event broadcasts the message to all connected clients.
- **`receive_message`**: Received by all connected clients to display incoming messages.

## Security Considerations

- **Password Hashing**: User passwords are hashed using `bcrypt` before being stored in the database, making it difficult for attackers to retrieve original passwords even if the database is compromised.
- **Session Management**: Flask’s built-in session management ensures that users are properly authenticated and only logged-in users can access the chat room.

## License

This project is licensed under the MIT License

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## Acknowledgments

- **Flask**: For building the web application.
- **Flask-SocketIO**: For enabling real-time communication in the chat application.
- **bcrypt**: For securely hashing passwords.
- **SQLite**: For lightweight database storage.
