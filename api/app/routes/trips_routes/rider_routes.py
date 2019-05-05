from app import app, jwt
from flask import jsonify
from flask_jwt_extended import jwt_required

@app.route('/api/show_all_trips', methods=['GET'])
@jwt_required
def show_all_joinable_trips():
    # make a list of all trips with seats available
    return jsonify({'trips': 'trip 1'}), 200

@app.route('/api/create_trip', methods=['POST'])
@jwt_required
def create_trip():
    print('create trip route')