from app.app import app, db, jwt, blacklist
from app.models.user import User
from flask import request, jsonify, abort
from flask_jwt_extended import (JWTManager, create_access_token, create_refresh_token, 
                                jwt_required, jwt_refresh_token_required, 
                                get_jwt_identity, get_raw_jwt, get_jwt_claims,
                                set_access_cookies, set_refresh_cookies, unset_jwt_cookies)


@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    return {
        'user_id': identity['user_id'],
        'username': identity['username']
    }

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist

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
    try:
        user = User(username = username, email = email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'user was created',
                        'username': user.username,
                        'email': user.email}), 201
    except:
        return jsonify({'message': 'Something went wrong when registering your username'}), 500
#curl -i -X POST -H "Content-Type: application/json" -d '{"username":"user_2","email": "test2@test.com", "password":"password"}' http://localhost:5000/api/create_user

# endpoint for granting a user an access token
@app.route('/api/login', methods=['POST'])
def login_user():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        user_object = {"user_id": user.id, "username": username}
        access_token = create_access_token(identity=user_object)
        resp = jsonify({'login': True, 'access_token': access_token})
        return resp, 200
    else:
        return jsonify({'message': 'invalid login credentials, please try again'}), 401
#curl -i -X POST -H "Content-Type: application/json" -d '{"username":"user","password":"password"}' http://localhost:5000/api/login
#export ACCESS=

# Endpoint for revoking the current users access token, #still able to access protected routes after getting sign out successful 
@app.route('/api/logout', methods=['DELETE'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify({"msg": "Successfully logged out"}), 200

#curl -i -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer $ACCESS" http://localhost:5000/api/logout

@app.route('/api/update_user_password', methods=['PUT'])
@jwt_required
def update_user_password():
    current_user_info = get_jwt_claims()
    user_id = current_user_info['user_id']
    user = User.query.filter(User.id == user_id).first()
    user_new_password = request.json.get('user_new_password')
    user_confirm_new_password = request.json.get('user_confirm_new_password')
    if user_new_password == user_confirm_new_password:
        try:
            user.set_password(user_confirm_new_password)
            db.session.add(user)
            db.session.commit()
            return jsonify({'updated_user_password': 'Your password was updated successfully!' }), 200
        except Exception as e:
            return jsonify({'unable to update user password': e.ergs }), 500
    else:
        return jsonify({'unable to update user password': 'passwords do not match'}), 500
#curl -i -X PUT -H "Authorization: Bearer $ACCESS" -H "Content-Type: application/json" -d '{"user_new_password":"password", "user_confirm_new_password": "password"}' http://localhost:5000/api/update_user_password






