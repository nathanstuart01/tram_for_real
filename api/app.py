from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_route():
    return 'Hey, we have Tram in a Docker container!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')