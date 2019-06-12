from app.app import app, db, jwt
from app.models.rider import Rider
from flask import request, jsonify, abort
from flask_jwt_extended import jwt_required

@app.route('/api/create_rider', methods=['POST'])
@jwt_required
def create_rider():
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    if first_name is None or last_name is None:
        message = 'Invalid rider inputs, please fill in both a first and last name'
        abort(400, message)
    try:
        rider = Rider(first_name=first_name, last_name=last_name)
        db.session.add(rider)
        db.session.commit()
        return jsonify({'Message': 'New rider was created',
                        'Rider first name': first_name,
                        'Rider last name': last_name
                        }), 201
    except:
        return jsonify({'Message': 'New rider was not able to be created, something went wrong'}), 500




