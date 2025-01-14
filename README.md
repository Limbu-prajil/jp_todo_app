## Todo Manager Web Application ##

** Overview **

A simple Todo Manager Web Application built with:
- Backend: Python (http.server) + PostgreSQL + psycopg2  
- Frontend: React + Vite + TypeScript

This application allows users to:
- Create new todo items
- View a list of all existing todos
- Complete or Uncomplete a todo
- Delete a todo

---------------------------------------------------------------------

** Project Structure **

jp-todoapp/
|-- backend/
|   |-- todo_backend.egg-info  # Manage backend dependencies
|   |-- server.py              # Python server
|   |-- schema.sql             # Database schema
|   |-- setup.py               # Pip installable setup
|-- frontend/
|   |-- src/
|   |   |-- App.tsx            # Main React Component
|   |   |-- index.css          # CSS for UI
|   |   |-- main.tsx           # Entry point for React
|   |-- package.json           # Frontend dependencies
|   |-- tsconfig.json          # TS config
|   |-- vite.config.ts         # Vite config
|   |-- index.html             # HTML template for UI
|   |-- eslint.config.js       # ESLint config
|   |-- README.md              # Frontend documentation
|   |-- others                 # Other json files
|-- README.md                  # Project documentation

---------------------------------------------------------------------

** Setup Instructions **

- BACKEND Setup

 1. Navigate to the backend directory:

  > cd backend

 2. Install dependencies:

  > pip install psycopg2

 3. Start the backend server:

  > python server.py

 The backend server will run at: `http://localhost:8000`

- DATABASE Setup

 1. Access PostgreSQL CLI:

  > psql -U postgres

 2. Create the database:

  > CREATE DATABASE todos_db;

 3. Switch to the new database:

  > \c todos_db;

 4. Run the schema file to create tables:

  > \i /path/to/schema.sql;

 5. Verify table creation:

  > \d todos;

 6. Insert sample data (optional):

  > INSERT INTO todos (title) VALUES ('Sample Task');
    SELECT * FROM todos;

- FRONTEND Setup (Vite + TypeScript)

 1. Navigate to the frontend directory:

  > cd frontend

 2. Install dependencies:

  > npm install

 3. Start the Vite development server:

  > npm run dev

  The frontend server will run at: `http://localhost:5173`

---------------------------------------------------------------------

** Usage **

1. Open the frontend application in your browser:  
`http://localhost:5173`

2. View Todos:
 - The existing todo items will automatically load.

3. Add a Todo:
 - Type a task in the input field and click "Add Todo".
 - Add a valid todo unless you are bored ( empty todos are also accepted :-() )  

  The task is sent to backend, the backend updates the database, sends response to frontend and gets immediately displayed on the list.

---------------------------------------------------------------------

** Tech Stack **

- Backend: Python (http.server) + PostgreSQL + psycopg2
- Frontend: React + Vite + TypeScript
- Database: PostgreSQL

---------------------------------------------------------------------

** Key Features **

- REST API (POST /todos, GET /todos, PUT /todos, DELETE /todos) for backend communication.
- State management in React with hooks (useState, useEffect).
- Python built-in http server
- Secure and efficient database connection using psycopg2.
- Clean separation of backend and frontend logic.

---------------------------------------------------------------------

** Testing **

1. Backend API Testing: Use tools like curl or Postman.
 Postman
 - Test GET /todos endpoint.
 - Test POST /todos with a JSON payload:
    {"title": "Test Task"}
 Curl
 - curl `http://localhost:8000`

2. Frontend Testing:
 - Verify todos are displayed correctly.
 - Check that adding a new task updates the list instantly.

---------------------------------------------------------------------
