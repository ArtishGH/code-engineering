from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


class NotImplementedError(HTTPException):
    code = 501
    description = 'Not Implemented'


@app.errorhandler(NotImplementedError)
def handle_not_implemented_error(error):
    response = jsonify({'error': 'Not Implemented'})
    response.status_code = error.code
    return response


class UserRepository:
    def get_users(self) -> None:
        raise NotImplementedError()

    def create_user(self, user_dao) -> None:
        raise NotImplementedError()

    def update_user(self, user_id: str, user_dao) -> None:
        raise NotImplementedError()

    def partial_update_user(self, user_id: str, user_dao) -> None:
        raise NotImplementedError()

    def delete_user(self, user_id: str) -> None:
        raise NotImplementedError()


@app.route('/users', methods=['GET'])
def get_users():
    user_repository.get_users()


@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    response = jsonify(user_data)
    response.status_code = 201
    return response


@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user_data = request.get_json()
    response = jsonify(user_data)
    response.status_code = 200
    return response


@app.route('/users/<id>', methods=['PATCH'])
def partial_update_user(id):
    user_data = request.get_json()
    response = jsonify(user_data)
    response.status_code = 200
    return response


@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    response = jsonify({})
    response.status_code = 204
    return response


if __name__ == '__main__':
    user_repository = UserRepository()
    app.run()
