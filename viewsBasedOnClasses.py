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
    def get_users(self):
        raise NotImplementedError()

    def create_user(self, user_dao):
        raise NotImplementedError()

    def update_user(self, user_id, user_dao):
        raise NotImplementedError()

    def partial_update_user(self, user_id, user_dao):
        raise NotImplementedError()

    def delete_user(self, user_id):
        raise NotImplementedError()


class UserController:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_users(self):
        self.user_repository.get_users()

    def create_user(self, user_dto):
        self.user_repository.create_user(user_dto)

    def update_user(self, user_id, user_dto):
        self.user_repository.update_user(user_id, user_dto)

    def partial_update_user(self, user_id, user_dto):
        self.user_repository.partial_update_user(user_id, user_dto)

    def delete_user(self, user_id):
        self.user_repository.delete_user(user_id)


class UserView:
    def __init__(self, user_controller):
        self.user_controller = user_controller

    def get(self):
        self.user_controller.get_users()

    def post(self):
        user_data = request.get_json()
        response = jsonify(user_data)
        response.status_code = 201
        return response

    def put(self, user_id):
        user_data = request.get_json()
        response = jsonify(user_data)
        response.status_code = 200
        return response

    def patch(self, user_id):
        user_data = request.get_json()
        response = jsonify(user_data)
        response.status_code = 200
        return response

    def delete(self, user_id):
        response = jsonify({})
        response.status_code = 204
        return response


if __name__ == '__main__':
    user_repository = UserRepository()
    user_controller = UserController(user_repository)
    user_view = UserView(user_controller)

    app.add_url_rule('/users', view_func=user_view.get, methods=['GET'])
    app.add_url_rule('/users', view_func=user_view.post, methods=['POST'])
    app.add_url_rule('/users/<id>', view_func=user_view.put, methods=['PUT'])
    app.add_url_rule('/users/<id>', view_func=user_view.patch, methods=['PATCH'])
    app.add_url_rule('/users/<id>', view_func=user_view.delete, methods=['DELETE'])

    app.run()
