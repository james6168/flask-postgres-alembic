from flask import Blueprint, request, jsonify
from routes.auth.schemes import RegisterUserScheme
from services.auth import register_user


auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.route("/register", methods=["POST"])
def register():


    data = RegisterUserScheme(**request.get_json())


    user = register_user(
        username=data.username,
        password=data.password,
        email=data.email
    )

    return jsonify({
        "message": "User has been created successfully", 
        "email": user.email, 
        "id": user.id
    }), 201



