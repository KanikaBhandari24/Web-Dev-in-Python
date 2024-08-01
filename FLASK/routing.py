from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/bye')
# @make_bold
# @make_emphasis
def bye():
    return('Bye World!')

@app.route('/<name>')
def greet(name):
    return f'Hello {name}!'

@app.route('/<name>/<int:num>')
def hello(name, num):
    return f'<h1 style="text-align:center">Hello {name}, you are {num} years old!</h1>'\
            '<h2 style="text-align:center">Hey Cutie!</h2>'\
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOG1qNXRxMzJyODBldG1oMTd5bjVkeXo4OHRkNmtuN3pubWJ6OGxndCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LQSo1H5ij66yI/giphy.gif">'

if __name__ == '__main__':
    app.run(debug=True) #reloads the server automatically 