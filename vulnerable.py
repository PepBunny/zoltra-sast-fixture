"""Deliberately vulnerable SAST fixture (do not copy into product code)."""

import hashlib  # noqa: I001 — fixture layout is intentional


AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def get_user(cursor, user_id):
    cursor.execute("SELECT * FROM users WHERE id = '%s'" % user_id)  # noqa: UP031
    return cursor.fetchone()


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
