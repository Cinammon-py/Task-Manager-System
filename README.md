# Simple Task Management System

This is a simple task management system built using Flask. It allows users to add, edit, delete, and mark tasks as complete or incomplete. 

## Features
- Add, edit, delete tasks
- Mark tasks as complete or incomplete
- Simple UI with embedded CSS for styling

## Technologies Used
- Python (Flask framework)
- HTML5/CSS3
- JavaScript (for dynamic flash messages and button behavior)

## Installation Instructions

### Prerequisites

### 1. Clone the Repository
```
git clone https://github.com/Cinammon-py/Simple-Task-Management-System.git
cd Simple-Task-Management-System
```
### 2. Set up a Virtual Environment
Create a virtual environment to isolate dependencies:

```
python -m venv venv
```
Activate the virtual environment:

On Windows:

```
venv\Scripts\activate
```
On macOS/Linux:
```
source venv/bin/activate
```

### 3. Install the Required Dependencies
Install the project dependencies listed in the requirements.txt file:

```
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a .env file in the root directory of the project. Inside the .env file, add the following line:

```
FLASK_SECRET_KEY="your-own-secret-key"
```
You can generate your own secret key and replace it with "your-own-secret-key"

### 5. Running the Application
After setting up your environment variables, run the Flask app:

```
flask run
```
By default, the application will be available at http://127.0.0.1:5000/.

### Known Limitations
#### No User Authentication:

- Limitation: Tasks are globally accessible without personalized user accounts.
- Improvement: Add user authentication for personal task lists.

#### No Persistent Storage by Default:

- Limitation: Tasks are lost when the server restarts.
- Improvement: Implement SQLite or another database for persistent storage.

#### Limited Task Organization:

- Limitation: No support for task prioritization, sub-tasks, or recurring tasks.
- Improvement: Add features for task prioritization, categorization, and recurring tasks.

#### Flash Messages:

- Limitation: Flash messages disappear after a set time and are not manually dismissible.
- Improvement: Add manual dismissal for better usability.

