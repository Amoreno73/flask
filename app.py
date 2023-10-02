from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'description': 'This is a job description'

    },
    {
        'id': 2,
        'title': 'Software Engineer',
        'description': 'This is a job description'
    },
    {
        'id': 3,
        'title': 'Software Engineer',
        'description': 'This is a job description'
    },

]

@app.route('/')
def index():
    return render_template('index.html', jobs = JOBS)
    
    
if __name__ == "__main__":
    app.run(debug = True)
