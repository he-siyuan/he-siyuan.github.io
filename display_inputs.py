from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    return f"<h1>Form Submission Results</h1><p>Name: {name}</p><p>Email: {email}</p><p>Message: {message}</p>"

if __name__ == '__main__':
    app.run(debug=True)