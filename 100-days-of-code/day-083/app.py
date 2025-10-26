from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    skills = ["Python", "Flask", "JavaScript", "HTML/CSS", "Data Analysis"]
    return render_template('index.html', skills=skills)

# Projects route
@app.route('/projects')
def projects():
    projects = [
        {"name": "Portfolio Website", "description": "A personal site built with Flask", "link": "#"},
        {"name": "Data Dashboard", "description": "Interactive dashboard using Plotly", "link": "#"},
        {"name": "Chatbot", "description": "A simple NLP chatbot built with Python", "link": "#"}
    ]
    return render_template('projects.html', projects=projects)

# Contact route
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
