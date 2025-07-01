from flask import Blueprint, render_template,request
import json

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/projects',methods=['GET'])
def projects():
    with open ('app/data/projects.json') as f:
        projects_data = json.load(f)
    return render_template('projects.html', projects = projects_data)

@main.route('/contact',methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # For now, just print to console or save to file
        print(f"Message from {name} ({email}): {message}")

        # Optional: Save to file
        with open('messages.txt', 'a') as f:
            f.write(f"{name} | {email} | {message}\n")

        return render_template('contact.html', success=True)

    return render_template('contact.html')