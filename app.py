from flask import Flask


#creates an object of the framwork
#helps it determin the rootpath

app = Flask(__name__)


#root directory
@app.route('/')


def hello_world():
    return 'Hello World!'


#calling other pages so they can run on the server
@app.route('/tuna')

def hello_tuna():
    return 'Hello World!'





#start the server or app
if __name__ == '__main__':
    app.run()
