from app import app

@app.route('/')
def home_and_login_route():
    return 'Tram home'
