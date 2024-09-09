import os
from flask import Flask, render_template, request, redirect, url_for, flash

from dotenv import load_dotenv

load_dotenv() 

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')  

# In-memory task storage
tasks = []
task_id_counter = 1

# Home route to display tasks
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Route to add a new task
@app.route('/add_task', methods=['POST'])
def add_task():
    global task_id_counter
    title = request.form['title']
    description = request.form['description']
    
    if not title or not description:
        flash("Please provide both a title and description for the task.")
        return redirect(url_for('index'))
    
    new_task = {
        'id': task_id_counter,
        'title': title,
        'description': description,
        'complete': False
    }
    
    tasks.append(new_task)
    task_id_counter += 1
    
    flash('Task added successfully!')
    return redirect(url_for('index'))

# Route to toggle task completion status
@app.route('/toggle_complete/<int:task_id>', methods=['POST'])
def toggle_complete(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['complete'] = not task['complete']
        status = 'completed' if task['complete'] else 'incomplete'
        flash(f"Task '{task['title']}' marked as {status}.")
    else:
        flash('Task not found.')
    
    return redirect(url_for('index'))

# Route to delete a task
@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    flash('Task deleted successfully.')
    return redirect(url_for('index'))

# Route to edit a task 
@app.route('/edit_task/<int:task_id>', methods=['GET'])
def edit_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return render_template('edit_task.html', task=task)
    else:
        flash('Task not found.')
        return redirect(url_for('index'))

# Route to update a task
@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        flash(f"Task '{task['title']}' updated successfully.")
    else:
        flash('Task not found.')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
