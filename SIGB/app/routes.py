from flask import jsonify, request, abort
from app import app, db, bcrypt
from app.models import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

@app.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users/<int:id>', methods=['GET'])
@jwt_required()
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or not 'username' in request.json:
        abort(400)
    user = User(
        username=request.json['username'],
        email=request.json.get('email', ""),
        role=request.json.get('role', "")
    )
    user.set_password(request.json['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@app.route('/users/<int:id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    user = User.query.get_or_404(id)
    if not request.json:
        abort(400)
    
    user.username = request.json.get('username', user.username)
    user.email = request.json.get('email', user.email)
    user.role = request.json.get('role', user.role)
    if 'password' in request.json:
        user.set_password(request.json['password'])
    
    db.session.commit()
    return jsonify(user.to_dict())

@app.route('/users/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return '', 204

@app.route('/auth/login', methods=['POST'])
def login():
    if not request.json or not 'username' in request.json or not 'password' in request.json:
        abort(400)
    user = User.query.filter_by(username=request.json['username']).first()
    if user is None or not user.check_password(request.json['password']):
        abort(401)
    access_token = create_access_token(identity=user.username)
    return jsonify(access_token=access_token), 200

def not_found(error):
    return jsonify({'error': 'Not found'}), 404

def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

app.register_error_handler(404, not_found)
app.register_error_handler(400, bad_request)
