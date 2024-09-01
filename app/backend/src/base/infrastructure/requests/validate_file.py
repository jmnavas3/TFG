import os
from functools import wraps

from flask import request, abort

from app.backend.configuration.configuration import Config


def validate_file(extension: str):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):

            if 'file' not in request.files:
                abort(406, {"error": "No file given"})

            file = request.files['file']

            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                abort(406, {"error": "No selected file"})

            if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in extension:
                abort(406, {"error": "Invalid file type"})

            try:
                filepath = Config.create('/config/config.yml')["NEW_RULES"]
                file.save(filepath)
                kwargs["rules_file"] = filepath
            except Exception as e:
                abort(400, {"error": str(e)})

            return f(*args, **kwargs)

        return decorated_function

    return decorator
