from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    greeting = f'Hello, {name}! Welcome to our Flask app!'
    return render_template('greet.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
