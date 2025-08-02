from database.models.auth import User
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest
from flask import g, jsonify


def register_user(
    username: str,
    email: str,
    password: str
) -> User:
    # Check whether user already exists
    if (
        g.db_session.query(User).filter(User.email == email).first()
    ):
        response = jsonify({"error": f"User with email: {email} already exists"})
        response.status_code = 400
        raise BadRequest(
            response=response
        )

    
    password_hash = generate_password_hash(password=password, method="pbkdf2:sha256", salt_length=8)

    new_user = User(
        email=email,
        password_hash=password_hash,
        username=username
    )

   
    g.db_session.add(new_user)
    g.db_session.commit()


    return new_user
    