from app import app, db
from app.models.user import User
from flask import request, jsonify, abort, session

# will need to make these requests over a secure http
# this route will be included in the signup view page
@app.route('/api/create_user', methods=['POST'])
def create_user():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')

    if username is None or email is None or password is None:
        abort(400) #missing arguments
    if User.query.filter_by(username = username).first() is not None:
        abort(400) #existing user
    if User.query.filter_by(email = email).first() is not None:
        abort(400) #existing email
    user = User(username = username, email = email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.username}), 201

# create a login route for an already created user
#diagram out the steps needed to login and access protected resources
@app.route('/api/login', methods=['POST'])
def login_user():
    email = request.json.get('email')
    password = request.json.get('password')
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        session['logged_in'] = True
        status = 'logged in'
    else:
        status = 'invalid login credentials, please try again'

    return jsonify({'result': status})



