# Chat Application

A real-time chat application built using Django, HTML, CSS, and JavaScript. This app allows users to sign up, log in, create rooms, set their usernames, and participate in real-time chats with other users in the same room.

## Features

- **Sign Up**: Users can create a new account by providing their email, username, and password.
- **Login**: Registered users can log in to their account using their credentials.
- **Create Room**: Users can create a unique chat room.
- **Set User Name**: Users can set their display name before joining the chat room.
- **Real-time Chat**: Users can send and receive messages in real-time with other users in the same room.

## Technologies Used

- **Django**: The web framework used for backend development.
- **HTML/CSS**: For structuring and styling the web pages.
- **JavaScript**: For handling front-end interactions and real-time messaging.
- **Channels**: Django Channels is used to implement WebSockets for real-time chat functionality.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```
2. Create a virtual environment (optional but recommended):

```bash
  python -m venv venv
  source venv/bin/activate  # On Windows, use venv\Scripts\activate
```
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```
4. Apply database migrations:

```bash
python manage.py migrate
```
5. Run the development server:

```bash
python manage.py runserver
```
6. Open your browser and visit http://127.0.0.1:8000/ to access the chat application.

## Usage

- After accessing the website, you'll be prompted to sign up or log in.
- Once logged in, you can create or join a chat room by entering a room name.
- Choose a user name to represent yourself in the chat room.
- Start chatting with other users in the room.

## Future Enhancements

- Add private messaging between users.
- Implement notifications when new users join the room.
- Integrate advanced styling with frameworks like Bootstrap or Tailwind CSS.
- Implement a logout feature to allow users to safely exit their account.
- Add media file sharing (images, videos, etc.) in chat rooms, similar to WhatsApp.
