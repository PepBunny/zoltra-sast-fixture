"""Clean SAST fixture: parameterized query and modern password hashing."""

import hashlib
import hmac
import os


def get_user(cursor, user_id):
    cursor.execute(
        "SELECT * FROM users WHERE id = :user_id", {"user_id": user_id}
    )
    return cursor.fetchone()


def hash_password(password, salt=None):
    active_salt = salt or os.urandom(16)
    return hmac.new(active_salt, password.encode(), hashlib.sha256).hexdigest()
