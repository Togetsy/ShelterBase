import hashlib
import secrets

from repositories import user_repository

def hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        100000
    ).hex()

    return password_hash, salt

def register_user(username, password, role):
    if role not in ("admin", "employee"):
        return False

    password_hash, salt = hash_password(password)

    user_repository.add_user(
        username,
        password_hash,
        salt,
        role
    )

    return True

def login_user(username, password):
    user = user_repository.get_user_by_username(username)

    if user is None:
        return None

    password_hash, _ = hash_password(password, user.salt)

    if password_hash == user.password_hash:
        return user

    return None

def create_first_admin(username, password):
    if user_repository.count_users() > 0:
        return False

    if not username or not password:
        return False

    return register_user(username, password, "admin")

def create_employee(current_user, username, password):
    if current_user.role != "admin":
        return False

    if not username or not password:
        return False

    if user_repository.get_user_by_username(username) is not None:
        return False

    return register_user(username, password, "employee")

def delete_employee(current_user, username):
    if current_user.role != "admin":
        return False

    if current_user.username == username:
        return False

    return user_repository.delete_employee(username)
