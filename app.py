# A simple web server to receive images, transfer style to them, and post them elsewhere.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'MOD. says hi hello. x'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

