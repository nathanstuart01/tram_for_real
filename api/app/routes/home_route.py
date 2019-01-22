from app import app

@app.route('/')
def home_route():
    return 'Hey, we have Tram in a Docker container!'