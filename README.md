# Real-Time Multiplayer Tic Tac Toe

A real-time multiplayer Tic Tac Toe game built with Django Channels, Redis, and Daphne. Players can create game rooms and play against each other in real-time using WebSocket connections.

## Features

- Real-time gameplay using WebSocket connections
- Room-based multiplayer system
- User authentication
- Room creation and joining functionality
- Responsive design
- Real-time game state updates

## Tech Stack

- **Backend**
  - Django
  - Django Channels (for WebSocket support)
  - Redis (as channel layer)
  - Daphne (ASGI server)

- **Frontend**
  - HTML5
  - CSS3
  - JavaScript (Vanilla)

## Prerequisites

Before running this project, make sure you have the following installed:
- Python 3.8+
- Redis Server
- pip (Python package manager)

## Installation

1. Clone the repository
```bash
git clone https://github.com/sathwikshetty33/tic-tac-toe.git
cd game
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up Redis
- Make sure Redis server is running on your machine
- For Windows users, you can use [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install) or [Redis Windows](https://github.com/microsoftarchive/redis/releases)

5. Apply database migrations
```bash
python manage.py migrate
```

6. Run the redis server 
```bash
redis-server --port 6380 
```


## How to Play

1. Create an account or log in
2. Choose to either create a new game room or join an existing one
3. If creating a room, share the room code with your opponent
4. If joining a room, enter the room code provided by the room creator
5. Play the game! The game updates in real-time for both players

## Deployment

To deploy this application, you'll need:
- A server with Python and Redis installed
- ASGI server (Daphne)

Basic deployment steps:
1. Set up your production server
2. Install required dependencies
3. Configure your database
4. Set up Redis
5. Run Daphne server


## Acknowledgments

* Django Channels documentation
* Redis documentation
* WebSocket protocol
